import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    lines = s.splitlines()
    split_index = 0
    previous_index = 0
    calories = []
    splits = [i for i, line in enumerate(lines) if line == '']
    for i, _ in enumerate(lines):
        if i in splits:
            calories.append(lines[previous_index:splits[split_index]])
            previous_index = i + 1
            split_index += 1
    out = sorted([sum(int(val) for val in c) for c in calories], reverse=True)
    return sum(out[:3])

if __name__ == "__main__":
    print(solver(file_reader(file)))
