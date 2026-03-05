class Paciente:
    def __init__(self, nome: str, idade: int, pcd: bool = False):
        self.nome = nome
        self.idade = idade
        self.pcd = pcd

    def __str__(self):
        tipo = "PCD" if self.pcd else "Não PCD"
        return f"Paciente: {self.nome} | Idade: {self.idade} | {tipo}"