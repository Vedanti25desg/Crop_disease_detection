import os, uuid
from flask import Flask, render_template, request, redirect, url_for, abort
from PIL import Image

import database
from remedies import get_info, build_remedies
from model import multipart          # TensorFlow models load lazily on first use

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
ALLOWED = {"png", "jpg", "jpeg"}
PART_LABELS = {"leaf": "Leaf", "fruit": "Fruit", "stem": "Stem", "flower": "Flower", "root": "Roots"}
FORM_FIELDS = ["discoloration", "wilting", "weather", "temperature",
               "fertilizer", "pesticide", "insects", "pest_damage"]

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024   # 16 MB
os.makedirs(UPLOAD_DIR, exist_ok=True)
database.init_db()


def home_error(msg, code=400):
    return render_template("home.html", error=msg), code


def result_page(rec, remedies=None):
    part = rec["part"] or "leaf"
    return render_template(
        "result.html", record_id=rec["id"], prediction=get_info(rec["disease_key"])["name"],
        confidence=round(rec["confidence"], 2), filename=rec["original_name"],
        part_label=PART_LABELS.get(part, part.title()), part_confidence=rec["part_confidence"],
        notice=rec["note"], image_url=url_for("static", filename="uploads/" + rec["image"]),
        remedies=remedies)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/history")
def history():
    items = [{"id": r["id"], "image_url": url_for("static", filename="uploads/" + r["image"]),
              "disease": get_info(r["disease_key"])["name"],
              "part": PART_LABELS.get(r["part"] or "leaf", "Leaf"),
              "confidence": round(r["confidence"], 2), "date": r["created_at"]}
             for r in database.list_records()]
    return render_template("history.html", history=items)


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("image")
    if not file or not file.filename:
        return home_error("Please choose an image first.")
    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ALLOWED:
        return home_error("Unsupported file type. Please upload a JPG or PNG image.")

    name = f"{uuid.uuid4().hex}.{ext}"
    path = os.path.join(UPLOAD_DIR, name)
    file.save(path)
    try:
        Image.open(path).verify()
    except Exception:
        os.remove(path)
        return home_error("That file is not a valid image. Please try another one.")

    res = multipart.analyze(path, request.form.get("part", "auto"))

    if res["status"] == "not_tomato":
        os.remove(path)
        return home_error("This does not look like a tomato plant part (leaf, fruit, stem, flower or roots). Please upload a clear tomato photo.")
    if res["status"] == "no_disease_model":
        os.remove(path)
        label = PART_LABELS.get(res["part"], res["part"])
        return home_error(f"Detected part: {label}. The disease model for this part is not installed yet. See the README to train and add it.", 200)

    # ==========================================
    # TWO-TIERED CONFIDENCE THRESHOLD HEURISTIC
    # ==========================================
    confidence = res.get("confidence", 0)

    # Tier 1: Reject Out-of-Distribution / Junk Data (< 66%)
    if confidence < 83.2:
        os.remove(path)
        return home_error("Image unrecognized or confidence too low (< 83.2%). Please retry with a clear tomato leaf or fruit photo.")

    # Tier 2: Low-confidence warning flag (66% - 75%)
    elif 83.2 <= confidence < 75.0:
        warning_msg = "Warning: Image clarity is low or symptoms are ambiguous. Please verify diagnosis."
        existing_notice = res.get("notice") or ""
        res["notice"] = f"{existing_notice} {warning_msg}".strip()
    # ==========================================

    rid = database.add_record(name, file.filename, res["disease_key"], res["confidence"],
                              res["part"], res["part_confidence"], res["notice"])
    return redirect(url_for("result", rid=rid))

@app.route("/result/<int:rid>")
def result(rid):
    rec = database.get_record(rid)
    if rec is None:
        abort(404)
    return result_page(rec)


@app.route("/result")
def result_root():
    return redirect(url_for("index"))


@app.route("/remedies", methods=["POST"])
def remedies():
    rec = database.get_record(request.form.get("record_id", type=int))
    if rec is None:
        abort(404)
    answers = {f: request.form.get(f, "") for f in FORM_FIELDS}
    return result_page(rec, remedies=build_remedies(rec["disease_key"], answers))


@app.errorhandler(413)
def too_large(_):
    return home_error("Image is too large. Maximum size is 16 MB.", 413)


if __name__ == "__main__":
    # use_reloader=False avoids loading TensorFlow twice
    app.run(debug=True, use_reloader=False)
