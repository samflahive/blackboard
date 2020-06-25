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
