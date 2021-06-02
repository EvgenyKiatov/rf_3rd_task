from library.products import Products
class Insert_REST(Products):
    def insert_into_table_rest(self,alias):
       self.get_requests_lib().post_on_session(alias=alias,url='/categories',json={'categoryname':'Arthouse'})