"""

Vanilla script for AWS Lambda function, deployed using the serverless framework
(see the options in the serverless.yml file).

The business logic is trivial - you can uncomment the import prophet line to test
the system with the Prophet library. The code is used to get some "napkin math" numbers
as a benchmark for the iteration time of this Python runtime compared to other
options for data practitioners.

"""

import time
import uuid



def lambda_handler(event, context):
    start = time.time()
    v = None
    try:
        import prophet
        from importlib.metadata import version
        v =  version('prophet') 
        assert v == '1.1.5'
    except ImportError:
        print("Prophet not installed.")
    
    # debug print - this will appear in cloudwatch logs
    print("All done!")

    return {
        "metadata": {
            "timeMs": int((time.time() - start) * 1000.0),
            "epochMs": int(time.time() * 1000),
            "eventId": str(uuid.uuid4()),
        },
        "data": {
            "version": v
        }
    }