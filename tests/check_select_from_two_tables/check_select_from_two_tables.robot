*** Settings ***
Documentation  Позитивные тесты для проверки запросов в базу данных
Metadata    Автор   Киятов Евгений
Resource    tests/check_select_from_two_tables/select_resource.robot
Test Setup  Test Setup
Test Teardown  Test Teardown

*** Test Cases ***
Check Select On Two Tables
    [Documentation]  Проверка запроса для двух таблиц
    ${title}    ${categoryname}     get_rest.get title and categoryname rest  alias=alias   url=/products?  params=select=*,categories(categoryname)
    ${title_db}     ${category_db}    get_sql.get title and categoryname sql  title=     categoryname=
    Col.Lists Should Be Equal    ${title_db}     ${title}
    Col.Lists Should Be Equal   ${category_db}      ${categoryname}



