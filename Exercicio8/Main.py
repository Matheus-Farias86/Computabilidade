# 8 - Desenvolva um AFN que aceite strings onde o número de '0's é divisível por 3.
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

states = {'q0', 'q1', 'q2'}
transition_function = {
    'q0': {'0': {'q1'}, '1': {'q0'}},
    'q1': {'0': {'q2'}, '1': {'q1'}},
    'q2': {'0': {'q0'}, '1': {'q2'}}
}
start_state = 'q0'
accept_states = {'q0'}

nfa = Main(states, transition_function, start_state, accept_states)

input_string = input("Insira a string para teste: ")
print(f"String '{input_string}' é aceita? {nfa.accept(input_string)}")
