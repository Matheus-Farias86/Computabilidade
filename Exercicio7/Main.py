# 7 - Implemente um AFN que reconheça strings que comecem com '01' e terminem com '10'.
class Main:
    def __init__(self, states, transition_function, start_state, accept_states):
        self.states = states
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def _move(self, current_states, symbol):
        new_states = set()
        for state in current_states:
            if symbol in self.transition_function.get(state, {}):
                new_states.update(self.transition_function[state][symbol])
            elif state in self.transition_function:
                new_states.add(state)
        return new_states

    def accept(self, input_string):
        current_states = {self.start_state}
        for symbol in input_string:
            current_states = self._move(current_states, symbol)
        return bool(current_states & self.accept_states)

states = {'q0', 'q1', 'q2', 'q3', 'q4'}
transition_function = {
    'q0': {'0': {'q1'}},
    'q1': {'1': {'q2'}},
    'q2': {'0': {'q2'}, '1': {'q2', 'q3'}},
    'q3': {'0': {'q4'}}
}
start_state = 'q0'
accept_states = {'q4'}

nfa = Main(states, transition_function, start_state, accept_states)

input_string = input("Insira a string para teste: ")
print(f"String '{input_string}' é aceita? {nfa.accept(input_string)}")
