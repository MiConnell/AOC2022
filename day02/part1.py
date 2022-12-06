from __future__ import annotations

import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file) as f:
        return f.read()


def solver(s: str) -> int:
    _translation = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"}
    values = {"R": 1, "P": 2, "S": 3}
    winning_losing_scores = {"R": "S", "P": "R", "S": "P"}
    total_score = 0
    for line in s.splitlines():
        opp, my = line.split(" ")
        opp, my = _translation[opp], _translation[my]
        if winning_losing_scores[opp] == my:
            total_score += 0 + values[my]
        elif winning_losing_scores[my] == opp:
            total_score += 6 + values[my]
        else:
            total_score += 3 + values[my]
    return total_score


def main() -> int:
    print(solver(file_reader(file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
