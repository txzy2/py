from rich.console import Console
console = Console()

def output(arr: list[list[int]]) -> None:
    for row in arr:
        print(' '.join(map(str, row)))

def up_half(arr: list[list[int]]) -> None:
    for i, row in enumerate(arr):
        for j in range(len(arr) - 1 - i, -1, -1):
            if row[j] == 0 and arr[j][i] == 0:
                row[j] = '+'

    console.print(
        """\n[red]Верхний треугольник квадратной матрицы[/red]\n"""
                  )
    output(arr)

def kv(n: int):
    console.print(
        """\n[red]Начальный массив[/red]\n"""
    )

    output([[0] * n for _ in range(n)])
    up_half([[0] * n for _ in range(n)])
