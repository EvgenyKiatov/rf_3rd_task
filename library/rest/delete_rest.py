from library.products import Products
class Delete_REST(Products):
    def delete_from_table_rest(self,alias:str,url:str):
        """
        Удаление данных из таблицы с помощью REST-запроса
        """
        self.get_requests_lib().delete_on_session(alias=alias,url=url)