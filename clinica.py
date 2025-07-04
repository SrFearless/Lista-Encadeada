class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class FilaTriagem:
    def __init__(self):
        self.head = None
        self.cont_verde = 1
        self.cont_amarelo = 201

    def adicionar_sem_prioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def adicionar_com_prioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir_paciente(self):
        while True:
            escolha = input("Tipo de cartão (A=Amarelo, V=Verde): ").strip().upper()
            if escolha in ('A','V'):
                break
            print("Opção inválida. Digite A ou V.")
        if escolha == 'V':
            numero = self.cont_verde
            self.cont_verde += 1
        else:
            numero = self.cont_amarelo
            self.cont_amarelo += 1

        novo = Nodo(numero, escolha)
        if not self.head:
            self.head = novo
        elif escolha == 'V':
            self.adicionar_sem_prioridade(novo)
        else:
            self.adicionar_com_prioridade(novo)

        print(f"Paciente {escolha} de Número {numero} Foi Adicionado à Fila.")

    def mostrar_fila(self):
        if not self.head:
            print("A fila está vazia.")
            return
        print("Fila de Espera:")
        atual = self.head
        while atual:
            print(f"  • Prioridade {atual.cor} Número {atual.numero}")
            atual = atual.proximo

    def chamar_proximo(self):
        if not self.head:
            print("Não há pacientes para chamar.")
            return
        chamado = self.head
        self.head = self.head.proximo
        print(f"Chamando Paciente de Prioridade {chamado.cor} Número {chamado.numero} para atendimento.")

def menu():
    fila = FilaTriagem()
    while True:
        print("\n=== Menu ===")
        print("1 = Adicionar Paciente na Fila")
        print("2 = Ver Lista de Espera")
        print("3 = Chamar Paciente")
        print("4 = Sair")
        opc = input("Escolha: ").strip()
        if opc == '1':
            fila.inserir_paciente()
        elif opc == '2':
            fila.mostrar_fila()
        elif opc == '3':
            fila.chamar_proximo()
        elif opc == '4':
            print("Encerrando. Até logo!")
            break
        else:
            print("Escolha inválida. Tente de novo.")

if __name__ == "__main__":
    menu()
