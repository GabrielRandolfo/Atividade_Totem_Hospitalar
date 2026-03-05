class GeradorSenha:

    contador_geral = 0
    contador_prioridade = 0

    def gerar(self, tipo):
        if tipo == "Prioritário":
            GeradorSenha.contador_prioridade += 1
            return f"P-{GeradorSenha.contador_prioridade:03d}"
        else:
            GeradorSenha.contador_geral += 1
            return f"G-{GeradorSenha.contador_geral:03d}"
