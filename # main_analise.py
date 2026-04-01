# main_analise.py

from prompt_engine import PromptEngineering
import os

# -----------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL QUE ORQUESTRA A ANÁLISE
# -----------------------------------------------------------------------------
def iniciar_analise_assistida(caminho_foto_teste, idade_dap):
    """
    Orquestra o processo de análise de fenotipagem de Grão-de-Bico.
    Args:
        caminho_foto_teste (str): Caminho do arquivo de imagem.
        idade_dap (int): Dias Após Plantio (dado agronômico crucial).
    """
    
    # 1. Instancia o motor com a foto e a IDADE do cultivo (A inovação da versão Beta)
    motor_prompts = PromptEngineering(caminho_foto_teste, dias_apos_plantio=idade_dap)
    
    # 2. Gera o prompt inteligente
    prompt_final = motor_prompts.gerar_prompt_encadeado()
    
    # 3. Simulação da interface do software
    print("---------------------------------------------------------")
    print(" 🌱 Sistema de Fenotipagem Digital - Grão-de-Bico (Beta v1.0)")
    print("---------------------------------------------------------")
    print(f"Arquivo: {caminho_foto_teste}")
    print(f"Dado de Entrada do Usuário: {idade_dap} Dias Após Plantio")
    print("Status: Gerando Prompt com Contexto Fenológico...")
    
    # print("\n--- DEBUG: Prompt Enviado à IA ---")
    # print(prompt_final)
    # print("----------------------------------\n")
    
    # 4. Simulação do Workflow de IA
    print("\nExecutando Análise Cognitiva...")
    print("  -> Validando coerência Idade vs. Aparência Visual... OK.")
    print("  -> Detectando estruturas (Vagens/Folhas/Raízes)... OK.")
    print("  -> Verificando presença de patógenos (Ascochyta/Fusarium)... OK.")
    print("  -> Calculando Ranking de Vigor (1-5)... OK.")
    
    print("\n✅ Relatório Gerado com Sucesso.")
    
    return prompt_final

# -----------------------------------------------------------------------------
# EXECUÇÃO DE TESTE (CENÁRIOS)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    # CENÁRIO 1: Imagem de planta seca (Colheita) - Onde o prompt antigo falhava
    FOTO_COLHEITA = "imagem_campo_final.jpg"
    IDADE_COLHEITA = 115 # Dias (Maturação)
    
    # CENÁRIO 2: Imagem de planta morta precocemente
    FOTO_DOENCA = "planta_morta_jovem.jpg"
    IDADE_DOENCA = 45 # Dias (Vegetativo)

    print("\n=== TESTE DO CENÁRIO 1: COLHEITA ===")
    try:
        iniciar_analise_assistida(FOTO_COLHEITA, IDADE_COLHEITA)
    except Exception as e:
        print(f"Erro: {e}")

    print("\n=== TESTE DO CENÁRIO 2: MORTE PREMATURA ===")
    try:
        iniciar_analise_assistida(FOTO_DOENCA, IDADE_DOENCA)
    except Exception as e:
        print(f"Erro: {e}")