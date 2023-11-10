class Aluno:
  def __init__(self, nome, matricula, curso):
    self.nome = nome
    self.matricula = matricula
    self.curso = curso

#dados_aluno = Aluno(input("Digite o nome do aluno: "), input("Digite a matricula do aluno: "), input("Digite o curso do aluno: "))

dados_aluno = Aluno("Etianne", "123456", "Professora")

print("nome: ", dados_aluno.nome)
print("matricula: ", dados_aluno.matricula)
print("curso: ", dados_aluno.curso)


