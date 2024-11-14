# 23 - Construa um AFN que aceite qualquer string que contenha a sequência "101" ou "110" sobre {0, 1}.
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

states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'1': {'q1'}},
    'q1': {'0': {'q2'}, '1': {'q4'}},
    'q2': {'1': {'q3'}},
    'q4': {'0': {'q5'}},
    'q3': {'0': {'q3'}, '1': {'q3'}, '0': {'q3'}, '1': {'q3'}},
    'q5': {'0': {'q5'}, '1': {'q5'}}
}
start_state = 'q0'
accept_states = {'q3', 'q5'}

nfa = Main(states, alphabet, transition_function, start_state, accept_states)

input_string = input("Digite uma string de teste: ")
print(f"String '{input_string}' é aceita? {nfa.accept(input_string)}")
