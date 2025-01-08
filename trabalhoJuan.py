# Crie sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas:
# Alunos: nome, matrícula, data de nascimento, sexo, endereço, telefone, e-mail.
# Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone, e-mail, disciplina, 
# Disciplinas: nome, código (Al1234), professor, carga horária.
# Turmas: nome, código (Al1234), disciplina, professor, alunos (lista-matricula).

# O sistema deve permitir a filtragem de professores por disciplina.
# O sistema deve permitir a matrícula de alunos em turmas.
# O sistema deve permitir a alocação de professores em disciplinas.
# O sistema deve permitir a alocação de disciplinas em turmas.
# O sistema deve permitir a consulta de alunos matriculados em disciplinas.
# O sistema deve permitir a consulta de disciplinas alocadas em turmas.

class Sistema_de_Cadastro_Escolar:
    def __init__(self):
        self.alunos = {}  #colocar os dados dos alunos automatico
        self.professores = {}  #colocar os dados dos professores automatico
        self.disciplinas = {}  #cadastrar diciplinas automatico
        self.turmas = {}  #cadastrar as turmas automatico

    def cadastrar_aluno(self):
        print("\nCadastro de Aluno:")
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        sexo = input("Sexo: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone (##) ####-####: ")
        email = input("E-mail: ")
        self.alunos[matricula] = {
            "nome": nome,
            "data_de_nascimento": data_nascimento,
            "sexo": sexo,
            "endereco": endereco,
            "telefone": telefone,
            "email": email
        }
        print(f"Aluno {nome} cadastrado com sucesso!")

    def cadastrar_professor(self):
        print("\nCadastro de Professor:")
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        data_de_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        sexo = input("Sexo: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone (##) ####-####: ")
        email = input("E-mail: ")
        self.professores[matricula] = {
            "nome": nome,
            "data_nascimento": data_de_nascimento,
            "sexo": sexo,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "disciplinas": []
        }
        print(f'Professor {nome} cadastrado com sucesso!')
        
    def cadastrar_turma(self):
        print('\nCadastrar Turma: ')
        codigo = input('Código da turma: ')
        nome = input('Nome da turma: ')
        self.turmas[codigo] = {
            'nome': nome,
            "disciplina": None,
            "professor": None,
            "alunos": []
        }
        print(f"Turma {nome} cadastrada com sucesso!")

    def cadastrar_disciplina(self):
        print("\nCadastro de Disciplina:")
        codigo = input("Código: ")
        nome = input("Nome: ")
        carga_horaria = input("Carga Horária: ")
        self.disciplinas[codigo] = {
            "nome": nome,
            "carga_horaria": carga_horaria,
            "professor": None
        }
        print(f'Disciplina {nome} cadastrada com sucesso!')


    def exibir_menu(self):
        while True:
            print("\n--- Sistema Escolar ---")
            print("1. Cadastrar Aluno")
            print("2. Cadastrar Professor")
            print("3. Cadastrar Disciplina")
            print("4. Cadastrar Turma")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar_aluno()
            elif opcao == "2":
                self.cadastrar_professor()
            elif opcao == "3":
                self.cadastrar_disciplina()
            elif opcao == "4":
                self.cadastrar_turma()
            elif opcao == "5":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Para colocar o sistema pra rodar é:
sistema = Sistema_de_Cadastro_Escolar()
sistema.exibir_menu()
