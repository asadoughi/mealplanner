class Measurement(object):
    GRAM, OUNCE, FLUID_OUNCE = range(3)

    def __init__(self, size, units):
        self.size = size
        self.units = units

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Measurement(other * self.size, self.units)
        raise TypeError("Cannot multiply Measurement by %s" % type(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        str_unit = "GRAM"
        if self.units == self.OUNCE:
            str_unit = "OUNCE"
        elif self.units == self.FLUID_OUNCE:
            str_unit = "FLUID_OUNCE"
        return "Measurement(%s, %s)" % (self.size, str_unit)


class Serving(object):
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Serving(self.size * other if self.size else None,
                           self.weight * other if self.weight else None)
        raise TypeError("Cannot multiply Serving by %s" % type(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return "Serving(%s, %s)" % (self.size, self.weight)


class Food(object):
    """Food measured in grams of fats, carbs, protein."""
    def __init__(self, serving, fat, carb, protein):
        self.serving = serving
        self.fat = fat
        self.carb = carb
        self.protein = protein

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Food(self.serving * other,
                        self.fat * other,
                        self.carb * other,
                        self.protein * other)
        raise TypeError("Cannot multiply Food by %s" % type(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return "Food(%s, %s, %s, %s)" % (
            self.serving, self.fat, self.carb, self.protein)


# Common measurements
CUP = Measurement(8, Measurement.FLUID_OUNCE)
TBSP = Measurement(0.5, Measurement.FLUID_OUNCE)
GRAMS = Measurement(1, Measurement.GRAM)
OUNCES = Measurement(1, Measurement.OUNCE)


class Beverages(object):
    Water = Food(Serving(CUP, 237 * GRAMS), 0, 0, 0)
    AlmondMilk = Food(Serving(CUP, None), 2.5, 8, 1)


class ProteinSources(object):
    Egg = Food(Serving(None, 50 * GRAMS), 4.5, 1, 6)
    EggWhite = Food(Serving(3 * TBSP, 46 * GRAMS), 0, 0, 6)
    ChickenBreast = Food(Serving(None, 4 * OUNCES), 1.5, 0, 27)
    WildSalmonSockeye = Food(Serving(None, 3 * OUNCES), 8, 0, 25)
    GreekYogurt = Food(Serving(CUP, 225 * GRAMS), 0, 16, 23)


class Nuts(object):
    # TODO: at Whole Foods: almonds
    # 12061 - 1 oz = approximately 23 whole almonds
    Almond = Food(Serving(None, 1 * OUNCES), 14, 6, 6)


class Carbs(object):
    # 20037 - 1 cup - 195 g
    BrownRice = Food(Serving(CUP, 180 * GRAMS), 6, 132, 16)
    WholeWheatBreadSlice = Food(Serving(None, 1.5 * OUNCES), 4, 19, 3)


class Beans(object):
    Hummus = Food(Serving(2 * TBSP, 28 * GRAMS), 6, 6, 3)


class Fruits(object):
    # 09040 - 1 large - 8" to 8 7/8"
    Banana = Food(Serving(None, 136 * GRAMS), 0, 31, 1)
    # 09202 - 1 fruit
    NavelOrange = Food(Serving(None, 140 * GRAMS), 0, 21, 1)


class Vegetables(object):
    # 11090
    Broccoli = Food(Serving(CUP, 91 * GRAMS), 0, 6, 3)
    # 11124
    Carrot = Food(Serving(CUP, 128 * GRAMS), 0, 12, 1)
    Spinach = Food(Serving(2 * CUP, 3 * OUNCES), 0, 3, 2)
    # 11529 - 1 tomato
    RomaTomato = Food(Serving(None, 100 * GRAMS), 0, 4, 1)
    # 09037 - Avocados, raw, all commercial varieties - ours are from MX
    Avocado = Food(Serving(CUP, 150 * GRAMS), 22, 13, 3)
