*** Setting ***
Library SSHLibrary
Suite Setup Open Connection
Suite Teardown    Close Connection

*** Variables ***
${HOST} 192.168.0.1
${USERNAME} admin
${PASSWORD} 12345


*** Keywords ***
Open Connection and Login

*** Test Cases ***
Execute home directory list
    $output=Execute Command ls -l/home
    Login to console ${output}

