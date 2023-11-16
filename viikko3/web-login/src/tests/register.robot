*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kettu
    Set Password  kurppala1
    Set Password Confirmation  kurppala1
    Submit Credentials  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  kurppala1
    Set Password Confirmation  kurppala1
    Submit Credentials  Register
    Register Should Fail With Message  Username must be at least 3 characters long and contain only letters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kettu
    Set Password  kurppala
    Set Password Confirmation  kurppala
    Submit Credentials  Register
    Register Should Fail With Message  Password must be at least 8 characters long and contain letters and at least one digit

Register With Nonmatching Password And Password Confirmation
    Set Username  kettu
    Set Password  kurppala1
    Set Password Confirmation  kurppala2
    Submit Credentials  Register
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  kettu
    Set Password  kurppala1
    Set Password Confirmation  kurppala1
    Submit Credentials  Register
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  kettu
    Set Password  kurppala1
    Submit Credentials  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  ab
    Set Password  kurppala1
    Set Password Confirmation  kurppala1
    Submit Credentials  Register
    Register Should Fail With Message  Username must be at least 3 characters long and contain only letters
    Go To Login Page
    Login Page Should Be Open
    Set Username  ab
    Set Password  kurppala1
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    [Arguments]  ${operation}
    Click Button  ${operation}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}