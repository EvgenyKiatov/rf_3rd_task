*** Settings ***
Library         library.rest.insert_rest.Insert_REST    WITH NAME   insert_rest
Library         library.rest.delete_rest.Delete_REST    WITH NAME   delete_rest
Resource  connections/connections.robot
Resource  connections/imports.robot
*** Keywords ***
Test Setup
    Create Session
    Connect To Postrgesql
Test Teardown
    delete_rest.delete from table rest  alias=alias
    Req.Delete All Sessions
    DB.Disconnect From Postgresql