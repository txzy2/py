from rich.console import Console 

from shared.text import text_lab1

"""
Lab 1
В списке из 0 и 1 найти длинну самого длинного подряд идущего ряда 1
"""

console = Console()

def max_island(_list: list[int]) -> str:
    console.print(f"""[red]{text_lab1}[/red]""")

    print(f"Начальный список: {_list}")
    buff: int = 0

    list_of_max: list[int] = []

    for i in _list:
        if i == 1:
            buff += 1

        else:
            if buff > 0:
                list_of_max.append(buff)

            buff = 0

    return f"Максимальный остров имеет длинну: {max(list_of_max)}"
