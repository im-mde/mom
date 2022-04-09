# IBM MQ Message-Oriented Middleware

## How to deploy & create snapshot of custom RHEL8 IBM MQ install on AWS
[1] This cloudformation template utilized later on requires the IBM MQ install 
tarball to be located in an S3 bucket. If a bucket doesn't currently exist, 
create one and copy the tarball to it. This can be done via the AWS CLI if you 
have it installed on your local machine.
```
aws s3 mb s3://your-bucket
aws s3 cp mqadv_dev924_linux_x86-64.tar.gz s3://your-bucket
``` 
[2] After uploading the installation tarball to an S3 bucket, create an AWS 
CloudFormation stack. You will be given an option to upload a template file to 
which you should upload 
[ibmmq_rhel8.yml](scripts/cloudformation/ibmmq_rhel8.yml) 
provided in this repository. You can customize your install by making changes
to the UserData field in the provided template. 

After uploading the template, you will be asked to input a stack name and choose
values for custom parameters. Make sure to choose a valid keypair, the S3 bucket
storing the installation tarball, and the path pointing to the installation
tarball in the bucket before going through the rest of the options. After 
creating the stack, it will take  several minutes to deploy all AWS 
resources and the EC2 instance.

[3] When the EC2 instances is up, remotely access it via SSH to verify it
is configured correctly. You can verify MQ is installed via command 
``` dspmqinst ```. If installed correctly, information on the MQ install will
show up. Note if you verify the install immediately after the instance is
created, the init script may still be installing IBM MQ. You can verify this
by looking into the file /var/log/cloud-init-input.log.

[4] Following verification of the installation, create a snapshot of the
instance. This can be done in the AWS web portal by going to EC2, clicking on
the deployed instance and selecting **Action > Create Image**.

[5] To avoid getting charged further usage, go to CloudFormation
and delete the stack created in step 2. This will remove all AWS resources
created including the EC2 instance.

[6] To test your new snapshot, you can create an new EC2 instances and select
your snapshot which will show up in **My AMIs**.