from sr26abbr import load


db = load.load()


orig_target = dict(
    Fiber_TD=38,
    Protein=155,
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


def get_db_nuts(target_keys):
    db_nuts = {tkey: {} for tkey in target_keys}
    for key in db.keys():
        cal = db[key]["Energ_Kcal"]
        for tkey in target_keys:
            db_nuts[tkey][key] = (db[key][tkey] / cal
                                  if db[key][tkey] and cal else 0)
    return db_nuts


def get_sorted_nuts(db_nuts, target_keys):
    sorted_nuts = dict()
    for tkey in target_keys:
        sorted_nuts[tkey] = sorted(
            db_nuts[tkey].iteritems(), reverse=True, key=lambda x: x[1])
    return sorted_nuts


def get_meal(sorted_nuts, target_keys):
    meal = []
    for tkey in target_keys:
        k, v = sorted_nuts[tkey][0]
        weight = target[tkey] / (v * db[k]["Energ_Kcal"])
        meal.append((k, weight))

        for key in target_keys:
            if key == tkey:
                target[key] = 0
            elif db[k][key]:
                target[key] = (0 if db[k][key] * weight > target[key]
                               else target[key] - db[k][key] * weight)
    return meal

target_keys = orig_target.keys()
while True:
    target = orig_target.copy()
    db_nuts = get_db_nuts(target_keys)
    sorted_nuts = get_sorted_nuts(db_nuts, target_keys)
    meal = get_meal(sorted_nuts, target_keys)

    sums = dict(Sugar_Tot=0, FA_Sat=0, Cholestrl=0, Energ_Kcal=0)
    for item, weight in meal:
        if weight:
            print item, "%.2f" % (weight * 100), db[item]["Shrt_Desc"]
        for sum_key in sums.keys():
            if db[item][sum_key]:
                sums[sum_key] += db[item][sum_key] * weight
    print sums

    keycode = raw_input("Item code to remove: ")
    print "Removing [%s]" % keycode
    if len(keycode) < 5:
        for key in db.keys():
            if key.startswith(keycode):
                db.pop(key)
    else:
        db.pop(keycode)

    # rotate thru first to optimize
    target_keys.append(target_keys.pop(0))
