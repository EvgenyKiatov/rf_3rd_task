*** Settings ***
Library         library.rest.insert_rest.Insert_REST    WITH NAME   insert_rest
Library         library.rest.delete_rest.Delete_REST    WITH NAME   delete_rest
*** Keywords ***
Delete From DB and Close Connections
    delete_rest.delete from table rest  alias=alias
    Req.Delete All Sessions
    DB.Disconnect From Postgresql