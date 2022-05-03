import math

# --- Separates the number by commas (,), example: 1,234,456 ---
def fValue(number):
    return ("{:,}".format(number))

# --- Rounds Up the number, example 1234.56789 -> 1234.57 ---
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier