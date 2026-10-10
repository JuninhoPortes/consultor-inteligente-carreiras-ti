
"""Motor de inferência do sistema especialista."""

from src.compatibilidade import preparar_experta

preparar_experta()

from experta import KnowledgeEngine
from src.fatos import RespostaUsuario


class MotorInferencia(KnowledgeEngine):
    """Gerencia os fatos e executa as regras de inferência."""

    def analisar(self, respostas: dict[str, str]):
        """
        Recebe as respostas do questionário
        e executa o motor de inferência.
        """

        # Reinicia o motor para uma nova avaliação.
        self.reset()

        # Registra as respostas como fatos.
        for pergunta, alternativa in respostas.items():
            self.declare(
                RespostaUsuario(
                    pergunta=pergunta,
                    alternativa=alternativa
                )
            )

        # Executa as regras disponíveis.
        self.run()
