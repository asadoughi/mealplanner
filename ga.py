from scipy.stats import scoreatpercentile
import random

from sr26abbr import load


db = load.load()
keys = db.keys()
MAX_WEIGHT = 5

target_protein = 155.0
target_calories = 2400.0


def nchoosek(n, k):
    r = [0 for i in range(n)]
    while k > 0:
        i = int(random.uniform(0, n-1))
        if r[i]:
            continue
        r[i] = 1
        k -= 1
    return r


def population(m, k):
    return [nchoosek(len(keys) * 3, k) for i in range(m)]


def fitness(x):
    total_calories = 0
    for i in range(len(keys)):
        a, b, c = x[3*i], x[3*i+1], x[3*i+2]
        if not a and not b and not c:
            continue
        weight = max((a * 1 + b * 2 + c * 4), MAX_WEIGHT)
        total_calories += db[keys[i]]["Energ_Kcal"] * weight
    return abs(total_calories - target_calories)/target_calories


def has_reached_target(fitness_p):
    print min(fitness_p)
    return min(fitness_p) <= 0.05


def select(p, fitness_p):
    threshold = scoreatpercentile(fitness_p, 98)
    ret = [p[i] for i in range(len(p)) if fitness_p[i] < threshold]
    print "threshold", threshold, "min", min(fitness_p),
    print "fit_p", len(ret)
    return ret


def new_population(fit_p):
    # crossover, inheritance
    new_p = []
    l = len(fit_p)
    i = 0
    while i + 1 < l:
        parent1, parent2 = fit_p[i], fit_p[i+1]
        point = int(random.uniform(0, len(parent1)))
        new_p.append(parent1[:point] + parent2[point:])
        new_p.append(parent2[:point] + parent1[point:])
        i += 2
    # mutation
    for i in range(len(new_p)):
        k = int(random.uniform(0, len(new_p[i])))
        l = int(random.uniform(0, len(new_p[i])))
        if new_p[i][k] != new_p[i][l]:
            new_p[i][k], new_p[i][l] = new_p[i][l], new_p[i][k]
    return new_p

p = population(1000, 22)
fitness_p = [fitness(x) for x in p]
while not has_reached_target(fitness_p):
    fit_p = select(p, fitness_p)
    p = new_population(fit_p)
    fitness_p = [fitness(x) for x in p]
