from library.products import Products
class Delete_REST(Products):
    def delete_from_table_rest(self,alias):
        self.get_requests_lib().delete_on_session(alias=alias,url='/categories?categoryname=eq.Arthouse')