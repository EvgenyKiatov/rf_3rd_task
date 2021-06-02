from library.products import Products
class Get_REST(Products):
    def get_data_from_rest(self, alias, params,url='/products?'):
        result = self.get_requests_lib().get_on_session(alias=alias, url=url,params=params)
        return result.json()
    def get_title_and_categoryname_rest(self,alias):
        result = self.get_data_from_rest(alias=alias,url='/products?',params='select=*,categories(categoryname)',)
        title = self.js.get_elements(result,'$..title')
        categoryname = self.js.get_elements(result,'$..categoryname')
        return title, categoryname

    def get_category_and_categoryname_rest(self,alias):
        result = self.get_data_from_rest(alias=alias,url='/categories?',params='select=*')
        category = self.js.get_elements(result,'$..category')
        categoryname = self.js.get_elements(result,'$..categoryname')
        return category, categoryname