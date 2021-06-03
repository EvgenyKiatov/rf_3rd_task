from library.products import Products
class Get_REST(Products):
    def get_data_from_rest(self, alias:str, params:str,url='/products?'):
        """
        Получение значений из таблицы с помощью REST-запроса
        :return:Возвращает таблицу в формате JSON
        """
        result = self.get_requests_lib().get_on_session(alias=alias, url=url,params=params)
        return result.json()
    def get_title_and_categoryname_rest(self,alias:str,url:str,params:str):
        """
        Получение списков значений для определенных доменов
        :return: Возвращает два списка для доменов title и categoryname
        """
        result = self.get_data_from_rest(alias=alias,url=url,params=params)
        title = self.js.get_elements(result,'$..title')
        categoryname = self.js.get_elements(result,'$..categoryname')
        return title, categoryname

    def get_category_and_categoryname_rest(self,alias:str,url:str,params:str):
        """
        Получение списков значений для определенных доменов
        :return: Возвращает два списка для доменов category и categoryname
        """
        result = self.get_data_from_rest(alias=alias,url=url,params=params)
        category = self.js.get_elements(result,'$..category')
        categoryname = self.js.get_elements(result,'$..categoryname')
        return category, categoryname