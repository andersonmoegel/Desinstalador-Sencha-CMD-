import os
import shutil
import time
import getpass

# Caminho base para os usuários
base_path = f"C:\\Users\\{getpass.getuser()}\\bin\\Sencha"
# Caminho para o arquivo de log
log_path = r"C:\Windows\Temp\Sencha_Uninstall_Log.txt"

def log_remocao():
    """Registra apenas a mensagem 'Sencha removido com sucesso' no arquivo de log"""
    try:
        with open(log_path, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Sencha removido com sucesso\n")
        print("Sencha CMD removido com sucesso!")  # Exibe no terminal
    except Exception:
        pass  # Ignora erros ao gravar no log

def excluir_arquivos(diretorio):
    """Exclui todos os arquivos e pastas dentro do diretório fornecido"""
    removido = False
    for root, dirs, files in os.walk(diretorio, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
                removido = True
            except Exception:
                pass
        for name in dirs:
            try:
                shutil.rmtree(os.path.join(root, name))
                removido = True
            except Exception:
                pass
    return removido

def desinstalar_sencha():
    """Desinstala o Sencha Cmd excluindo seus arquivos"""
    if os.path.exists(base_path):
        if excluir_arquivos(base_path):
            log_remocao()
    else:
        print("Diretório não encontrado. O Sencha Cmd pode não estar instalado.")  # Não cria log

if __name__ == "__main__":
    desinstalar_sencha()
