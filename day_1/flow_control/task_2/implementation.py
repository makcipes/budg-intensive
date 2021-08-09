def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """

    """цельсий в фаренгейты"""
    if to_scale == "farengeit":
        value = value * 9/5  +32
        print(value)
    elif to_scale == "celsius":
        value = (value - 32) * 5/9
        print(value)



    raise NotImplementedError


