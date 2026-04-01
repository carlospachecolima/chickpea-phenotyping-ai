import hashlib
import os

def calcular_hash_sha256(caminho_arquivo):
    """
    Calcula o Hash SHA-256 (Impressão Digital) do arquivo especificado.
    """
    # Verifica se o arquivo existe no caminho informado
    if not os.path.exists(caminho_arquivo):
        print(f"\n❌ ERRO CRÍTICO: O arquivo não foi encontrado.")
        print(f"O sistema procurou em: {caminho_arquivo}")
        print("Verifique se o pendrive/HD externo (E:) está conectado e se o nome da pasta está correto.")
        return None

    # Prepara o algoritmo SHA-256
    sha256_hash = hashlib.sha256()

    try:
        print(f"🔄 Lendo arquivo do disco E: ...")
        print(f"📂 Caminho: {caminho_arquivo}")
        
        # Abre o arquivo em modo binário de leitura
        with open(caminho_arquivo, "rb") as f:
            # Lê o arquivo em blocos de 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        # Retorna a string hexadecimal final
        return sha256_hash.hexdigest()

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

# --- CONFIGURAÇÃO ---
# O 'r' antes das aspas indica uma 'raw string', essencial para caminhos do Windows
ARQUIVO_ALVO = r"E:\Artigo Engenharia de Prompt Grão-de-Bico\Artigo Engenharia de Prompt Grão-de-Bico.zip"

# --- EXECUÇÃO ---
if __name__ == "__main__":
    print("\n" + "="*60)
    print(" 🔐 GERADOR DE HASH PARA REGISTRO DE SOFTWARE (INPI)")
    print("="*60)
    
    resultado_hash = calcular_hash_sha256(ARQUIVO_ALVO)
    
    if resultado_hash:
        print("\n✅ SUCESSO! CÓDIGO GERADO:")
        print("-" * 64)
        print(resultado_hash)
        print("-" * 64)
        print("\n📋 Copie o código acima para o formulário do INPI.")
        print("="*60 + "\n")