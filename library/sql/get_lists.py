def get_lists(data,d1,d2):
    title_db = []
    category_db=[]
    for row in data:
        title_db.append(row[d1])
        category_db.append(row[d2])
    return title_db,category_db
