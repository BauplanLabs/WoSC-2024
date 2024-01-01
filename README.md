# Sigmod Demonstration 2024

This repo contains code snippets and details to reproduce the results on our demonstration paper at SIGMOD 2024.

Last Update: Jan 2024.

## Overview

TBC

## Projects

### Aws Lambda + Docker


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