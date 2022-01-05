import math

HEX_BIN_LOOKUP = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def convert_to_bin(hex):
    return "".join(HEX_BIN_LOOKUP[c] for c in hex)

class BitStringEnumerator:
    def __init__(self, bitstr) -> None:
        self.bitstr = bitstr
        self.ptr = 0
    
    def next(self, n):
        pos = self.ptr
        self.ptr += n
        return self.bitstr[pos:self.ptr]

def parse_packet(bitstr):
    bit_start_pos = bitstr.ptr
    version = int(bitstr.next(3), base=2)
    type_id = int(bitstr.next(3), base=2)
    value = None
    sub_packets = []
    if type_id == 4:
        bin_value = ""
        while True:
            group = bitstr.next(5)
            bin_value += group[1:]
            if group[0] == "0":
                break
        value = int(bin_value, base=2)
    else:
        length_type = bitstr.next(1)
        if length_type == "0":
            bit_length = int(bitstr.next(15), base=2)
            while bit_length > 0:
                sub_packet = parse_packet(bitstr)
                sub_packets.append(sub_packet)
                bit_length -= sub_packet[-1]
        else:
            num_packets = int(bitstr.next(11), base=2)
            for _ in range(num_packets):
                sub_packet = parse_packet(bitstr)
                sub_packets.append(sub_packet)
    packet_length = bitstr.ptr - bit_start_pos
    return (version, type_id, value, sub_packets, packet_length)

def sum_version_numbers(packet):
    s = packet[0]
    for sub_packet in packet[3]:
        s += sum_version_numbers(sub_packet)
    return s

def evaluate_packet(packet):
    if packet[1] == 0:
        return sum(evaluate_packet(p) for p in packet[3])
    elif packet[1] == 1:
        return math.prod(evaluate_packet(p) for p in packet[3])
    elif packet[1] == 2:
        return min(evaluate_packet(p) for p in packet[3])
    elif packet[1] == 3:
        return max(evaluate_packet(p) for p in packet[3])
    elif packet[1] == 4:
        return packet[2]
    left = evaluate_packet(packet[3][0])
    right = evaluate_packet(packet[3][1])
    if packet[1] == 5:
        return 1 if left > right else 0
    elif packet[1] == 6:
        print(packet)
        return 1 if left < right else 0
    elif packet[1] == 7:
        return 1 if left == right else 0

def solve_1(data):
    bitstr = convert_to_bin(data[0])
    bitstr = BitStringEnumerator(bitstr)
    parsed = parse_packet(bitstr)
    return sum_version_numbers(parsed)

def solve_2(data):
    bitstr = convert_to_bin(data[0])
    bitstr = BitStringEnumerator(bitstr)
    parsed = parse_packet(bitstr)
    return evaluate_packet(parsed)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
