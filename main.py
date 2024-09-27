import random
from rich.console import Console
from lab1 import max_island
from lab2 import kv

def main() -> None:
    console = Console()

    console.print(
        """[magenta]
██▓███ ▓██   ██▓    ██▓███   ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ▄████▄  
▓██░  ██▒▒██  ██▒   ▓██░  ██▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  
▓██░ ██▓▒ ▒██ ██░   ▓██░ ██▓▒▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒▓█    ▄ 
▒██▄█▓▒ ▒ ░ ▐██▓░   ▒██▄█▓▒ ▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒
▒██▒ ░  ░ ░ ██▒▓░   ▒██▒ ░  ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░▒ ▓███▀ ░
▒▓▒░ ░  ░  ██▒▒▒    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░
░▒ ░     ▓██ ░▒░    ░▒ ░       ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ▒ ░  ░  ▒   
░░       ▒ ▒ ░░     ░░         ░░   ░   ░   ▒   ░          ░       ▒ ░░        
     ░ ░                    ░           ░  ░░ ░                ░  ░ ░      
     ░ ░                                    ░                     ░        
        [/magenta]"""
    )
    console.print(
"[white]Сделал [red]Anton Kamaev[/red] [/white]\n\n"
    )

    while True:
        console.print("--Меню--", style="bold magenta")
        console.print("1. Lab1\n2. Lab2\n0. Выход", style="bold magenta")

        try:
            _input = int(input("Выберем пункт: "))
        except ValueError:
            _input = -1

        match _input:
            case 0:
                console.print("[green]Выход из программы...[/green]")
                break
            case 1:
                random_list: list[int] = [random.choice([0, 1]) for _ in range(20)]
                print(max_island(_list=random_list))
            case 2:
                n = int(input('Введите число: '))
                kv(n)
                break
            case _:
                console.print("\n[red]Неверный ввод, попробуйте снова[/red]\n")


if __name__ == '__main__':
    main()
