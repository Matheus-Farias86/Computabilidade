# 6 - Construa um autômato finito não-determinístico (AFN) que aceite strings que contenham pelo menos um '0' sobre o alfabeto {0, 1}.
class Main:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def _move(self, current_states, symbol):
        new_states = set()
        for state in current_states:
            if symbol in self.transition_function.get(state, {}):
                new_states.update(self.transition_function[state][symbol])
        return new_states

    def accept(self, input_string):
        current_states = {self.start_state}
        for symbol in input_string:
            current_states = self._move(current_states, symbol)
        return bool(current_states & self.accept_states)

states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': {'q1'}, '1': {'q0'}},
    'q1': {'0': {'q1'}, '1': {'q1'}},
    'q2': {}
}
start_state = 'q0'
accept_states = {'q1'}

nfa = Main(states, alphabet, transition_function, start_state, accept_states)

input_string = input("Digite uma string de teste: ")
print(f"String '{input_string}' é aceita? {nfa.accept(input_string)}")
