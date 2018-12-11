def read_constraints():
    constraints = []
    with open("input.txt") as puzzle_input:
        for line in puzzle_input:
            parts = line.split()
            constraints.append((parts[1], parts[7]))
    return constraints


def all_tasks(constraints):
    tasks = set()
    for constraint in constraints:
        tasks.add(constraint[0])
        tasks.add(constraint[1])
    return tasks


def available_tasks(constraints, todo):
    available = set(todo)
    for constraint in constraints:
        if constraint[1] in available and constraint[0] in todo:
            available.remove(constraint[1])
    return available


constraints = read_constraints()
todo = all_tasks(constraints)
completed = []
while len(todo) > 0:
    available = available_tasks(constraints, todo)
    task = sorted(available)[0]
    completed.append(task)
    todo.remove(task)

print("The order is {}.".format("".join(completed)))