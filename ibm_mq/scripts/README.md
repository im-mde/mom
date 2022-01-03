## Ansible
A sample ansible environment to install IBM MQ. The site playbook
requires variables to be set when executing: path to the tarball provided by
IBM and the preferred MQ_INSTALL_PATH. A group_vars file is included which is
used by default for the required variables. The site playbook can be executed
via the following command after making required changes to the ansible variable
and inventory file.
```
ansible-playbook -i sandbox site.yml
```
## CloudFormation
Sample AWS CloudFormation configurations to setup an AWS environment for IBM MQ.
CloudFormation configurations are configured for AWS region us-east-2.
The availability zone option will need to be altered for use outside of
us-east-2. Failure to do so will result in an error when initializing 
the CloudFormation stack.

## Shell
Shell scripts provided for conveniance in IBM MQ administration. MQSC
input files are provided to define MQ objects that can be used for testing. Note
that the MQSC files will need to be altered for each use case such as when
defining objects like AUTHREC and CHLAUTH.