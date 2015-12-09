wires = {}
values = {}
with open("inputs/day7.txt", 'r') as fh:
    lines = fh.readlines()
for line in lines:
    parts = line.split()
    wires[parts[-1]] = parts[0:-2]


def get_value_for_wire(wire):
    if wire in values:
        return values[wire]
    elif wire == 'b':
        value = 956
    elif wire.isdigit():
        value = int(wire)
    else:
        parts = wires[wire]
        if len(parts) == 1:
            # 123 -> a
            # a -> b
            value = get_value_for_wire(parts[0])
        elif parts[0] == "NOT":
            # NOT a -> b
            value = ~get_value_for_wire(parts[1])
        else:
            if parts[1] == "AND":
                # 1 AND a -> b
                # a AND b -> c
                value = get_value_for_wire(parts[0]) & get_value_for_wire(parts[2])
            elif parts[1] == "OR":
                # a OR b -> c
                value = get_value_for_wire(parts[0]) | get_value_for_wire(parts[2])
            elif parts[1] == "RSHIFT":
                # a RSHIFT 2 -> c
                value = get_value_for_wire(parts[0]) >> get_value_for_wire(parts[2])
            elif parts[1] == "LSHIFT":
                # a LSHIFT 2 -> c
                value = get_value_for_wire(parts[0]) << get_value_for_wire(parts[2])
    values[wire] = value
    return value


print(get_value_for_wire('a'))
