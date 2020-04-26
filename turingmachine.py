class TuringMachine:
    """
    The TuringMachine class has data members to contain various components of a Turing Machine
    - alphabet - The finite set of symbols that can be used by the input string. Includes the blank symbol.
    - tape - A list storing each cahracter of the input string in an individual cell. The last cell contains the blank symbol.
    - blank_symbol - The character used to specify a blank in the tape.
    - current_state - The current state of the machine. Starts at the initial state.
    - final_states - A list of states (accept and reject) that cause the machine to stop running when reached.
    - transition_function - A dictionary storing the conditions of transitions as the keys and the rules of transitions as the values.
    - head_position - The position in the tape where each step through the machine begins. Moves forward (R) or backwards (L) each step of the loop.
    """

    def __init__(self, alphabet, tape_string, blank_symbol, initial_state,
                 final_states, transition_function):
        self.alphabet = alphabet
        self.tape = list(tape_string)
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

        self.head_position = 0
        self.tape.append(blank_symbol)  # indicating end
    
    def step(self):
        current_char = self.tape[self.head_position]
        transition_key = (self.current_state, current_char)  # tuple of state and cell value

        # retrieve transition rule for current configuration
        if transition_key in self.transition_function:
            transition_rule = self.transition_function[transition_key]
            new_state, update_value, head_direction = transition_rule

            self.tape[self.head_position] = update_value  # write the cell value in the transition rule in current cell
            # move head position to right or left
            