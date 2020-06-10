import math_blocks
from random import randint
from block_methods import *

class random_number:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def generate(self):
        return randint(self.lower, self.upper)


def decode_math_board(line):

    commands = line.split(",")

    command_outputs = []
    
    for command in commands:
        args, action, description = command.split("|")

        # creating an object
        if description == "_i_":
            create_math_block(action, args, command_outputs)
        # performing and operation
        elif description == "op":
            math_block_operation(action, args, command_outputs)
        # not implemented
        else:
            if action == "f":
                fraction_method(args, description, command_outputs)
            elif action == "c":
                chain_method(args, description, command_outputs)
            elif action == "cx":
                complex_method(args, description, command_outputs)
            elif action == "e":
                exponential_method(args, description, command_outputs)
            else:
                raise NotImplementedError(f"{action} does not have any methods besides __init__")
    return command_outputs


def get_sign(s):
    return s == "T"

def extract_single_arg(arg, blocks):
    # arg = int
    block = blocks[arg]
    if isinstance(block, random_number):
        block = block.generate()

    return block

def convert_to_block_double(action, args, blocks):
    a = extract_single_arg(int(args[0]), blocks)
    b = extract_single_arg(int(args[1]), blocks)
    
    sign = get_sign(args[2])

    if action == "f":
        block = math_blocks.fraction(a,b,sign=sign)
    elif action == "e":
        block = math_blocks.exponential(a,b,sign=sign)
    elif action == "l":
        block = math_blocks.logarithm(a,b,sign=sign)
    elif action == "cx":
        block = math_blocks.complex_number(a,b,sign=sign)
    else:
        raise NotImplementedError(f"No implementation for {action} yet.")

    return block

def convert_to_block_list_sign(list_args, sign, action):
    if action == "c":
        return math_blocks.chain(items=list_args, sign=sign)
    elif action == "p":
        return math_blocks.product(items=list_args, sign=sign)
    elif action == "py":
        return math_blocks.polynomial(items=list_args, sign=sign)
    else:
        raise NotImplementedError(f"No implementation for {action} yet.")


def extract_list_args(list_args, blocks):
    # list_arg = "0 1 2..."
    list_args = list_args.split(" ")
    list_args = [int(i) for i in list_args]
    return list(map(lambda arg: blocks[arg].generate() if isinstance(blocks[arg], random_number) else blocks[arg], list_args))
    


def create_math_block(action, args, blocks):
    args = args.split("~")
    # random number
    if action == "rn":
        block = random_number(int(args[0]),int(args[1]))

    # variable
    elif action == "v":
        if args[1] == " ":
            value = None
        else:
            value = extract_single_arg(int(args[1]), blocks)

        block = math_blocks.variable(args[0], value, sign=get_sign(args[2]))
            

    else:
        # single arg
        if action == "n":
            value = extract_single_arg(int(args[0]), blocks)
            sign = get_sign(args[1])
            block = math_blocks.number(value=value, sign=sign)
            
        # list is first argument
        elif action in ["c","p","py","sp"]:
            list_args = extract_list_args(args[0], blocks)
            if action == "sp":
                block = math_blocks.simple_poly(list_args, extract_single_arg(int(args[1]), blocks), sign = get_sign(args[2]))
            else:
                block = convert_to_block_list_sign(list_args, get_sign(args[1]), action)
            
        # just two args and a sign
        else:
            block = convert_to_block_double(action, args, blocks)
            

    blocks.append(block)

def math_block_operation(action, args, blocks):
    args = [int(arg) for arg in args.split("~")]
    if action == "+":
        block = blocks[args[0]]+blocks[args[1]]
    elif action == "-":
        block = blocks[args[0]]-blocks[args[1]]
    elif action == "*":
        block = blocks[args[0]]*blocks[args[1]]
    elif action == "/":
        block = blocks[args[0]]/blocks[args[1]]
    else:
        raise NotImplementedError(f"No implementation for operation {action}")

    blocks.append(block)


example_line = '-100~100|rn|_i_,0~T|n|_i_,0~T|n|_i_,1~2|+|op,3~2|/|op'
example_line_2 = '-100~100|rn|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,1 2 3 4~T|c|_i_'
example_line_3 = 'x~ ~T|v|_i_,0~5|rn|_i_,1~T|n|_i_,1~T|n|_i_,1~T|n|_i_,1~T|n|_i_,2 3 4 5~0~T|sp|_i_'
example_line_4 = '-100~100|rn|_i_,0~T|n|_i_,0~T|n|_i_,1~2~T|f|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,4 5 3 6~T|c|_i_,0~T|n|_i_,7~8~T|f|_i_,9|f|sp'
out = decode_math_board(example_line_4)
print(out[-1].latex())
