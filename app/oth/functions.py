def get_combo_text(dice_value: int):
    """return dice value as string


    Args:
        dice_value (int)

    Returns:
        list: list of dices values
    """    
    #           0         1        2        3
    values = ["BAR", "виноград", "лимон", "семь"]

    dice_value -= 1
    result = []
        
    for _ in range(3):
        result.append(values[dice_value % 4])
        dice_value //= 4
        
    return result


def check_combo(value, cost):
    """
    Checks if the dice have fallen 
    out :dice_value parameter: the value of the dice (number)
    returns: True if a bone has fallen out
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