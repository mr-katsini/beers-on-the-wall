for quant in range(99, 0, -1):
    if quant > 1:
        print quant, "bottles of beer on the weall.", quant, 'bottles of beer.'
        if quant > 2:
            suffix = str(quant - 1) + "bottles of beer on the wall"
        else:
            suffix = "1 bottle of beer on the wall."
    elif quant == 1:
        print "1 bottle of beer on the wall"
        suffix = 'no more beer on the wall!'

    print "take one down, pass it around,", suffix
    print '--'
