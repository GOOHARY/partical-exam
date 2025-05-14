def divisible_by_3(binary_string):
    state = 0
    for bit in binary_string:
        bit = int(bit)
        if state == 0:
            state = 0 if bit == 0 else 1
        elif state == 1:
            state = 2 if bit == 0 else 0
        elif state == 2:
            state = 1 if bit == 0 else 2
    return state == 0

# Example usage
binaries = ["0", "11", "110", "1001", "111"]
for b in binaries:
    print(f"{b}: {'Accepted' if divisible_by_3(b) else 'Rejected'}")