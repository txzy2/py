import random

"""
Lab 1
В списке из 0 и 1 найти длинну самого длинного подряд идущего ряда 1
"""

def main(_list: list[int]) -> str:
    print(f"Start list: {_list}")
    print('-'*40)
    buff: int = 0

    list_of_max: List[int] = []

    for i in _list:
        if i == 1:
            buff += 1

        else:
            if buff > 0:
                list_of_max.append(buff)

            buff = 0

    return f"Max island is: {max(list_of_max)}"


if __name__ == '__main__':
    random_list: list[int] = [random.choice([0, 1]) for _ in range(20)]
    print(main(_list=random_list))
