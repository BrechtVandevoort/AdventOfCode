def parse_data(data):
    connections = {}
    for left, right in map(lambda x: x.split("-"), data):
        if left not in connections:
            connections[left] = []
        if right not in connections:
            connections[right] = []
        connections[left].append(right)
        connections[right].append(left)
    return connections

def count_paths(edges, start, visited):
    if start == "end":
        return 1
    
    total = 0
    for node in edges[start]:
        if "A" <= node[0] <= "Z" or node not in visited:
            total += count_paths(edges, node, visited + [node])
    return total

def count_paths_2(edges, start, visited, twice_used):
    if start == "end":
        return 1
    
    total = 0
    for node in edges[start]:
        if "A" <= node[0] <= "Z" or \
                node not in visited or \
                (node != "start" and not twice_used):
            tw = twice_used or ("a" <= node[0] <= "z" and node in visited)
            total += count_paths_2(edges, node, visited + [node], tw)
    return total

def solve_1(data):
    edges = parse_data(data)
    return count_paths(edges, "start", ["start"])

def solve_2(data):
    edges = parse_data(data)
    return count_paths_2(edges, "start", ["start"], False)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
