class Triagem:
    """
    Responsável por tratar o tipo de atendimento escolhido.
    Se for 'Emergência', deve ignorar senhas/fila e exibir alerta.
    """

    ALERTA_EMERGENCIA = "ENCAMINHAR IMEDIATAMENTE AO BOX MÉDICO"

    def __init__(self):
        self.emergencia = False

    def avaliar(self, servico: str) -> str:
        """
        Recebe uma string (serviço escolhido) e retorna:
          - alerta de emergência, se for emergência
          - string vazia, caso contrário
        """
        servico_norm = (servico or "").strip().lower()

        if servico_norm in ["emergencia", "emergência", "e"]:
            self.emergencia = True
            return self.ALERTA_EMERGENCIA

        self.emergencia = False
        return ""

    def is_emergencia(self) -> bool:
        return self.emergencia