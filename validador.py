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
