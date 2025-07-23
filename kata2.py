def make_negative( number ):
    if number <= 0:
        return number
    number = str(number)
    number = int(f"-{number}")
    return number