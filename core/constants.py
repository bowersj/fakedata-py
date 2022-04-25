from datetime import date

DEFAULT_BATCH_SIZE = 1000

# Defaults for random_variable.py
DEFAULT_MU = 0.5
DEFAULT_SIGMA = 0.10
DEFAULT_B = 1

DEFAULT_TIME_PATTERN = "%H:%M:%S.%f"
DEFAULT_DATE_PATTERN = "%Y-%m-%d"
DEFAULT_DATETIME_PATTERN = DEFAULT_DATE_PATTERN + "T" + DEFAULT_TIME_PATTERN

# This is the global default because it doesn't require values to be generated in batches which saves memory
DEFAULT_DIST = "numpy_integer"

sec_in_min = 60
sec_in_hr = 3600
micro_in_sec = 1_000_000

micro_in_min = micro_in_sec * sec_in_min
micro_in_hr  = micro_in_sec * sec_in_hr