def get_lists(data:str,d1:str,d2:str):
    """
    Получение списка значений для двух доменов
    :param data: Результат SQL-запроса
    :param d1:Имя первого домена
    :param d2:имя второго домена
    :return: Возвращает два списка значений для доменов
    """
    title_db = []
    category_db=[]
    for row in data:
        title_db.append(row[d1])
        category_db.append(row[d2])
    return title_db,category_db
