## **Projeto: Validador de Senha Avançado**

### **Código Python Avançado**

```python
import re
from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def validar_senha(senha):
    mensagens = []

    if len(senha) < 8:
        mensagens.append("A senha deve ter pelo menos 8 caracteres.")
    if not re.search(r"[A-Z]", senha):
        mensagens.append("A senha deve conter ao menos uma letra maiúscula.")
    if not re.search(r"[a-z]", senha):
        mensagens.append("A senha deve conter ao menos uma letra minúscula.")
    if not re.search(r"[0-9]", senha):
        mensagens.append("A senha deve conter ao menos um número.")
    if not re.search(r"[!@#$%^&*()\-_=+]", senha):
        mensagens.append("A senha deve conter ao menos um caractere especial (!@#$%^&*()-_=+).")

    return mensagens

def main():
    print(Fore.CYAN + "=== Validador de Senha Avançado ===")
    
    while True:
        senha = input(Fore.YELLOW + "Digite sua senha: ")
        resultado = validar_senha(senha)

        if len(resultado) == 0:
            print(Fore.GREEN + "✅ Sua senha é forte!")
            break
        else:
            print(Fore.RED + "❌ Sua senha não atende aos seguintes critérios:")
            for msg in resultado:
                print(Fore.RED + "- " + msg)
            print(Fore.MAGENTA + "Tente novamente!\n")

if __name__ == "__main__":
    main()
```

---

### **Requisitos**

* Python 3.x
* Biblioteca `colorama` (para instalar: `pip install colorama`)

---

### **Como Executar**

1. Salve o código em `validador_senha_avancado.py`
2. Instale a biblioteca `colorama`:

```bash
pip install colorama
```

3. Execute:

```bash
python validador_senha_avancado.py
```

4. Digite senhas até criar uma forte.

---

### **Exemplo de Uso**

```text
=== Validador de Senha Avançado ===
Digite sua senha: abc123
❌ Sua senha não atende aos seguintes critérios:
- A senha deve ter pelo menos 8 caracteres.
- A senha deve conter ao menos uma letra maiúscula.
- A senha deve conter ao menos um caractere especial (!@#$%^&*()-_=+)
Tente novamente!

Digite sua senha: Abc123!
✅ Sua senha é forte!
```

---

### **README.md para GitHub**

````markdown
# 🔒 Validador de Senha Avançado

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

## Descrição
Este projeto é um **validador de senha avançado**, que verifica se a senha escolhida pelo usuário é forte o suficiente.  
Ele fornece **feedback colorido no terminal** e permite que o usuário tente várias senhas até criar uma válida.

---

## Requisitos
- Python 3.x
- Biblioteca `colorama` (`pip install colorama`)

---

## Como Executar
1. Salve o arquivo `validador_senha_avancado.py`  
2. Instale a biblioteca `colorama`:

```bash
pip install colorama
````

3. Execute o programa:

```bash
python validador_senha_avancado.py
```

4. Digite senhas até criar uma forte.

---

## Funcionalidades

* Feedback colorido no terminal
* Verificação de:

  * Mínimo de 8 caracteres
  * Letra maiúscula
  * Letra minúscula
  * Número
  * Caractere especial (!@#\$%^&\*()-\_=+)
* Loop interativo até a senha ser válida

---

## Melhorias Futuras

* Interface gráfica (Tkinter, PyQt)
* Salvar senhas fortes de forma criptografada
* Adicionar indicadores de força (fraca, média, forte)
* Suporte a múltiplos usuários

---

## Exemplo de Uso

```text
Digite sua senha: abc123
❌ Sua senha não atende aos seguintes critérios:
- A senha deve ter pelo menos 8 caracteres.
- A senha deve conter ao menos uma letra maiúscula.
- A senha deve conter ao menos um caractere especial (!@#$%^&*()-_=+)
Tente novamente!

Digite sua senha: Abc123!
✅ Sua senha é forte!
```

---

## Licença

Uso pessoal e acadêmico.
