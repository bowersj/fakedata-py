import os

SOURCE_DIR        = r"D:\fakeData\_fakeData\names\data"

FAMOUS_FIRST_NAME = {
    "name": "famous first names",
    "path": os.path.join( SOURCE_DIR, r"famousFirstNames.json" ),
    "data_prop": "name",
    "perc_prop": None
}

FAMOUS_LAST_NAME = {
    "name": "famous last names",
    "path": os.path.join( SOURCE_DIR, r"famousLastNames.json" ),
    "data_prop": "name",
    "perc_prop": None
}

FAMOUS_PEOPLE = {
    "name": "famous people",
    "path": os.path.join( SOURCE_DIR, r"FamousPeople.csv" ),
    "data_prop": "name",
    "perc_prop": None
}

MALE_FIRST_NAME = {
    "name": "male first names",
    "path": os.path.join( SOURCE_DIR, r"maleFirstNames.json" ),
    "data_prop": "name",
    "perc_prop": None
}

FEMALE_FIRST_NAME = {
    "name": "female first names",
    "path": os.path.join( SOURCE_DIR, r"femaleFirstNames.json" ),
    "data_prop": "name",
    "perc_prop": "probability"
}

LAST_NAME = {
    "name": "last names",
    "path": os.path.join( SOURCE_DIR, r"surnames.json" ),
    "data_prop": "name",
    "perc_prop": "probability"
}