"""1차원 엘리멘터리 세포 자동자.

규칙 하나(0~255)가 세 칸의 이웃 상태를 다음 세대의 한 칸으로 접는다.
현재 세대 한 줄만 들고 있으므로 메모리는 세대 수와 무관하다.
"""

import sys

ALIVE = "\u2588"
DEAD = " "


def rule_table(rule: int) -> list[int]:
    """규칙 번호를 8개 이웃 패턴에 대한 비트 테이블로 편다."""
    return [(rule >> i) & 1 for i in range(8)]


def step(row: list[int], table: list[int]) -> list[int]:
    """이웃 세 칸을 0..7 인덱스로 접는다. 경계는 원형으로 감는다."""
    n = len(row)
    return [table[(row[(i - 1) % n] << 2) | (row[i] << 1) | row[(i + 1) % n]] for i in range(n)]


def render(row: list[int]) -> str:
    return "".join(ALIVE if c else DEAD for c in row)


def main() -> int:
    args = sys.argv[1:]
    try:
        rule = int(args[0]) if len(args) > 0 else 82
        width = int(args[1]) if len(args) > 1 else 61
        gens = int(args[2]) if len(args) > 2 else 24
    except ValueError:
        print("arguments must be integers: main.py [rule] [width] [generations]", file=sys.stderr)
        return 1

    if not 0 <= rule <= 255:
        print(f"rule must be from 0 to 255. Got: {rule}", file=sys.stderr)
        return 1
    if width < 3:
        print("width must be at least 3.", file=sys.stderr)
        return 1

    table = rule_table(rule)
    row = [0] * width
    row[width // 2] = 1

    print(f"rule {rule}  width {width}  generations {gens}")
    print("-" * width)
    for _ in range(gens):
        print(render(row))
        row = step(row, table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
