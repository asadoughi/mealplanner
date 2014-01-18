import db

meal_plan = [
    db.ProteinSources.Egg,
    db.ProteinSources.EggWhite,
    db.Beverages.AlmondMilk,
    db.Fruits.Banana,
    2 * db.Carbs.WholeWheatBreadSlice,
    2 * db.Nuts.Almond,
    2/3. * db.Vegetables.Spinach,
    4/3. * db.ProteinSources.ChickenBreast,
    db.Vegetables.RomaTomato,
    0.45 * db.Vegetables.Avocado,
    db.Carbs.BrownRice,
    db.Vegetables.Carrot,
    db.Beans.Hummus,
    db.Fruits.NavelOrange,
    db.Beverages.AlmondMilk,
    5/3. * db.ProteinSources.WildSalmonSockeye,
    db.Vegetables.Broccoli,
    db.Carbs.BrownRice,
    db.ProteinSources.GreekYogurt,
]

sum_fat, sum_carbs, sum_protein = 0, 0, 0
for item in meal_plan:
    sum_fat += item.fat
    sum_carbs += item.carb
    sum_protein += item.protein

print round(sum_fat, 2), 'g fat', round(sum_carbs, 2), 'g carbs',
print round(sum_protein, 2), 'g protein'

print round(sum_fat * 9, 2), 'fat',
print round(sum_carbs * 4, 2), 'carbs',
print round(sum_protein * 4, 2), 'proteins'

total_calories = sum_fat * 9 + sum_carbs * 4 + sum_protein * 4
print 'Total calories:', round(total_calories, 2)

print 'Fat %:', round((sum_fat * 9) / total_calories, 3) * 100
print 'Carb %:', round((sum_carbs * 4) / total_calories, 3) * 100
print 'Protein %:', round((sum_protein * 4) / total_calories, 3) * 100
