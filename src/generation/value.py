
def check_value(value):
    if value < 0:
        value = 0
    elif value > 100:
        value = 100
    return value