# Sigmod Demonstration 2024

This repo contains code snippets and details to reproduce the baseline numbers in our demonstration paper at SIGMOD 2024.

Last Update: Jan 2024.

## Overview

TBC

Note that the numbers we care about are _iteration_ numbers, not startup / building numbers, so for example the AWS + Docker setup does not consider the fact that the Python Docker image needs to be built and the Lambda function needs to be created before even iterating on packages (i.e. installing _Propeth_).Nonetheless, the difference in the feedback loop when compared with the proposed solution is still significant.

Note that we also don't care about the actual coding logic, so the Python functions we are running are just checking the right package is installed, i.e.:

```python
v =  version('prophet') 
assert v == '1.1.5'
```

### Testing setup

All napking numbers are reported running the code snippets below from New York City, with a ~100 Mbps available bandwith (as checked with [fast](https://fast.com/it/) before running), `us-east-1` as the target region, and a `Apple M2 Max 2023` laptop.

## Projects

### Aws Lambda + Docker

#### Pre-requisites

We assume you have a working AWS account, the [serverless framework](https://www.serverless.com/framework/) and Docker installed.

#### How to run

Deploy an vanilla Python Lambda function using the serverless framework:

```bash
cd serverless
serverless deploy
```

At the end of the first deployment, the terminal should print out the name of the lambda just created, e.g. `prophet-lambda-napkin-paper-dev-prophetrunner`. To test the function, run the following command (in a virtualenv with the `boto3`, or your global environment):

```bash
python3 client.py prophet-lambda-napkin-paper-dev-prophetrunner
```

To test an iteration loop, uncomment the `RUN pip install prophet==1.1.5` in the Dockerfile, comment out the relevant sections in `app.py` and re-deploy:

```bash
serverless deploy
```

Note that:

* the `re-build container` number in the paper is the packaging time in serverless CLI (time to build locally and upload to ECR);
* the `re-run function` number in the paper is the sum of the time to update Cloud Formation after ECR is updated and the time to run the function and get a result back with the client script (cold start).

### Snowflake (Snowpark)


### Bauplan

#### Pre-requisites

A working Bauplan account and a link to the private Alpha environment is required to run the code in this section. Please contact us if you wish to try out Bauplan.

#### How to run

Assuming you have Bauplan credentials for the Alpha environment, make sure you're running the latest version of the CLI (in your target virtualenv or in your global environment):

```bash
pip install bauplan --upgrade
```

Cd into the `bauplan/sigmod` directory and run the following command:

```bash
bauplan run
```

You can comment in / out the relevant sections in `models.py` to test the Prophet installation, or try out other packages for more experiments.