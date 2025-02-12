class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        self.notas = []

    def adicionar_notas(self, nota):
        self.notas.append(nota)

    def media(self):
        if len(self.notas) > 0:

            return sum(self.notas) / len(self.notas)
        
        else:
            return 0
    
    def resultado(self):
        media_final = self.media()
        if media_final > 7:
            return 'Aprovado.'
        elif media_final >= 5:
            return 'Recuperação.'
        else:
            return 'Reprovado.'