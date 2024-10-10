#10 - Implemente um AFN que aceite qualquer string que tenha pelo menos um '0' seguido de pelo menos um '1'.
class Main:
    def __init__(self, states, transition_function, start_state, accept_states):
        self.states = states
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def process(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol in self.transition_function[current_state]:
                current_state = self.transition_function[current_state][symbol].pop()
            else:
                current_state = 'q0'

        return current_state in self.accept_states

states = {'q0', 'q1', 'q2'}
transition_function = {
    'q0': {'0': {'q1'}, '1': {'q0'}},
    'q1': {'0': {'q1'}, '1': {'q2'}},
    'q2': {}
}

start_state = 'q0'
accept_states = {'q2'}

# Criando a instância do AFD
afd = Main(states, transition_function, start_state, accept_states)

# Entrada do usuário
stringUser = input("Digite uma string: ")
if afd.process(stringUser):
    print("A string é aceita.")
else:
    print("A string não é aceita.")
