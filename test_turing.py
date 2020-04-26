from turingmachine import TuringMachine

alphabet = ["a", "b", "*"]

print("Enter a string using the following symbols:", end=" ")
for i in alphabet:
    print(i, end=" ")
print()
input_string = input()

# make sure input characters are valid (in the alphabet)
for char in input_string:
    if char not in alphabet:
        print("Invalid input string.")
        exit()

initial_state = "q_0"
final_states = ["q_acc", "q_rej"]

# transition functions
transition_function = {
    ("q_0", "a"): ("q_0", "a", "R"),    # stay in q_0
    ("q_0", "b"): ("q_1", "b", "R"),    # transition to q_1 when 'b' is encountered
    ("q_0", "*"): ("q_rej", "*", "L"),  # no 'b's found and we reached the end. Reject and halt.
    ("q_1", "a"): ("q_1", "a", "R"),    # stay in q_1
    ("q_1", "b"): ("q_acc", "b", "R"),  # encountered second 'b'! Accept and halt.
    ("q_1", "*"): ("q_rej", "*", "L")   # only 1 'b' found. Reject and halt.
}

turing = TuringMachine(alphabet, input_string, "*", initial_state, final_states, transition_function)

# step through Turing machine until a final state is reached.
while not turing.final_state():
    turing.step()

if turing.current_state == "q_acc":
    print(f"String {input_string} is accepted")
else:
    print(f"String {input_string} is rejected")