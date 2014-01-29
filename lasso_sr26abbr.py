from sklearn import linear_model
import random

from sr26abbr import load


db = load.load()

target_calories = 2400
target_protein = 155
target_vitamin_a = 900
target_vitamin_c = 90
target_vitamin_d = 15
target_vitamin_e = 15
target_vitamin_b12 = 2.4
target_vitamin_b6 = 1.3
target_thiamin = 1.2
target_sodium = 1500

# inequality constraints
# constrain # of weights that are non-zero (don't want to eat more than 20
# different things in a day)
# constrain domain of weight (0 < w < 500 g)

def run_fit(keys):
    x = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    y = [target_calories, target_protein, target_vitamin_c, target_vitamin_a,
         target_vitamin_e, target_vitamin_b12, target_vitamin_b6,
         target_vitamin_d, target_thiamin, target_sodium]
    for num in keys:
        item = db[num]
        x[0].append(item["Energ_Kcal"])
        x[1].append(item["Protein"])
        x[2].append(item["Vit_C"] if item["Vit_C"] else 0)
        x[3].append(item["Vit_A_RAE"] if item["Vit_A_RAE"] else 0)
        x[4].append(item["Vit_E"] if item["Vit_E"] else 0)
        x[5].append(item["Vit_B12"] if item["Vit_B12"] else 0)
        x[6].append(item["Vit_B6"] if item["Vit_B6"] else 0)
        x[7].append(item["Vit_D_mcg"] if item["Vit_D_mcg"] else 0)
        x[8].append(item["Thiamin"] if item["Thiamin"] else 0)
        x[9].append(item["Sodium"] if item["Sodium"] else 0)
    clf = linear_model.Lasso(alpha = 0.1, fit_intercept=False, positive=True)
    clf.fit(x, y)
    return clf

keys = db.keys()
random.shuffle(keys)
clf = run_fit(keys)
print len(clf.coef_)
for i, e in enumerate(clf.coef_):
    if e >= 0.01:
        print i, e, db[keys[i-1]]["Shrt_Desc"]
