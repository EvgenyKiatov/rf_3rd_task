*** Settings ***
Library         RequestsLibrary     WITH NAME   Req
Library         PostgreSQLDB        WITH NAME   DB
Library         Collections         WITH NAME   Col
Library         library.rest.get_rest.Get_REST   WITH NAME  get_rest
Library         library.sql.get_sql.Get_SQL     WITH NAME  get_sql
