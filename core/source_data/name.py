import os
import json



SOURCE_DIR        = r"D:\fakeData\_fakeData\names\data"

FAMOUS_FIRST_NAME = os.path.join( SOURCE_DIR, r"famousFirstNames.json" )
FAMOUS_FIRST_LAST = os.path.join( SOURCE_DIR, r"famousLastNames.json" )
FAMOUS_PEOPLE     = os.path.join( SOURCE_DIR, r"FamousPeople.json" )
MALE_FIRST_NAME   = os.path.join( SOURCE_DIR, r"maleFirstNames.json" )
FEMALE_FIRST_NAME = os.path.join( SOURCE_DIR, r"femaleFirstNames.json" )
LAST_NAME         = os.path.join( SOURCE_DIR, r"surnames.json" )



class Names:
    def __init__(self) -> None:
        