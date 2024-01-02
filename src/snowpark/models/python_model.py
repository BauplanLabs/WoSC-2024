from importlib.metadata import version


def model(dbt, session):
    dbt.config(
        materialized = "table", # Python models can only be tables
        #packages = ['holidays==0.18','prophet']
    )
    my_sql_model_df = dbt.ref("retrieve_columns")
    print("I am a python model")

    # UN-COMMENT HERE AND THE PACKAGES ABOVE TO RUN WITH PROPHET 
    
    #import prophet
    # v =  version('prophet') 
    #assert v == '1.1.5'

    return my_sql_model_df