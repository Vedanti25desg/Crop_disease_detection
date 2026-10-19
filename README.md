# Tomato Crop Disease Detection (Flask + Keras)

Detects the plant part (leaf, fruit, stem, flower, roots) and then the disease of that part.

## Python version
TensorFlow supports Python 3.10-3.13 only (not 3.14). Use Python 3.12.

## Run (Windows PowerShell, inside this folder)
    py -3.12 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

## Model files (put inside model/)
| File pair | Purpose |
|---|---|
| tomato_cnn.keras + class_indices.json | Leaf diseases (already included) |
| part_model.keras + part_classes.json | Part classifier: leaf/fruit/stem/flower/root/other |
| fruit_model.keras + fruit_classes.json | Fruit diseases |
| stem_model.keras + stem_classes.json | Stem diseases |
| flower_model.keras + flower_classes.json | Flower diseases |
| root_model.keras + root_classes.json | Root diseases |

Only the leaf model is included now. The others are created by notebooks/Train_Multipart_Models.ipynb
(run it in Google Colab, download the zip it makes, copy its files into model/).
The website uses whichever models exist:
- No part_model: the image is treated as a leaf (or the part you choose in the upload form).
- Part detected but its disease model missing: the site says that part's model is not installed yet.
- Part = "other": the site asks for a tomato photo.

## Optional images
static/img/bg.jpg and static/img/classes/<name>.jpg for the home gallery.
