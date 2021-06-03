from library.products import Products
class Insert_REST(Products):
    def insert_into_table_rest(self,alias:str,url:str,json:dict):
        """
        Занесение данных в таблицу с помощью REST-запроса
        :param json:Словарь,который описывает вставляемый кортеж.Ключ соответсвует имени домена, а значение, соответствующее ему,
         является значением, находящееся в кортеже под этим доменом.
        """
        self.get_requests_lib().post_on_session(alias=alias,url=url,json=json)