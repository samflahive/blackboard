from .block_methods import math_block_method
from .create_block import create_math_block
from .block_operation import math_block_operation


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
        # block object method
        else:
            math_block_method(action, args, description, command_outputs)
    return command_outputs





example_line = '-100~100|rn|_i_,0~T|n|_i_,0~T|n|_i_,1~2|+|op,3~2|/|op'
example_line_2 = '-100~100|rn|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,1 2 3 4~T|c|_i_'
example_line_3 = 'x~ ~T|v|_i_,0~5|rn|_i_,1~T|n|_i_,1~T|n|_i_,1~T|n|_i_,1~T|n|_i_,2 3 4 5~0~T|sp|_i_'
example_line_4 = '-100~100|rn|_i_,0~T|n|_i_,0~T|n|_i_,1~2~T|f|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,4 5 3 6~T|c|_i_,0~T|n|_i_,7~8~T|f|_i_,9|f|sp'
example_line_5 = '-10~10|rn|_i_,0~T|n|_i_,y~1~T|v|_i_,0~T|n|_i_,0~T|n|_i_,0~T|n|_i_,2~3 4 5|sp|fr,2~5|py|rf,2~3 4|sp|fr,6~7~T|f|_i_'
examples = (example_line, example_line_2, example_line_3, example_line_4, example_line_5)
