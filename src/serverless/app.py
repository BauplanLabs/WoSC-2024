import time
import uuid



def lambda_handler(event, context):
    start = time.time()
    v = None
    from importlib.metadata import version
    
    # UN-COMMENT HERE IF YOU HAVE INSTALLED PROPHET 
    # IN THE DOCKER FOR THE LAMBDA!
    
    # import prophet
    # v =  version('prophet') 
    # assert v == '1.1.5'
    
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