class AvaliadorFenotipoGraoDeBico:
    def __init__(self, caminho_foto: str, dias_apos_plantio: int):
        self.caminho_foto = caminho_foto
        self.dias_apos_plantio = dias_apos_plantio  # NOVA VARIÁVEL DE ENTRADA

        # Prompt 1 — Persona (Mantido)
        self.P1_PERSONA = (
            "Assuma a persona de um Engenheiro Agrônomo especialista em fisiologia vegetal e grão-de-bico. "
            "Sua tarefa é avaliar a saúde e o desenvolvimento das plantas com base na idade da cultura."
        )

        # Prompt 2 — Contexto (NOVO E CRUCIAL)
        # Aqui injetamos a regra de negócio baseada na idade
        self.P2_CONTEXTO = (
            f"DADOS DA AMOSTRA:\n"
            f"- Cultura: Grão-de-bico (Cicer arietinum)\n"
            f"- Idade: {self.dias_apos_plantio} dias após o plantio (DAP).\n\n"
            "REGRA DE INTERPRETAÇÃO FENOLÓGICA:\n"
            "Use a idade para calibrar sua avaliação de 'saúde':\n"
            "1. FASE VEGETATIVA/REPRODUTIVA (0 a ~90 dias): O esperado é tecido verde e turgido. "
            "Clorose, necrose ou seca são defeitos graves (Doença/Estresse).\n"
            "2. FASE DE MATURAÇÃO/SENESCÊNCIA (>90 dias): O esperado é o amarelecimento natural (clorose senescente) "
            "e secagem dos tecidos para colheita. NÃO penalize a cor marrom/amarela se for uniforme (sinal de maturação). "
            "Penalize apenas anomalias (manchas de fungos, podridão ou 'ficar verde' quando deveria estar seco)."
        )

        # Prompt 3 — Observação (Ligeiro ajuste para focar em anomalias)
        self.P3_OBSERVACAO = (
            "Descreva visualmente a planta focando em:\n"
            "1) Coloração (Verde vs. Amarelo/Marrom).\n"
            "2) Turgidez (Ereta/Hidratada vs. Seca/Quebradiça).\n"
            "3) Presença de estruturas reprodutivas (Flores, Vagens verdes, Vagens secas).\n"
            "4) Sinais de patógenos (Manchas circulares, mofo, lesões)."
        )

        # Prompt 4 — Ranking Dinâmico (Ajustado para a idade)
        self.P4_RANKING = (
            "Com base na idade informada, atribua uma Nota de Performance (1-5):\n\n"
            "CRITÉRIOS:\n"
            "- Nota 5 (Excelente): Planta compatível com a idade. "
            "(Se jovem: verde/vigorosa. Se velha: seca uniforme/muitas vagens).\n"
            "- Nota 3 (Regular): Atraso no desenvolvimento ou doença leve.\n"
            "- Nota 1 (Falha): Planta morta prematuramente (se jovem) ou apodrecida/doente.\n\n"
            "Saída obrigatória:\n"
            "Resumo: [Uma frase comparando a aparência com a idade esperada]\n"
            "Diagnóstico: [Estresse / Normal / Maturação]\n"
            "Nota: [1-5]"
        )

    def montar_prompt(self) -> str:
        return (
            f"{self.P1_PERSONA}\n\n"
            f"--- CONTEXTO OBRIGATÓRIO ---\n{self.P2_CONTEXTO}\n\n"
            f"--- TAREFA DE OBSERVAÇÃO ---\n{self.P3_OBSERVACAO}\n\n"
            f"--- TAREFA DE RANKING ---\n{self.P4_RANKING}"
        )

# Exemplo de como você chamaria no seu software Beta:
# imagem_colheita = "caminho/para/foto_amarela.jpg"
# avaliador = AvaliadorFenotipoGraoDeBico(imagem_colheita, dias_apos_plantio=110)
# prompt_final = avaliador.montar_prompt()