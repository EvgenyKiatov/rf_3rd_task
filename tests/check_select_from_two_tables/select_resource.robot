*** Settings ***
Resource  connections/connections.robot
Resource  connections/imports.robot
*** Keywords ***
Test Setup
    Create Session
    Connect To Postrgesql
Test Teardown
    Req.Delete All Sessions
    DB.Disconnect From Postgresql
