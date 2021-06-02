*** Keywords ***
Test Setup
    Req.Create session                   alias       http://localhost:3000
    DB.Connect To Postgresql      hadb    authenticator   password2021dljfklkla1!kljf;    localhost  8432
Test Teardown
    Req.Delete All Sessions
    DB.Disconnect From Postgresql
