from library.products import Products
from library.sql.get_lists import get_lists
class Get_SQL(Products):
    def get_title_and_categoryname_sql(self, title, categoryname):
        """
        Для SQL-запроса из двух таблиц
        Получение списков для значений двух доменов
        :return: Возвращает два списка
        """
        sql = """ SELECT title, categoryname 
        from bootcamp.products,bootcamp.categories 
        where categories.category=products.category"""

        params = {"title": title, "categoryname": categoryname}
        result = self.get_postgresql_lib().execute_sql_string_mapped(sql, **params)
        title_db,categoryname_db = get_lists(result,d1='title',d2='categoryname')
        return title_db, categoryname_db
    def get_category_and_categoryname_sql(self,category,categoryname):
        """
        Для SQL-запроса из одной таблицы
        Получение списков для значений двух доменов
        :return: Возвращает два списка
        """
        sql = """select category,categoryname
        from bootcamp.categories"""
        params = {'category':category,'categoryname':categoryname}
        result = self.get_postgresql_lib().execute_sql_string_mapped(sql,**params)
        category_db,caegoryname_db = get_lists(result,d1='category',d2='categoryname')
        return category_db,caegoryname_db