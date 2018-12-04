import re

def compute_timestamp(record):
    timestamp = record[0] * 12 + record[1]
    timestamp = timestamp * 31 + record[2]
    timestamp = timestamp * 24 + record[3]
    timestamp = timestamp * 60 + record[4]
    return timestamp


def process_input_line(line):
    match_obj = re.match("\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.+)", line)
    record = match_obj.groups()
    record = tuple(map(int, record[:-1])) + record[-1:]
    timestamp = compute_timestamp(record)
    record = (timestamp, ) + record
    return record


def read_records():
    records = []
    with open("input.txt") as puzzle_input:
        for line in puzzle_input:
            records.append(process_input_line(line))
    records.sort(key=lambda rec: rec[0])
    return records


def create_guards_sleeping_stats(records):
    current_guard = None
    last_sleep_min = None
    guards = dict()
    for record in records:
        words = record[6].split()
        if words[0] == "Guard":
            current_guard = int(words[1][1:])
            if current_guard not in guards:
                guards[current_guard] = [0 for _ in range(60)]
        elif words[0] == "falls":
            last_sleep_min = record[5]
        else: #wakes up
            for i in range(last_sleep_min, record[5]):
                guards[current_guard][i] += 1
    return guards


records = read_records()
guards = create_guards_sleeping_stats(records)

max_asleep = 0
max_minute = 0
max_guard = None
for guard, sleeping in guards.items():
    for i in range(60):
        if sleeping[i] > max_asleep:
            max_asleep = sleeping[i]
            max_minute = i
            max_guard = guard

print("Guard {} sleeps most frequent on minute {}.".format(max_guard, max_minute))
print("The answer is {}".format(max_guard * max_minute))
