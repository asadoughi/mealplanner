from sr26abbr import load

db = load.load()


def print_meal():
    meal_plan = [
        ("01132", 0.5),
        ("01124", 0.46),
        ("14016", 4.8),
        ("09040", 1.36),
        ("18076", 0.85),
        ("12061", 0.57),
        ("11457", 0.57),
        ("05063", 1.13),
        ("11529", 1.00),
        ("09037", 0.68),
        ("20037", 2.50),
        ("11124", 1.28),
        ("16158", 0.28),
        ("09202", 1.54),
        ("15086", 1.42),
        ("11090", 0.91),
        ("01256", 2.25)]

    total = dict()
    for meal, weight in meal_plan:
        i = db[meal]
        for field_name, field_type in load.FIELDS:
            if field_type is str:
                continue
            if not i[field_name]:
                continue

            w = i[field_name] * weight
            if field_name not in total:
                total[field_name] = w
            else:
                total[field_name] += w

    total.pop("GmWt_1")
    total.pop("GmWt_2")
    for key in total:
        print key, total[key]


def print_meal_key(meal_plan, key):
    total = 0
    for num, weight in meal_plan:
        item = db[num]
        print item[key], item["Shrt_Desc"]
        total += item[key] * weight if item[key] else 0
    print total


def print_high_vitC_low_carb():
    l = []
    for num in db:
        if db[num]["Vit_C"] and db[num]["Vit_C"] > 10:
            l.append(
                (db[num]["Shrt_Desc"],
                 db[num]["Vit_C"],
                 db[num]["Carbohydrt"]))
    m = sorted(l, key=lambda e: e[2] / e[1] if e[2] else float('inf'))
    for e in m[:100]:
        print "%s:%s:%s" % e

print_meal()
