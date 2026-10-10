
"""Motor de inferência do sistema especialista."""

from src.compatibilidade import preparar_experta

preparar_experta()

from experta import KnowledgeEngine, Rule, OR
from src.fatos import RespostaUsuario, EvidenciaCarreira


class MotorInferencia(KnowledgeEngine):
    """Gerencia os fatos e executa as regras de inferência."""

    # R01 — Identificação de perfil Back-end
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="A")
    )
    def regra_r01_backend(self):
        """Identifica interesse em desenvolvimento Back-end."""

        self.declare(
            EvidenciaCarreira(
                carreira="Back-end",
                regra="R01",
                justificativa=(
                    "Interesse em desenvolver APIs e regras de negócio, "
                    "combinado à preferência por implementar algoritmos "
                    "e funcionalidades."
                )
            )
        )
    
    # R02 — Back-end: desenvolvimento e ferramentas
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="A"),
        OR(
            RespostaUsuario(pergunta="Q03", alternativa="A"),
            RespostaUsuario(pergunta="Q03", alternativa="C"),
            RespostaUsuario(pergunta="Q03", alternativa="D")
        )
    )
    def regra_r02_backend(self):
        """Identifica afinidade técnica com Back-end."""

        self.declare(
            EvidenciaCarreira(
                carreira="Back-end",
                regra="R02",
                justificativa=(
                    "Interesse em desenvolver APIs e regras de negócio, "
                    "combinado à familiaridade com Python, Java/C# "
                    "ou bancos de dados."
                )
            )
        )

    # R03 — Identificação de perfil Front-end & UI/UX
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="B"),
        RespostaUsuario(pergunta="Q02", alternativa="B")
    )
    def regra_r03_frontend(self):
        """Identifica interesse em Front-end e UI/UX."""

        self.declare(
            EvidenciaCarreira(
                carreira="Front-end & UI/UX",
                regra="R03",
                justificativa=(
                    "Interesse em desenvolver interfaces web, "
                    "combinado à preferência por criar experiências "
                    "visuais e interativas."
                )
            )
        )

    # R04 — Front-end: desenvolvimento e ferramentas
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="B")
    )
    def regra_r04_frontend(self):
        """Identifica afinidade técnica com Front-end e UI/UX."""

        self.declare(
            EvidenciaCarreira(
                carreira="Front-end & UI/UX",
                regra="R04",
                justificativa=(
                    "Interesse em desenvolver interfaces web, "
                    "combinado à familiaridade com JavaScript, "
                    "HTML e CSS."
                )
            )
        )
    
    # R05 — Ciência de Dados: modelos preditivos e matemática
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="A"),
        RespostaUsuario(pergunta="Q01", alternativa="C")
    )
    def regra_r05_ciencia_dados(self):
        """Identifica afinidade com Ciência de Dados e ML."""

        self.declare(
            EvidenciaCarreira(
                carreira="Ciência de Dados e ML",
                regra="R05",
                justificativa=(
                    "Interesse em analisar dados e construir modelos "
                    "preditivos, combinado à alta afinidade com "
                    "matemática e estatística."
                )
            )
        )
    
    # R06 — Ciência de Dados: análise e identificação de padrões
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="C")
    )
    def regra_r06_ciencia_dados(self):
        """Identifica interesse em análise de dados e ML."""

        self.declare(
            EvidenciaCarreira(
                carreira="Ciência de Dados e ML",
                regra="R06",
                justificativa=(
                    "Interesse em desenvolver modelos preditivos, "
                    "combinado à preferência por analisar dados "
                    "e identificar padrões."
                )
            )
        )
    
    # R07 — Engenharia de Dados: processamento e transformação
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="B"),
        RespostaUsuario(pergunta="Q02", alternativa="D")
    )
    def regra_r07_engenharia_dados(self):
        """Identifica interesse em Engenharia de Dados."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Dados",
                regra="R07",
                justificativa=(
                    "Interesse em construir processos de coleta, "
                    "transformação e disponibilização de dados, "
                    "combinado à preferência por organizar "
                    "e processar grandes volumes de informações."
                )
            )
        )
    
    # R08 — Engenharia de Dados: pipelines e bancos de dados
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="D")
    )
    def regra_r08_engenharia_dados(self):
        """Identifica afinidade técnica com Engenharia de Dados."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Dados",
                regra="R08",
                justificativa=(
                    "Interesse em construir pipelines de coleta e "
                    "transformação de dados, combinado à "
                    "familiaridade com SQL e bancos de dados."
                )
            )
        )





    def analisar(self, respostas: dict[str, str]):
        """Recebe as respostas e executa o motor de inferência."""

        self.reset()

        for pergunta, alternativa in respostas.items():
            self.declare(
                RespostaUsuario(
                    pergunta=pergunta,
                    alternativa=alternativa
                )
            )

        self.run()
