INPUT_FILE = "input.txt"

def part_one():
    with open(INPUT_FILE, "r") as fp:
        data = fp.read()

    values = sorted([sum([int(y) for y in x.split("\n")]) for x in data.split("\n\n")])
    max_calories = values[-1]

    print(f"Result of part one: {max_calories}")

def part_two():
    with open(INPUT_FILE, "r") as fp:
        data = fp.read()

    values = sorted([sum([int(y) for y in x.split("\n")]) for x in data.split("\n\n")])
    total_sum = sum(values[-3:])

    print(f"Result of part one: {total_sum}")

if __name__ == '__main__':
    part_one()
    part_two()