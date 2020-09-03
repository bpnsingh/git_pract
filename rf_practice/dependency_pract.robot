*** Settings ***
Library  DependencyLibrary

*** Test cases ***
Passing Test
    No operation

Failing Test
    Fail  This test is intentionally hardcoded to fail

This Test Depends on "Passing Test" Passing
    Depends on test  Failing Test
    Log  The rest of the keywords in this test will run as normal.