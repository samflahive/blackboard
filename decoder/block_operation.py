def math_block_operation(action, args, blocks):
    args = [int(arg) for arg in args.split("~")]
    if action == "+":
        block = blocks[args[0]]+blocks[args[1]]
    elif action == "-":
        block = blocks[args[0]]-blocks[args[1]]
    elif action == "*":
        block = blocks[args[0]]*blocks[args[1]]
    elif action == "d": # not / to avoid url problems
        block = blocks[args[0]]/blocks[args[1]]
    else:
        raise NotImplementedError(f"No implementation for operation {action}")

    blocks.append(block)
