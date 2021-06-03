from library.products import Products
class Insert_REST(Products):
    def insert_into_table_rest(self,alias,url,json):
       self.get_requests_lib().post_on_session(alias=alias,url=url,json=json)