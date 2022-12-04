import os
import string
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    values = {letter: i for i, letter in enumerate(string.ascii_letters, start=1)}
    out = 0
    comp: List[str] = []
    for i, line in enumerate(s.splitlines()):
        if i != 0 and i % 3 == 0:
            comp = []
        comp.append(line)
        if len(comp) < 3:
            continue
        (val,) = set(comp[0]) & set(comp[1]) & set(comp[2])
        out += values[val]
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(solver(file_reader(file)))