import sys

sys.setrecursionlimit(10000)

def read_input(filename: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    rules = {}
    orders = []
    with open(filename) as f:
        while (line := f.readline()) and line.strip():
            i, j = map(int, line.split("|"))
            rules[i] = {j, *rules.get(i, [])}
        while (line := f.readline()) and line.strip():
            orders.append(list(map(int, line.split(","))))
    return rules, orders

def get_order_value(rules: dict[int, set[int]], order: list[int], changed: bool = False) -> int:
    seen = set()
    for i, page in enumerate(order):
        if failing_rule := rules.get(page, set()).intersection(seen):
            failed = failing_rule.pop()
            failure_id = order.index(failed)
            for j in range(failure_id, i):
                order[j] = order[j+1]
            order[i] = failed
            return get_order_value(rules, order, True)
        seen.add(page)
    if changed:
        return order[int((len(order)-1) / 2)]
    return 0

def solve(rules: dict[int, set[int]], orders: list[list[int]]) -> int:
    sum = 0
    for order in orders:
        sum += get_order_value(rules, order)
    return sum


if __name__ == "__main__":
    rules, orders = read_input(sys.argv[1])
    print(solve(rules, orders))
