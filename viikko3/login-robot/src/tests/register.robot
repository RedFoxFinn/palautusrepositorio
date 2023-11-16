*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kettu  kanala321
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kurppala2
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  kurppala2
    Output Should Contain  Username must be at least 3 characters long and contain only letters

Register With Enought Long But Invalid Username And Valid Password
    Input Credentials  abc123  kurppala2
    Output Should Contain  Username must be at least 3 characters long and contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  kettu  kukku2
    Output Should Contain  Password must be at least 8 characters long and contain letters and at least one digit

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kettu  kukkalaatikko
    Output Should Contain  Password must be at least 8 characters long and contain letters and at least one digit

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command