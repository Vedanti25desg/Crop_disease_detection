"""Two-stage predictor: (1) which tomato part is in the photo, (2) which disease that part has.

Files looked for inside this folder (all optional, loaded only when present):
    part_model.keras  + part_classes.json      -> part classifier (leaf/fruit/stem/flower/root/other)
    <part>_model.keras + <part>_classes.json   -> disease model for that part
    tomato_cnn.keras  + class_indices.json     -> original leaf model (used for leaf if leaf_model.keras is absent)
"""
import os, json
import numpy as np
from PIL import Image

DIR = os.path.dirname(os.path.abspath(__file__))
PARTS = ["leaf", "fruit", "stem", "flower", "root"]
_cache = {}


def _load(model_file, json_file):
    mp, jp = os.path.join(DIR, model_file), os.path.join(DIR, json_file)
    if not (os.path.exists(mp) and os.path.exists(jp)):
        return None
    if model_file not in _cache:
        import tensorflow as tf            # imported lazily so the site starts fast
        with open(jp) as f:
            meta = json.load(f)
        _cache[model_file] = (tf.keras.models.load_model(mp), meta)
    return _cache[model_file]


def _predict(bundle, path):
    model, meta = bundle
    size = meta.get("img_size", 160)
    img = Image.open(path).convert("RGB").resize((size, size))
    probs = model.predict(np.expand_dims(np.array(img, dtype="float32"), 0), verbose=0)[0]
    i = int(np.argmax(probs))
    return meta["keys_by_index"][i], float(probs[i]) * 100


def _disease_bundle(part):
    b = _load(f"{part}_model.keras", f"{part}_classes.json")
    if b is None and part == "leaf":
        b = _load("tomato_cnn.keras", "class_indices.json")
    return b


def analyze(path, part_choice="auto"):
    """Returns dict: status ('ok' | 'not_tomato' | 'no_disease_model'), part, part_confidence,
    disease_key, confidence, notice."""
    r = {"status": "ok", "part": None, "part_confidence": None,
         "disease_key": None, "confidence": None, "notice": None}
    part_bundle = _load("part_model.keras", "part_classes.json")

    if part_choice in PARTS:
        part = part_choice
    elif part_bundle:
        part, pc = _predict(part_bundle, path)
        if part not in PARTS:                       # "other" = not a tomato plant part
            r.update(status="not_tomato", part=part)
            return r
        r["part_confidence"] = round(pc, 2)
        if pc < 60:
            r["notice"] = "The system is not very sure which plant part this is. Try a closer, clearer photo of one part."
    else:
        part = "leaf"
        r["notice"] = ("Automatic part detection is not installed yet, so this image was treated as a leaf. "
                       "Choose the part manually on the upload form if it is a different part.")
    r["part"] = part

    bundle = _disease_bundle(part)
    if bundle is None:
        r["status"] = "no_disease_model"
        return r
    key, conf = _predict(bundle, path)
    r.update(disease_key=key, confidence=round(conf, 2))
    return r
