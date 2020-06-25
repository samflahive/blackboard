import math_blocks.algebra

def math_block_method(action, args, description, command_outputs):
    if action == "f":
        fraction_method(args, description, command_outputs)
    elif action == "c":
        chain_method(args, description, command_outputs)
    elif action == "cx":
        complex_method(args, description, command_outputs)
    elif action == "e":
        exponential_method(args, description, command_outputs)
    elif action == "sp" or action == "py":
        poly_method(args, description, command_outputs, action)
    else:
        raise NotImplementedError(f"{action} does not have any methods besides __init__")





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


def poly_method(args, description, blocks, poly_type):
    if poly_type == "sp":
        simple_poly_method(args, description, blocks)
    elif poly_type == "py":
        polynomials_method(args, description, blocks)

    else:
        raise ValueError("invalid action - must be 'sp' or 'py'")

def polynomials_method(args, description, blocks):
    # r2f
    if description == "rf":
        args = args.split("~")
        var = blocks[int(args[0])]
        val = blocks[int(args[1])]
        block = math_blocks.algebra.polynomials.Polynomial.root_to_factor(var,val)
        blocks.append(block)
        
    
def simple_poly_method(args, description, blocks):
    # from roots
    if description == "fr":
        args = args.split("~")
        var = blocks[int(args[0])]
        args = args[1].split(" ")
        roots = [blocks[int(arg)] for arg in args]
        block = math_blocks.algebra.polynomials.SimplePoly.from_roots(var, roots)
        blocks.append(block)
    else:
        raise NotImplementedError(f"{description} is not a fraction method")
