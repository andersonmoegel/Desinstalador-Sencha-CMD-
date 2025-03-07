# Documentação do Script de Desinstalação do Sencha Cmd (Usuário Atual)

Este script é responsável por desinstalar o Sencha Cmd de uma instalação localizada na pasta `C:\Users\<usuario>\bin\Sencha`, excluindo os arquivos e pastas relacionados, e registrando a remoção em um arquivo de log.

## Funcionalidades

1. **Detecção do diretório de instalação do Sencha Cmd para o usuário atual**: O script verifica se o diretório onde o Sencha Cmd está instalado no perfil do usuário atual existe.
2. **Exclusão de arquivos**: O script remove todos os arquivos e pastas dentro do diretório de instalação do Sencha Cmd.
3. **Registro de remoção**: Após a remoção, o script registra no arquivo de log a mensagem "Sencha removido com sucesso".
4. **Logs**: O arquivo de log é armazenado em `C:\Windows\Temp\Sencha_Uninstall_Log.txt`.

## Estrutura do Código

### 1. Importação de Bibliotecas

```python
import os
import shutil
import time
import getpass
```
Essas bibliotecas são utilizadas para manipulação de arquivos e diretórios, além de obter o nome do usuário atual:
- **`os`**: Para manipulação de arquivos e verificação de diretórios.
- **`shutil`**: Para remover arquivos e pastas.
- **`time`**: Para registrar a data e a hora da remoção no log.
- **`getpass`**: Para obter o nome do usuário atual do sistema de forma segura.

### 2. Variáveis de Configuração

#### Caminho de instalação do Sencha Cmd

```python
base_path = f"C:\\Users\\{getpass.getuser()}\\bin\\Sencha"
```

Este é o caminho onde o Sencha Cmd está instalado para o usuário atual. O caminho é dinâmico e usa `getpass.getuser()` para determinar o nome do usuário, garantindo que o script funcione para qualquer usuário que esteja executando o script.

#### Caminho do arquivo de log

```python
log_path = r"C:\Windows\Temp\Sencha_Uninstall_Log.txt"
```

Este é o caminho do arquivo de log onde a remoção do Sencha Cmd será registrada, incluindo a data e a hora da remoção.

### 3. Funções

#### `log_remocao()`

```python
def log_remocao():
    """Registra apenas a mensagem 'Sencha removido com sucesso' no arquivo de log"""
    try:
        with open(log_path, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Sencha removido com sucesso\n")
        print("Sencha CMD removido com sucesso!")  # Exibe no terminal
    except Exception:
        pass  # Ignora erros ao gravar no log
```

Esta função é responsável por registrar no arquivo de log que o Sencha Cmd foi removido com sucesso, incluindo a data e a hora da remoção. Se ocorrer algum erro durante a gravação do log, ele será ignorado.

#### `excluir_arquivos(diretorio)`

```python
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
```

Essa função percorre o diretório fornecido e remove todos os arquivos e pastas dentro dele. Ela retorna `True` se algum arquivo ou pasta foi removido com sucesso, ou `False` caso contrário.

#### `desinstalar_sencha()`

```python
def desinstalar_sencha():
    """Desinstala o Sencha Cmd excluindo seus arquivos"""
    if os.path.exists(base_path):
        if excluir_arquivos(base_path):
            log_remocao()
    else:
        print("Diretório não encontrado. O Sencha Cmd pode não estar instalado.")  # Não cria log
```

Esta função verifica se o diretório de instalação do Sencha Cmd para o usuário atual existe. Se o diretório existir, ela chama a função `excluir_arquivos()` para excluir os arquivos e, em seguida, registra a remoção no arquivo de log. Caso o diretório não seja encontrado, uma mensagem é exibida no terminal, mas o log não é gerado.

### 4. Execução do Script

```python
if __name__ == "__main__":
    desinstalar_sencha()
```

Esta linha garante que o script será executado apenas quando for chamado diretamente (não quando importado como módulo). Ela chama a função `desinstalar_senha()` para iniciar o processo de desinstalação.

## Uso

1. **Executar o script**: Para rodar o script, basta executá-lo em um ambiente Python. O script irá verificar se o Sencha Cmd está instalado no diretório do usuário atual e, caso seja encontrado, procederá com a remoção.
2. **Verificar o log**: Após a execução, o arquivo de log localizado em `C:\Windows\Temp\Sencha_Uninstall_Log.txt` pode ser verificado para confirmar a remoção realizada.

## Possíveis Melhorias

- **Aprimoramento no gerenciamento de erros**: Em vez de ignorar os erros ao tentar gravar no log ou excluir arquivos, o script poderia registrar detalhes dos erros no log, para facilitar a resolução de problemas.
- **Verificação adicional de permissões**: O script pode ser expandido para verificar se o usuário tem permissões adequadas para excluir arquivos do diretório especificado.

## Conclusão

Este script foi desenvolvido para facilitar a remoção do Sencha Cmd, permitindo que a desinstalação seja realizada de forma automatizada, com registro da remoção para rastreamento e auditoria.
