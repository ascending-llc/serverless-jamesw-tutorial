![name-of-you-image](https://raw.githubusercontent.com/weibeld/sam-hello-world/master/sam.png)

# ASCENDING SAM AWS demo by James Whyte
This project serves as a demostration of using SAM AWS to deploy a serverless hello-world application.

## Usage
The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS.

A serverless application is a combination of:
- Lambda functions
- Event source
- CloudFormation template
- Test

Note: SAM is more than just a Lambda function—it can include additional resources such as APIs, databases, and event source mappings.

## Application
The sample application provides a REST API (with API Gateway) with a single endpoint. When this endpoint is requested, a Lambda function is triggered.

## Prerequisites
Creating AWS account, AWS Identity and Access Management (IAM) permissions, and installatiion of SAM CLI required deployment.

## Containerization (optional)

For sandboxing and testing on local machine one can use a docker image.

## Deloy
To deploy the application to AWS use SAM CLI with the following:

```python
#Step 1 - Download a sample application
sam init

#Step 2 - Build your application
cd sam-app
sam build

#Step 3 - Deploy your application
sam deploy --guided
```

These commands deploy your application to the AWS Cloud. It takes the deployment artifacts that you build with the sam build command, packages and uploads them to an Amazon Simple Storage Service (Amazon S3) bucket that the AWS SAM CLI creates, and deploys the application using AWS CloudFormation. In the output of the sam deploy command, you can see the changes being made to your AWS CloudFormation stack.

# HTTP endpoint trigger
If your application created an HTTP endpoint, the outputs that sam deploy generates also show you the endpoint URL for your test application. You can use curl to send a request to your application using that endpoint URL. For example:
```
curl https://<restapiid>.execute-api.us-east-1.amazonaws.com/Prod/hello/
```
After successfully deploying your application, you see output like the following:
```
 {"message": "hello world"}
```

If you see that message you've then succesfully uploaded your file to the AWS cloud.

## Critical files
```
template.yaml: Contains the AWS SAM template that defines your application's AWS resources.

hello_world/app.py: Contains your actual Lambda handler logic.

hello_world/requirements.txt: Contains any Python dependencies that the application requires, and is used for sam build.
```
# SAM Packaging
This command creates a .zip file of your code and dependencies, and uploads the file to Amazon Simple Storage Service (Amazon S3). AWS SAM enables encryption for all files stored in Amazon S3. It then returns a copy of your AWS SAM template, replacing references to local artifacts with the Amazon S3 location where the command uploaded the artifacts.

Create an S3 bucket on AWS console to link with your project.

We can use the following command:
sam package [OPTIONS] [ARGS]

I replaced ```[OPTIONS] [ARGS]``` with ```-t``` followed by the path where my AWS SAM template is located, as well as ```--s3-bucket``` followed by the name of the S3 created on my AWS console, ```--output-template-file``` followed by the path to the file where the command writes the packaged template. 

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
python-demo$ pip install -r tests/requirements.txt --user
# unit test
python-demo$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
python-demo$ AWS_SAM_STACK_NAME=<stack-name> python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name python-demo
```

## Article
This is an accompanying code repository of the following article:

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-package.html
