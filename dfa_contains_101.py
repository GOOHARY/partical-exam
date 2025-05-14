def dfa_contains_101(binary_string):
    state = 0
    for bit in binary_string:
        if state == 0:
            state = 1 if bit == '1' else 0
        elif state == 1:
            state = 2 if bit == '0' else 1
        elif state == 2:
            state = 3 if bit == '1' else 0
        elif state == 3:
            state = 3  # once accepted, remain in accepting state
    return state == 3

# Example usage
test_strings = ["1001", "101", "1101", "111", "010101"]
for s in test_strings:
    print(f"{s}: {'Accepted' if dfa_contains_101(s) else 'Rejected'}")