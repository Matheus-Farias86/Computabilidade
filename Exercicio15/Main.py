# 15 - Implemente um AFN que reconheça a linguagem de todas as strings sobre {a, b} com comprimento par.
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

# Definição dos estados e transições para alternar entre par e ímpar
states = {'q0', 'q1'}
alphabet = {'a', 'b'}
transition_function = {
    'q0': {'a': {'q1'}, 'b': {'q1'}},  # Estado q0 (par), vai para q1 (ímpar) ao receber 'a' ou 'b'
    'q1': {'a': {'q0'}, 'b': {'q0'}}   # Estado q1 (ímpar), vai para q0 (par) ao receber 'a' ou 'b'
}
start_state = 'q0'
accept_states = {'q0'}  # Aceita apenas se terminar em q0 (comprimento par)

nfa = Main(states, alphabet, transition_function, start_state, accept_states)

# Entrada de teste
input_string = input("Digite uma string sobre {a, b}: ")
print(f"String '{input_string}' é aceita? {'Sim' if nfa.accept(input_string) else 'Não'}")
