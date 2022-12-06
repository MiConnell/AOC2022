from __future__ import annotations

import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file) as f:
        return f.read()


def solver(s: str) -> int:
    out = 0
    for line in s.splitlines():
        first, second = line.split(",")
        f_min, f_max = first.split("-")
        s_min, s_max = second.split("-")
        first_set = set(range(int(f_min), int(f_max) + 1))
        second_set = set(range(int(s_min), int(s_max) + 1))
        if first_set & second_set:
            out += 1
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(solver(file_reader(file)))
