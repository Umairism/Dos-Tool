from colorama import Fore, Style

def display_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
 __        __   _     _     _           
 \ \      / /__| |__ (_)___| |__  _ __  
  \ \ /\ / / _ \ '_ \| / __| '_ \| '_ \ 
   \ V  V /  __/ |_) | \__ \ | | | |_) |
    \_/\_/ \___|_.__/|_|___/_| |_| .__/ 
                                 |_|    
            Whistler v0.3       
""")
    print(Fore.YELLOW + Style.BRIGHT + "A powerful DDoS tool for educational purposes only.")
    print(Fore.YELLOW + Style.BRIGHT + "Use responsibly and ensure you have permission to test the target.")
    print(Fore.RESET + Style.RESET_ALL)
