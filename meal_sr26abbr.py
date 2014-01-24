from sr26abbr.load import load

meal_plan = [
    ("01132", 0.5),
    ("01124", 0.46),
    ("14016", 4.8),
    ("09040", 1.36),
    ("18076", 0.85),
    ("12061", 0.57),
    ("11457", 0.57),
    ("05747", 1.13),
    ("11529", 1.00),
    ("09037", 0.68),
    ("20037", 2.50),
    ("11124", 1.28),
    ("16158", 0.28),
    ("09202", 1.54),
    ("15273", 1.42),
    ("11740", 0.91),
    ("01256", 2.25),
]


db = load()
total_calories = 0
total_protein = 0
total_fat = 0
total_carbs = 0
for meal, weight in meal_plan:
    i = db[meal]
    kcal = i["Energ_Kcal"] * weight
    protein = i["Protein"] * weight
    fat = i["Lipid_Tot"] * weight
    carbs = i["Carbohydrt"] * weight
    print "%s:%s:%s:%s:%s" % (i["Shrt_Desc"], kcal, protein, fat, carbs)
    total_calories += kcal
    total_protein += protein
    total_fat += fat
    total_carbs += carbs

print total_calories, total_protein, total_fat, total_carbs
verify_total = total_protein * 4 + total_fat * 9 + total_carbs * 4
print "Verify total kcal", verify_total
print "Protein %.1f" % (total_protein * 4 / verify_total * 100.)
print "Fat %.1f" % (total_fat * 4 / verify_total * 100.)
print "Carbs %.1f" % (total_carbs * 4 / verify_total * 100.)
