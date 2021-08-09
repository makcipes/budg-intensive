def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    if some_date in range(1,30):
        print(some_date+1)
    elif some_date == 31:
        print("1")
    else:
        print("введена не верная дата")

    raise NotImplementedError
