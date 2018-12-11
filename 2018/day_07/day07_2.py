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


def available_tasks(constraints, todo, completed):
    available = set(todo)
    for constraint in constraints:
        if constraint[1] in available and constraint[0] not in completed:
            available.remove(constraint[1])
    return available


def first_available_worker(workers):
    min_worker = None
    for worker in workers:
        if min_worker is None or min_worker[0] > worker[0]:
            min_worker = worker
    return min_worker


NUM_WORKERS = 5
constraints = read_constraints()
todo = all_tasks(constraints)
completed = []
workers = [[0, None] for _ in range(NUM_WORKERS)]
while len(todo) > 0:
    # Take first available worker
    worker = first_available_worker(workers)
    #Collect all finished tasks
    for w in workers:
        if w[0] == worker[0]:
            completed_task = w[1]
            if completed_task is not None:
                completed.append(completed_task)
                w[1] = None
    # Take first available job
    available = available_tasks(constraints, todo, completed)
    if len(available) > 0:
        task = sorted(available)[0]
        todo.remove(task)
        task_duration = 61 + ord(task) - ord("A")
        worker[0] += task_duration
        worker[1] = task
    else:
        # No task available: wait one second
        worker[0] += 1
        worker[1] = None

finish_time = max(worker[0] for worker in workers)
print("The duration is {}.".format(finish_time))