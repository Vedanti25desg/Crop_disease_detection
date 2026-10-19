"""Disease information + remedies, keyed by the model's `keys_by_index` names."""

REMEDIES = {
 "bacterial_spot": {"name": "Tomato Bacterial Spot",
  "about": "Caused by Xanthomonas bacteria. Small dark, water-soaked spots appear on leaves and fruit, and spread by splashing water in wet weather.",
  "treatment": ["Remove and destroy badly infected leaves; do not compost them.",
                "Spray a copper-based bactericide, following the product label and repeating as directed.",
                "Stop overhead watering and avoid touching plants while they are wet."],
  "prevention": ["Use certified disease-free seed and seedlings.",
                 "Rotate with non-tomato/pepper crops for 2-3 years.",
                 "Use drip irrigation and clean tools between plants.", "Clear crop debris after harvest."]},
 "early_blight": {"name": "Tomato Early Blight",
  "about": "Caused by the fungus Alternaria solani. Brown spots with ring patterns and a yellow halo start on the oldest leaves.",
  "treatment": ["Remove infected lower leaves and bag them.",
                "Apply a protectant fungicide (for example chlorothalonil, mancozeb or copper) per label, every 7-10 days in wet weather.",
                "Mulch the soil to stop spores splashing up onto leaves."],
  "prevention": ["Rotate crops for 2-3 years.", "Stake and prune plants for good airflow.",
                 "Water at the base, in the morning.", "Keep plants well fed so they stay vigorous."]},
 "late_blight": {"name": "Tomato Late Blight",
  "about": "Caused by Phytophthora infestans. Large, greasy dark patches appear on leaves and stems, with white fuzzy growth underneath in humid weather. It spreads very fast in cool, wet conditions.",
  "treatment": ["Act immediately: remove and destroy infected plants (do not compost).",
                "Apply a fungicide labelled for late blight (e.g. mancozeb, chlorothalonil, or cymoxanil/metalaxyl-type products) as the label directs.",
                "Warn neighbouring growers, as spores travel on the wind."],
  "prevention": ["Plant resistant varieties where available.", "Avoid overhead irrigation and leaf wetness at night.",
                 "Space plants widely for airflow.", "Destroy volunteer tomato/potato plants and cull piles."]},
 "leaf_mold": {"name": "Tomato Leaf Mold",
  "about": "Caused by the fungus Passalora fulva. Pale yellow spots form on the upper leaf surface with olive-grey velvety mold underneath; common in high humidity.",
  "treatment": ["Improve ventilation and lower humidity around plants.", "Remove infected leaves.",
                "Apply a fungicide such as chlorothalonil or copper per label if spreading."],
  "prevention": ["Choose resistant varieties.", "Space and prune plants for airflow.",
                 "Water in the morning and keep leaves dry.", "Ventilate greenhouses well."]},
 "septoria_leaf_spot": {"name": "Tomato Septoria Leaf Spot",
  "about": "Caused by Septoria lycopersici. Many small round spots with dark borders and grey centres (tiny black dots inside) appear, starting on lower leaves.",
  "treatment": ["Remove infected lower leaves.",
                "Apply chlorothalonil, mancozeb or copper per label every 7-10 days during wet weather.",
                "Mulch to reduce soil splash."],
  "prevention": ["Rotate crops for at least 3 years.", "Remove plant debris and nightshade weeds.",
                 "Avoid overhead watering.", "Stake plants to keep foliage off the ground."]},
 "spider_mites": {"name": "Tomato Spider Mites (Two-spotted)",
  "about": "Tiny mites feed on the underside of leaves, causing yellow stippling, bronzing and fine webbing. They thrive in hot, dry, dusty conditions.",
  "treatment": ["Spray the undersides of leaves with a strong jet of water to knock mites off.",
                "Use insecticidal soap or neem oil, repeating every 5-7 days.",
                "For severe cases use a miticide only as the label directs, or release predatory mites."],
  "prevention": ["Keep plants well watered and reduce dust.", "Avoid broad-spectrum insecticides that kill natural predators.",
                 "Check leaf undersides weekly.", "Remove weedy hosts nearby."]},
 "target_spot": {"name": "Tomato Target Spot",
  "about": "Caused by Corynespora cassiicola. Brown spots with ring patterns appear on leaves and can spread to stems and fruit; looks similar to early blight.",
  "treatment": ["Remove infected leaves and destroy them.",
                "Apply a labelled fungicide (e.g. chlorothalonil or mancozeb) per directions.",
                "Improve airflow by pruning lower foliage."],
  "prevention": ["Rotate crops.", "Avoid overhead watering.", "Remove crop debris after harvest.", "Avoid overcrowding plants."]},
 "yellow_leaf_curl_virus": {"name": "Tomato Yellow Leaf Curl Virus",
  "about": "A virus spread by whiteflies. Leaves curl upward and turn yellow at the edges, plants are stunted and flowers drop. There is no cure.",
  "treatment": ["Remove and destroy infected plants early (bag them first so whiteflies do not escape).",
                "Control whiteflies with yellow sticky traps, neem oil or insecticidal soap; use insecticides only as locally recommended.",
                "Remove weeds that host whiteflies."],
  "prevention": ["Plant resistant or tolerant varieties.", "Raise seedlings under insect-proof net.",
                 "Use reflective mulch.", "Inspect transplants before planting."]},
 "mosaic_virus": {"name": "Tomato Mosaic Virus",
  "about": "A virus causing light and dark green mottling and distorted, fern-like leaves. It spreads by contact, tools, hands and infected seed. There is no cure.",
  "treatment": ["Remove and destroy infected plants.",
                "Wash hands with soap and disinfect tools (for example a 10% bleach solution) between plants.",
                "Do not handle tobacco before touching plants."],
  "prevention": ["Use resistant varieties and certified seed.", "Rotate crops and clear all plant debris.",
                 "Control weeds that carry the virus.", "Keep working areas clean."]},
 "healthy": {"name": "Healthy Tomato Leaf",
  "about": "No disease pattern was detected on this leaf.",
  "treatment": ["No treatment needed. Keep monitoring your plants."],
  "prevention": ["Water at the base of plants, not on leaves.", "Feed with balanced fertilizer.",
                 "Check leaf undersides and new growth weekly.", "Remove any yellowing leaves promptly."]},
}

def _e(name, about, treatment, prevention):
    return {"name": name, "about": about, "treatment": treatment, "prevention": prevention}


_OK = ["No treatment needed. Keep monitoring."]
_CHECK = ["Water at the base, avoid wounding the plant, and check it weekly."]
REMEDIES.update({
 # ---------------- FRUIT ----------------
 "fruit_healthy": _e("Healthy Tomato Fruit", "No disease pattern was detected on this fruit.", _OK, _CHECK),
 "fruit_blossom_end_rot": _e("Fruit Blossom End Rot",
  "A non-infectious disorder linked to calcium uptake problems, usually from uneven watering. A sunken, dark, leathery patch forms at the blossom end.",
  ["Remove affected fruit so the plant puts energy into healthy ones.", "Water deeply and evenly; never let the soil dry out then flood.", "Mulch to hold moisture and avoid heavy nitrogen feeding."],
  ["Keep soil pH around 6.2-6.8.", "Use steady irrigation, preferably drip.", "Avoid damaging roots when weeding."]),
 "fruit_anthracnose": _e("Fruit Anthracnose",
  "A fungal disease (Colletotrichum) causing sunken, round, water-soaked spots on ripe fruit that darken and may show rings.",
  ["Remove and destroy infected fruit.", "Apply a labelled fungicide such as chlorothalonil, mancozeb or copper.", "Harvest fruit promptly when ripe."],
  ["Rotate crops for 2-3 years.", "Avoid overhead watering.", "Stake plants so fruit stays off the soil.", "Remove crop debris."]),
 "fruit_late_blight": _e("Fruit Late Blight",
  "Caused by Phytophthora infestans. Large, firm, greasy brown patches appear on fruit and the disease spreads quickly in cool, wet weather.",
  ["Remove and destroy infected fruit and plants (do not compost).", "Apply a fungicide labelled for late blight as the label directs.", "Warn neighbouring growers."],
  ["Plant resistant varieties.", "Avoid overhead irrigation.", "Space plants for airflow.", "Destroy volunteer tomato and potato plants."]),
 "fruit_early_blight": _e("Fruit Early Blight",
  "Caused by Alternaria. Dark, leathery, sunken lesions with ring patterns form near the stem end of the fruit.",
  ["Remove infected fruit and lower leaves.", "Apply a protectant fungicide (chlorothalonil, mancozeb or copper) per label."],
  ["Rotate crops.", "Mulch and stake plants.", "Water at the base.", "Keep plants well nourished."]),
 "fruit_cracking": _e("Fruit Cracking",
  "A physiological disorder where fruit splits, often after heavy rain or watering following a dry spell. Cracks let rot organisms in.",
  ["Harvest cracked fruit soon and use it quickly.", "Keep watering even and mulch the soil."],
  ["Grow crack-resistant varieties.", "Keep potassium and calcium balanced.", "Shade plants in extreme heat.", "Harvest on time."]),
 "fruit_mold": _e("Fruit Mold",
  "Grey or white fuzzy mold (for example Botrytis) on the fruit, favoured by humid, poorly ventilated conditions and wounds.",
  ["Remove and destroy moldy fruit.", "Improve ventilation and reduce humidity.", "Apply a labelled fungicide if it keeps spreading."],
  ["Prune for airflow.", "Avoid wounding fruit.", "Harvest ripe fruit promptly.", "Keep leaves and fruit dry."]),
 "fruit_worm_damage": _e("Fruit Worm Damage",
  "Caterpillars such as Helicoverpa bore holes into fruit, leaving droppings and rot behind.",
  ["Hand-pick caterpillars and remove damaged fruit.", "Spray Bacillus thuringiensis (Bt) or another product recommended locally.", "Use pheromone traps to time treatments."],
  ["Monitor plants weekly.", "Remove crop residues.", "Use insect nets where practical."]),
 "fruit_abiotic_disorder": _e("Fruit Abiotic (Non-infectious) Disorder",
  "Damage caused by environment rather than germs, such as sunscald, catfacing, or nutrient and water stress.",
  ["Remove badly damaged fruit.", "Provide shade cloth in extreme heat.", "Keep watering and feeding steady."],
  ["Keep enough leaf cover to shade fruit.", "Avoid sudden temperature or watering swings.", "Feed with a balanced fertilizer."]),
 "fruit_infected": _e("Infected Tomato Fruit",
  "The fruit shows disease symptoms, but the exact disease could not be told apart by this model.",
  ["Remove and bag infected fruit.", "Do not harvest from visibly rotting parts of the plant.", "Show a sample to your local agriculture officer for exact identification."],
  ["Keep fruit off the ground.", "Water at the base.", "Space and prune plants for airflow.", "Clear crop debris."]),
 # ---------------- STEM ----------------
 "stem_healthy": _e("Healthy Tomato Stem", "No disease pattern was detected on this stem.", _OK, _CHECK),
 "stem_bacterial_canker": _e("Stem Bacterial Canker",
  "Caused by Clavibacter michiganensis. Brown streaks and cankers on stems, wilting of leaf edges and plant decline.",
  ["Remove and destroy infected plants; do not compost.", "Disinfect tools and hands between plants.", "Copper sprays only slow spread; they do not cure it."],
  ["Use certified disease-free seed.", "Rotate crops for 3 years.", "Avoid wounding plants and overhead watering."]),
 "stem_bacterial_wilt": _e("Stem Bacterial Wilt",
  "Caused by Ralstonia solanacearum. Sudden wilting while leaves stay green, with brown vascular tissue inside the stem. There is no cure.",
  ["Remove and destroy infected plants including roots.", "Do not move soil or water from affected areas.", "Disinfect tools and boots."],
  ["Use resistant varieties or grafted plants.", "Rotate with non-host crops.", "Improve soil drainage and use clean irrigation water."]),
 "stem_gray_mold": _e("Stem Gray Mold",
  "Botrytis cinerea creates grey fuzzy mold and grey-brown lesions on stems, often at pruning wounds in humid weather.",
  ["Remove infected plant parts and destroy them.", "Improve ventilation and reduce humidity.", "Apply a labelled fungicide if needed."],
  ["Prune in dry weather with clean cuts.", "Space plants well.", "Remove dead leaves and flowers promptly."]),
 "stem_early_blight": _e("Stem Early Blight (Collar Rot)",
  "Alternaria causes dark, sunken lesions with ring patterns on stems, especially near the soil line.",
  ["Remove severely affected plants.", "Apply a protectant fungicide per label.", "Mulch to keep soil from splashing onto stems."],
  ["Rotate crops.", "Stake plants.", "Water at the base."]),
 # ---------------- FLOWER ----------------
 "flower_healthy": _e("Healthy Tomato Flower", "No disease pattern was detected on this flower.", _OK, _CHECK),
 "flower_gray_mold": _e("Flower Gray Mold",
  "Botrytis cinerea causes brown, rotting flowers covered in grey fuzzy mold, which can spread to fruit.",
  ["Remove infected flowers and destroy them.", "Improve airflow and lower humidity.", "Apply a labelled fungicide if it persists."],
  ["Remove spent flowers promptly.", "Avoid overhead watering.", "Space plants well."]),
 "flower_blossom_drop": _e("Flower Blossom Drop",
  "Flowers fall off without setting fruit, usually from heat above about 32 °C, cold nights, water stress or too much nitrogen. It is not an infection.",
  ["Provide shade in heat and keep watering even.", "Reduce nitrogen feeding.", "Gently shake flower clusters to help pollination."],
  ["Plant heat-tolerant varieties.", "Maintain steady moisture.", "Avoid extreme temperature swings."]),
 # ---------------- ROOT ----------------
 "root_healthy": _e("Healthy Tomato Roots", "No disease pattern was detected on these roots.", _OK, ["Keep soil well drained and rotate crops."]),
 "root_knot_nematode": _e("Root-knot Nematode",
  "Microscopic worms cause swollen galls on roots, leading to stunting, wilting and yellowing even with enough water.",
  ["Remove and destroy infected plants with their roots.", "Solarize the soil in hot weather.", "Ask your agriculture officer about approved nematicides."],
  ["Grow resistant varieties or grafted plants.", "Rotate with marigold or cereals.", "Add organic matter and use clean transplants."]),
 "root_rot": _e("Root Rot",
  "Soil fungi such as Pythium or Fusarium rot the roots, causing wilting, yellowing and brown mushy roots, often in waterlogged soil.",
  ["Reduce watering and improve drainage.", "Remove badly affected plants.", "Consider a Trichoderma bio-fungicide, or a labelled fungicide drench."],
  ["Use raised beds and well-drained soil.", "Use clean seedling media.", "Rotate crops and avoid overwatering."]),
})


def get_info(key):
    """Remedy entry for any disease key; unknown keys get a safe generic entry."""
    return REMEDIES.get(key) or _e(
        key.replace("_", " ").title(), "Specific advice for this condition is not available yet.",
        ["Remove the affected part if practical.", "Ask your local agriculture officer to confirm the problem."],
        ["Water at the base.", "Keep plants spaced and tools clean.", "Scout plants weekly."])


FUNGAL_BACTERIAL = {"bacterial_spot", "early_blight", "late_blight", "leaf_mold", "septoria_leaf_spot", "target_spot",
    "fruit_anthracnose", "fruit_late_blight", "fruit_early_blight", "fruit_mold", "stem_bacterial_canker",
    "stem_gray_mold", "stem_early_blight", "flower_gray_mold", "root_rot"}
VIRAL = {"yellow_leaf_curl_virus", "mosaic_virus"}


def build_remedies(key, a):
    """Combine the base remedy with advice based on the 'Additional Information' answers `a`."""
    base = get_info(key)
    healthy = key == "healthy" or key.endswith("_healthy")
    notes = []
    if a.get("weather") in ("rainy", "humid") and key in FUNGAL_BACTERIAL:
        notes.append("Wet or humid weather helps this disease spread. Avoid overhead watering, improve airflow, and apply protectants before forecast rain.")
    if key == "late_blight" and a.get("temperature") == "cool" and a.get("weather") in ("rainy", "humid"):
        notes.append("Cool, wet weather is ideal for late blight. Treat quickly and check plants daily.")
    if key == "spider_mites" and (a.get("temperature") == "hot" or a.get("weather") == "dry"):
        notes.append("Hot, dry conditions favour mites. Increase watering and mist the undersides of leaves.")
    if a.get("fertilizer") == "yes" and not healthy and key not in VIRAL:
        notes.append("Avoid extra nitrogen fertilizer until plants recover; soft, lush growth is more prone to disease.")
    if a.get("pesticide") == "yes" and not healthy:
        notes.append("Because you have already used a pesticide, switch to a product with a different active ingredient next time to avoid resistance, and respect the waiting period before harvest.")
    if a.get("insects") == "yes":
        if key in VIRAL or key == "spider_mites":
            notes.append("Insect pests are linked to this problem. Controlling whiteflies, aphids and mites is a key part of treatment.")
        else:
            notes.append("Identify the insects you saw; they can spread disease and make wounds that let infection in.")
    if a.get("pest_damage") == "yes" and key not in VIRAL and key != "spider_mites":
        notes.append("Pest damage may be separate from this disease. This tool only checks for leaf disease, so inspect plants for pests too.")
    if a.get("wilting") == "yes":
        notes.append("Wilting can also come from dry or waterlogged soil, root problems or wilt diseases that this tool does not detect. Check soil moisture and the stem base.")
    if a.get("discoloration") == "yes" and healthy:
        notes.append("You reported discoloration, but the leaf looks healthy to the model. It may be a nutrient deficiency or water stress; check other leaves too.")
    if a.get("discoloration") == "no" and not healthy:
        notes.append("You reported no discoloration, yet a disease pattern was detected. Look closely at other leaves or upload a clearer photo.")
    return {**base, "notes": notes}
