#!/usr/bin/env python3

from colorama import Fore, Style, init
from pyfiglet import figlet_format

# Inicializa colorama
init(autoreset=True)

def banner():
    """Muestra el banner con el título de la herramienta."""
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.GREEN + Style.BRIGHT + figlet_format("MASKIFY", font="slant"))
    print(Fore.YELLOW + "      Developed by: Thomas O'Neil Álvarez".center(60))
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)

def mask_url(original_url, fake_url, keywords):
    """
    Genera una URL enmascarada siguiendo el formato funcional:
    https://fake-domain-keywords@original-domain.com
    """
    if original_url.startswith("http"):
        # Construye la URL enmascarada
        return f"https://{fake_url}-{keywords}@{original_url.split('//')[-1]}"
    else:
        return None

def main():
    """Función principal del programa."""
    banner()
    
    print(Fore.CYAN + Style.BRIGHT + "Welcome to Maskify!")
    print(Fore.YELLOW + "Create custom-masked URLs easily.\n")
    
    # Solicitar la URL original
    print(Fore.MAGENTA + "Step 1: Enter the URL you want to mask.")
    print(Fore.YELLOW + "Example: https://example.com/example")
    original_url = input(Fore.CYAN + "URL to mask: ").strip()

    # Validar URL original
    if not original_url.startswith("http"):
        print(Fore.RED + "Invalid URL! Make sure it starts with 'http' or 'https'.")
        return

    # Solicitar la URL ficticia
    print(Fore.MAGENTA + "\nStep 2: Enter a fake or custom domain.")
    print(Fore.YELLOW + "Example: movies.com")
    fake_url = input(Fore.CYAN + "Fake Domain: ").strip()

    # Solicitar palabras clave
    print(Fore.MAGENTA + "\nStep 3: Enter keywords for social engineering (no spaces).")
    print(Fore.YELLOW + "Example: horror-movies")
    keywords = input(Fore.CYAN + "Keywords: ").strip()

    # Generar la URL enmascarada
    print(Fore.YELLOW + "\nGenerating your masked URL...")
    masked_url = mask_url(original_url, fake_url, keywords)

    # Mostrar la URL final
    if masked_url:
        print(Fore.CYAN + "=" * 60)
        print(Fore.GREEN + "Your Masked URL is:")
        print(Fore.YELLOW + masked_url.center(60))
        print(Fore.CYAN + "=" * 60)
    else:
        print(Fore.RED + "Error creating the masked URL.")

if __name__ == "__main__":
    main()
