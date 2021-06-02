from robot.libraries.BuiltIn import BuiltIn
from JsonValidator import JsonValidator
class Products(object):
    builtin_lib: BuiltIn = BuiltIn()
    js : JsonValidator = JsonValidator()
    def get_postgresql_lib(self):
        return self.builtin_lib.get_library_instance("DB")

    def get_requests_lib(self):
        return self.builtin_lib.get_library_instance("Req")

