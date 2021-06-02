*** Settings ***
Documentation   Позитивные тесты для проверки занесения данных в таблицу
Metadata  Автор  Киятов Евгений
Resource  connections/connections.robot
Resource  tests/check_insert_into_table/insert_resource.robot
Resource  connections/imports.robot
Test Setup  Test Setup
Test Teardown  Delete From DB and Close Connections
*** Test Cases ***
Check Insert Into Table
    [Documentation]      Проверка занесения данных в таблицу с помощью REST-запроса
    insert_rest.insert into table rest  alias
    ${category}  ${categoryname}    get_rest.get category and categoryname rest  alias=alias
    ${category_db}  ${categoryname_db}  get_sql.get category and categoryname sql  category=   categoryname=
    Col.Lists Should Be Equal   ${category_db}  ${category}
    Col.Lists Should Be Equal   ${categoryname_db}  ${categoryname}