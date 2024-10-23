"""

A Snowpark Python model run through dbt to show how to add the Prophet library 
to the serverless Python runtime.

The business logic is trivial, as the code is only used to generate some 
"napkin math" numbers to compare the iteration time of this Python runtime
with other options for data practitioners.

"""


from importlib.metadata import version


def model(dbt, session):
    dbt.config(
        # note that Python models can only be tables
        materialized = "table", 
        # packages = ['holidays==0.18','prophet']
    )
    my_sql_model_df = dbt.ref("retrieve_columns")
    # debug print!
    print("I am a python model")

    # UN-COMMENT HERE AND THE PACKAGES ABOVE TO RUN WITH PROPHET 
    
    # import prophet
    # v =  version('prophet') 
    # assert v == '1.1.5'

    return my_sql_model_df