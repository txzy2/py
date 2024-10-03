from rich.console import Console
console = Console()

def output(arr: list[list[int]]) -> None:
    for row in arr:
        print(' '.join(map(str, row)))

def right_triangle(arr: list[list[int]]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i <= j and i >= n - 1 - j:
                arr[i][j] = '+'

    print("\nПравый треугольник матрицы\n")
    output(arr)

def kv(n: int):
    console.print(
        """\n[red]Начальный массив[/red]\n"""
    )

    output([[0] * n for _ in range(n)])
    right_triangle([[0] * n for _ in range(n)])
