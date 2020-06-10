import math_blocks

def fraction_method(args, description, blocks):

    # split
    if description == "sp":
        block = blocks[int(args)]
        result = block.split()
        blocks.append(result)

    # inverse
    elif description == "iv":
        block = blocks[int(args)]
        result = block.inverse()
        blocks.append(result)

    else:
        raise NotImplementedError(f"{description} is not a fraction method")


def chain_method(args, description, blocks):

    # ripple
    if description == "rs":
        block = blocks[int(args)]
        result = block.ripple_sign()
        blocks.append(result)

    else:
        raise NotImplementedError(f"{description} is not a fraction method")

def complex_method(args, description, blocks):

    # to_polar
    if description == "tp":
        block = blocks[int(args)]
        result = block.to_polar()
        blocks.append(result)

    # from_polar
    elif description == "fp":
        args = args.split("~")
        sign = args[-1] == "T"
        angle = blocks[int(args[0])]
        radius = blocks[int(args[1])]
        result = math_blocks.complex_number.from_polar(angle, radius, sign=sign)
        blocks.append(result)

    else:
        raise NotImplementedError(f"{description} is not a fraction method")

def exponential_method(args, description, blocks):
    # rebase
    if description == "rb":
        block, base = [blocks[int(arg)] for arg in args.split("~")]
        result = block.rebase(base)
        blocks.append(result)

    else:
        raise NotImplementedError(f"{description} is not a fraction method")
