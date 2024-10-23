"""

A simple Python DAG to show how to add the Prophet library to a Bauplan model, 
i.e. using a decorator to define the Python environment "as code".

The code is used to get some "napkin math" numbers to compare iteration time with
other "serverless" Python runtimes.

NOTE: you need access to a Bauplan environment to run this code. Please get in touch
through the information in the README.

"""

import bauplan


@bauplan.model()
@bauplan.python('3.11')
def retrieve_columns(
    # input is a lakehouse (Iceberg) table, abstracted away by the platform
    data=bauplan.Model('titanic',
        # column push down
        columns=[
            'Age',
            'Fare',
            'PassengerId',
            'Pclass',
            'Embarked',
            'Sex',
        ],
        # filter push down
        filter='Age > 1'
    )
):
    # inspect the input data, which is a PyArrow table
    print(f"Input dataset has {data.num_rows} rows.")
    # return a dataframe-like object, in this case a PyArrow table
    return data


@bauplan.model()
# declare the prophet dependency here
@bauplan.python('3.11', pip={'prophet': '1.1.5'})
def try_out_prophet(
    # input follows the naming convention of using the previous function name
    data=bauplan.Model('retrieve_columns')
):
    # data is a PyArrow table
    print(f"Input dataset has {data.num_rows} rows.")
    
    # function-specific code here
    import prophet
    from importlib.metadata import version
    
    # print and verify prophet version
    print(f"Prophet version: {version('prophet')}")
    assert version('prophet') == '1.1.5'
    
    return data

