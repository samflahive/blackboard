from .random_number import RandomNumber
import math_blocks.algebra

def get_sign(s):
    return s == "T"

def create_math_block(action, args, blocks):
    args = args.split("~")
    # random number
    if action == "rn":
        block = RandomNumber(int(args[0]),int(args[1]))

    # variable
    elif action == "v":
        if args[1] == " ":
            value = None
        else:
            value = extract_single_arg(int(args[1]), blocks)

        block = math_blocks.algebra.polynomials.Variable(args[0], value, sign=get_sign(args[2]))
            

    else:
        # single arg
        if action == "n":
            value = extract_single_arg(int(args[0]), blocks)
            sign = get_sign(args[1])
            block = math_blocks.algebra.core.Number(value=value, sign=sign)
            
        # list is first argument
        elif action in ["c","p","py","sp"]:
            list_args = extract_list_args(args[0], blocks)
            if action == "sp":
                block = math_blocks.algebra.exponentials.SimplePoly(list_args, extract_single_arg(int(args[1]), blocks), sign = get_sign(args[2]))
            else:
                block = convert_to_block_list_sign(list_args, get_sign(args[1]), action)
            
        # just two args and a sign
        else:
            block = convert_to_block_double(action, args, blocks)
            

    blocks.append(block)


def extract_single_arg(arg, blocks):
    # arg = int
    block = blocks[arg]
    if isinstance(block, RandomNumber):
        block = block.generate()

    return block

def convert_to_block_double(action, args, blocks):
    a = extract_single_arg(int(args[0]), blocks)
    b = extract_single_arg(int(args[1]), blocks)
    
    sign = get_sign(args[2])

    if action == "f":
        block = math_blocks.algebra.core.Fraction(a,b,sign=sign)
    elif action == "e":
        block = math_blocks.algebra.exponentials.Exponential(a,b,sign=sign)
    elif action == "l":
        block = math_blocks.algebra.exponentials.Logarithm(a,b,sign=sign)
    elif action == "cx":
        block = math_blocks.algebra.exponentials.ComplexNumber(a,b,sign=sign)
    else:
        raise NotImplementedError(f"No implementation for {action} yet.")

    return block

def convert_to_block_list_sign(list_args, sign, action):
    if action == "c":
        return math_blocks.algebra.core.Chain(items=list_args, sign=sign)
    elif action == "p":
        return math_blocks.algebra.core.Product(items=list_args, sign=sign)
    elif action == "py":
        return math_blocks.algebra.polynomials.Polynomial(items=list_args, sign=sign)
    else:
        raise NotImplementedError(f"No implementation for {action} yet.")


def extract_list_args(list_args, blocks):
    # list_arg = "0 1 2..."
    list_args = list_args.split(" ")
    list_args = [int(i) for i in list_args]
    return list(map(lambda arg: blocks[arg].generate() if isinstance(blocks[arg], RandomNumber) else blocks[arg], list_args))
    
