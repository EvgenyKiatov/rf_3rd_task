*** Settings ***
Documentation   Позитивные тесты для проверки занесения данных в таблицу
Metadata  Автор  Киятов Евгений
Resource  tests/check_insert_into_table/insert_resource.robot
Test Setup  Test Setup
Test Teardown  Test Teardown
*** Test Cases ***
Check Insert Into Table
    [Documentation]      Проверка занесения данных в таблицу с помощью REST-запроса
    ${json}  create dictionary  categoryname=Arthouse
    insert_rest.insert into table rest  alias=alias     url=/categories?    json=${json}
    ${category}  ${categoryname}    get_rest.get category and categoryname rest  alias=alias    url=/categories?    params=select=*
    ${category_db}  ${categoryname_db}  get_sql.get category and categoryname sql  category=   categoryname=
    Col.Lists Should Be Equal   ${category_db}  ${category}
    Col.Lists Should Be Equal   ${categoryname_db}  ${categoryname}