# WoSC10 benchmarks (ACM Middleware 2024)

This repo contains code snippets to reproduce the baseline numbers in the paper `Bauplan: Zero-copy, Scale-up FaaS for Data Pipelines`, published at the 10th International Workshop on Serverless Computing ([WoSC10](https://www.serverlesscomputing.org/wosc10/papers)), part of ACM Middleware 2024.

Quick links:

* paper pre-print on [arxiv](https://arxiv.org/abs/2410.17465)
* camera-ready paper on ACM Digital Library (coming soon!)
* [bauplan website](https://www.bauplanlabs.com/)

Paper authors:

* [Jacopo Tagliabue](https://jacopotagliabue.it/)
* [Tyler R. Caraza-Harter](https://tyler.caraza-harter.com/)
* [Ciro Greco](https://www.linkedin.com/in/cirogreco/)

Last code update: February 2024.

## Overview

This repo contains Bauplan, AWS Lambda (with Docker) and Snowpark (plus dbt) code snippets to reproduce the numbers in Table 2 $$the paper. The goal is to show the difference in feedback loop time when iterating on a data pipeline with a _new_ package dependency: in other words, we care about are _iteration_ numbers, not startup / building numbers. For example the Lambda setup does not consider the fact that the Docker image and the function need to be created before even iterating on packages. While exact numbers may differ based on the specific setup, Python version, package, platform evolution, the ``napkin math'' difference should be consistent across different setups.

For more details on the use cases, the industry motivation and the background assumptions, please refer to our [paper](https://arxiv.org/abs/2410.17465).

### Testing setup

All numbers are reported running the snippets below from New York City, with a ~100 Mbps available bandwith (as checked with [fast](https://fast.com/it/) before running), `us-east-1` as the target region, and a `Apple M2 Max 2023` laptop.

## Projects

### Aws Lambda + Docker

#### Pre-requisites

We assume you have a working AWS account, the [serverless framework](https://www.serverless.com/framework/) and Docker installed.

#### How to run

Deploy a vanilla Lambda function using the serverless framework:

```bash
cd aws_lambda_with_serverless
serverless deploy
```

At the end of the first deployment, the terminal should print out the name of the lambda just created, e.g. `prophet-lambda-paper-dev-prophetrunner`. To test the function with the provided client script, run the following command (in a virtualenv with the `boto3`, or your global environment):

```bash
python3 client.py prophet-lambda-paper-dev-prophetrunner
```

To test the iteration loop, uncomment the `RUN pip install prophet==1.1.5` in the Dockerfile, comment out the relevant sections in `app.py` and re-deploy:

```bash
serverless deploy
```

Note that in the paper we list:

* the `re-build container` number as the packaging time in the CLI to build locally and upload to ECR;
* the `re-run function` number as the time to update Cloud Formation and re-run the function with the client script.

### Snowflake + dbt

#### Pre-requisites

We assume you have a working Snowflake account and [dbt](https://docs.getdbt.com/) installed in your target environment (e.g. `python3 -m pip install dbt-snowflake`): we also assume you have configured your dbt profile correctly to connect to Snowflake. Please note that you need to enable [Anaconda in your Snowflake account](https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-packages#using-third-party-packages-from-anaconda) to have third-party libraries installed.

We will be using Snowflake standard TPC as a the first query in a SQL + Python DAG, which will be isomorphic to the Bauplan DAG (one node to retrieve columns first, one to install the data science package).

#### How to run

You can run a baseline test to check that the setup is working correctly:

```bash
cd snowpark
dbt run
```

You should find a new `PYTHON_MODEL` table in the target Snowflake database. To test an iteration loop, uncomment the relevant lines in `python_model.py` and re-run dbt with `dbt run`.

### Bauplan

#### Pre-requisites

A working Bauplan account for the private Beta is required to run the code in this section. Please [contact us](https://www.linkedin.com/in/jacopotagliabue/) if you wish to try out Bauplan.

#### How to run

Assuming you have Bauplan credentials, install the latest version of the library:

```bash
pip install bauplan --upgrade
```

Cd into the `bauplan/wosc` directory and run:

```bash
bauplan run
```

You can comment in / out the relevant sections in `models.py` to test the Prophet installation, or try out other packages for more experiments. Re-running a second time (i.e. removing and adding again Prophet) with the same dependencies will hit the container cache, resulting in basically 0 seconds spent on re-installation.
