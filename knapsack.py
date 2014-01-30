from sr26abbr import load

db = load.load()


target = dict(
    Fiber_TD=38,
    Vit_A_RAE=900,
    Vit_C=90,
    Vit_D_mcg=15,
    Vit_E=15,
    Vit_K=120,
    Thiamin=1.2,
    Riboflavin=1.3,
    Niacin=16,
    Vit_B6=1.3,
    Folate_Tot=400,
    Vit_B12=2.4,
    Panto_acid=5,
    # Biotin=30 mcg,
    Choline_Tot=550,
    Calcium=1000,
    Iron=8,
    Magnesium=400,
    Manganese=2.3,
    # Molybdenum = 45 mcg
    Phosphorus=700,
    Potassium=4700,
    Selenium=55,
    Sodium=1500,
    Zinc=11,
    )

db_nuts = {tkey: {} for tkey in target.keys()}
for key in db.keys():
    for tkey in target.keys():
        db_nuts[tkey][key] = db[key][tkey] if db[key][tkey] else 0

sorted_nuts = dict()
for tkey in target.keys():
    sorted_nuts[tkey] = sorted(
        db_nuts[tkey].iteritems(), reverse=True, key=lambda x: x[1])

meal = []
for tkey in target.keys():
    k, v = sorted_nuts[tkey][0]
    weight = target[tkey] / v
    meal.append((k, weight))

calories = 0
for item, weight in meal:
    print item, "%.2f" % (weight * 100), db[item]["Shrt_Desc"],
    print db[item]["Energ_Kcal"] * weight
    calories += db[item]["Energ_Kcal"] * weight
print "calories:", calories
