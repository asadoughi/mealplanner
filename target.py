"""Source: http://fnic.nal.usda.gov/fnic/interactiveDRI/"""
from db import GRAMS

G = GRAMS
MG = 1e-3 * GRAMS
MCG = 1e-6 * GRAMS

# Macronutrients were modified
target_macronutrients = dict(
    carbohydrates=281 * G,
    fiber=38 * G,
    protein=155 * G,
    fat=56 * G,
)

target_vitamins = dict(
    vitamin_A=900 * MCG,
    vitamin_C=90 * MG,
    vitamin_D=15 * MCG,
    vitamin_E=15 * MG,
    thiamin=1.2 * MG,
    riboflavin=1.3 * MG,
    niacin=16 * MG,
    vitamin_b6=1.3 * MG,
    folate=400 * MCG,
    vitamin_b12=2.4 * MCG,
    pantothenic_acid=5 * MG,
    biotin=30 * MCG,
    choline=550 * MG,
)

target_minerals = dict(
    calcium=1000 * MG,
    chloride=2.3 * G,
    chromium=35 * MCG,
    copper=900 * MCG,
    fluoride=4 * MG,
    iodine=150 * MCG,
    iron=8 * MG,
    magnesium=400 * MG,
    manganese=2.3 * MG,
    molybdenum=45 * MCG,
    phosphorus=700 * MG,
    potassium=4.7 * G,
    selenium=55 * MCG,
    sodium=1.5 * G,
    zinc=11 * MG
)

targets = dict(
    macronutrients=target_macronutrients,
    vitamins=target_vitamins,
    minerals=target_minerals,
)
