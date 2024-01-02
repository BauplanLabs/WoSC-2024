"""

Vanilla script to invoke the Lambda function, print out the response, and exit.
We time the invocation, so we can see how long it takes.


Note that the script expects an additional argument, the name of the Lambda function; also
AWS credentials are read by boto3 in the usual way (it looks for ~/.aws/credentials first, then
environment variables): make sure to supply these.

"""

import boto3
import json
# we setup the client before the function, so that it does not add
# to the invocation time
lambda_client = boto3.client('lambda', region_name='us-east-1')


def invoke_my_lambda(lambda_function_name: str):
    response = lambda_client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=b'{}' # needs to be bytes
    )
    return json.loads(response['Payload'].read().decode("utf-8"))


if __name__ == '__main__':
    import sys
    import time
    # make sure we have the right number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 client.py <lambda_function_name>")
        sys.exit(1)

    start_time = time.time()
    r = invoke_my_lambda(sys.argv[1])
    end_time = time.time()
    print(f"Response: {r}")
    print(f"Time: {end_time - start_time} seconds")






