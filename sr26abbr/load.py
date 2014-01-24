"""
The ASCII file (Table 16) is in delimited format. Fields are separated by a caret (^) and text fields are surrounded by tildes (~). Data refer to 100 g of the edible portion of the food item. Decimal points are included in the fields. Missing values are denoted by the null value of two consecutive carets (^^) or two carets and two tildes (~~). The file is sorted in ascending order by the NDB number. Two common measures are provided, which are the first two common measures in the Weight file for each NDB number.
"""

FILENAME = "sr26abbr/ABBREV.txt"
FIELDS = (
    ("Shrt_Desc", str),
    ("Water", 10.2),
    ("Energ_Kcal", 10),
    ("Protein", 10.2),
    ("Lipid_Tot", 10.2),
    ("Ash", 10.2),
    ("Carbohydrt", 10.2),
    ("Fiber_TD", 10.1),
    ("Sugar_Tot", 10.2),
    ("Calcium", 10),
    ("Iron", 10.2),
    ("Magnesium", 10),
    ("Phosporus", 10),
    ("Potassium", 10),
    ("Sodium", 10),
    ("Zinc", 10.2),
    ("Copper", 10.3),
    ("Manganese", 10.3),
    ("Selenium", 10.1),
    ("Vit_C", 10.1),
    ("Thiamin", 10.3),
    ("Riboflavin", 10.3),
    ("Niacin", 10.3),
    ("Panto_acid", 10.3),
    ("Vit_B6", 10.3),
    ("Folate_Tot", 10),
    ("Folic_acid", 10),
    ("Food_Folate", 10),
    ("Folate_DFE", 10),
    ("Choline_Tot", 10),
    ("Vit_B12", 10.2),
    ("Vit_A_IU", 10),
    ("Vit_A_RAE", 10),
    ("Retinol", 10),
    ("Alpha_Carot", 10),
    ("Beta_Carot", 10),
    ("Beta_Crypt", 10),
    ("Lycopene", 10),
    ("Lut+Zea", 10),
    ("Vit_E", 10.2),
    ("Vit_D_mcg", 10.1),
    ("Vit_D_IU", 10),
    ("Vit_K", 10.1),
    ("FA_Sat", 10.3),
    ("FA_Mono", 10.3),
    ("FA_Poly", 10.3),
    ("Cholestrl", 10.3),
    ("GmWt_1", 9.2),
    ("GmWt_Desc1", str),
    ("GmWt_2", 9.2),
    ("GmWt_Desc2", str),
    ("Refuse_Pct", 2)
)

def parse_string(field):
    return field.lstrip("~").rstrip("~")


def parse_number(field):
    return float(field)


def parse_ndb_no(line):
    return parse_string(line[0])


def parse_fields(line):
    record = dict()
    for field, line_field in zip(FIELDS, line[1:]):
        key = field[0]
        if not line_field:
            record[key] = None
        elif field[1] == str:
            record[key] = parse_string(line_field)
        else:
            record[key] = parse_number(line_field)
    return record


def load():
    f = open(FILENAME)
    db = dict()
    for line in f.readlines():
        line = line.strip().split("^")
        ndb_no = parse_ndb_no(line)
        db[ndb_no] = parse_fields(line)
    return db
