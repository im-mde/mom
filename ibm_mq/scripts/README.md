## Ansible
Ansible playbooks install IBM MQ onto the remote machines. Each playbook
requires parameters to be set when executing: path to the tarball provided by
IBM and a boolean value (yes or no) to whether the tarball is on the remote
server or not.
```
ansible-playbook install.yml -e "package=/home/immde/mq.tar.gz remote=no MQ_INSTALL_PATH=/opt/mqm"
```
## CloudFormation
CloudFormation configurations are configured for AWS region us-east-2.
The availability zone option will need to be altered for use outside of
us-east-2. Failure to do so will result in an error when initializing 
the CloudFormation stack.

## Shell
Shell scripts provided for conveniance in IBM MQ administration. MQSC
input files are provided to define MQ objects that can be used for testing. Note
that the MQSC files will need to be altered for each use case such as when
defining objects like AUTHREC and CHLAUTH.