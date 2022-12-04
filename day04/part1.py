import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()

def solver(s: str) -> int:
    out = 0
    for line in s.splitlines():
        first, second = line.split(',')
        f_min, f_max = int(first.split('-')[0]), int(first.split('-')[-1])
        s_min, s_max = int(second.split('-')[0]), int(second.split('-')[-1])
        if f_min <= s_min and s_max <= f_max or s_min <= f_min and f_max <= s_max:
            out += 1
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(solver(file_reader(file)))
