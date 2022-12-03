import os
import string

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    values = {letter: i for i, letter in enumerate(string.ascii_letters, start=1)}
    out = 0
    for line in s.splitlines():
        mid = len(line) // 2
        first, second = line[:mid], line[mid:]
        priority_item = set(first) & set(second)
        (idx,) = priority_item
        out += values[idx]
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(solver(file_reader(file)))
