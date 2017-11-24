pluralize = lambda x: x != 1 and 's' or ''
bottle_beer = lambda x: "{} bottle{} of beer".format(x, pluralize(x))

def _beer_printer(quant):
    print("{b} on the wall. {b}.".format(b=bottle_beer(quant)))
    next_up = "{} on the wall.\n--".format(bottle_beer(quant - 1))
    if quant - 1 <= 0:
        next_up = "no more bottles of beer on the wall."
    print("Take one down, pass it around, {}".format(next_up))

if __name__ == "__main__":
    list(map(lambda quant: _beer_printer(quant), range(99, 0, -1)))
