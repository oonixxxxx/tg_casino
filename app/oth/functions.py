def get_combo_text(dice_value: int):
    """
    Возвращает то, что было на конкретном дайсе-казино
    :param dice_value: значение дайса (число)
    :return: массив строк, содержащий все выпавшие элементы в виде текста
    Альтернативный вариант (ещё раз спасибо t.me/svinerus):
    return [casino[(dice_value - 1) // i % 4]for i in (1, 4, 16)]
    """
    #           0        1          2       3
    values = ["BAR", "виноград", "лимон", "семь"]

    dice_value -= 1
    result = []
        
    for _ in range(3):
        result.append(values[dice_value % 4])
        dice_value //= 4
        
    return result


def check_combo(value, cost):
    """
    Проверяет, что выпал дайс
    :param dice_value: значение дайса (число)
    :return: True, если выпал дайс
    """
    const = 0

    if value[0] == value[1] == value[2]:
        const = 3
    elif value[0] == value[1] or value[1] == value[2]:
        const = 2

    if const == 3:
        cost = cost * 1.3
    elif const == 2:
        cost = cost * 0.7
    else:
        cost = 0

    return cost