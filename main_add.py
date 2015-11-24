def sum( arg1, arg2 ):

    if (len(locals()) != 2):
        return None
    elif (type(arg1) or type(arg2)) == str:
        return False
    elif (type(arg1) or type(arg2)) == bool:
        return False
    else:
        total = arg1 + arg2
        return total;