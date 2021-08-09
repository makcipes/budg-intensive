def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    for item in range(1000,2000):
        if item % 7 == 0 and item % 5 !=0 :
            print(item)


    raise NotImplementedError

