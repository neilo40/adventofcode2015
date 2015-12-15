import json


with open("inputs/day12.txt", 'r') as fh:
    j = json.load(fh)


def get_numbers(obj):
    if type(obj) == list:
        return sum([get_numbers(x) for x in obj])
    elif type(obj) == dict:
        if "red" in obj.values():
            return 0
        else:
            return sum([get_numbers(obj[x]) for x in obj])
    elif type(obj) == int:
        return obj
    else:
        return 0


print(get_numbers(j))


