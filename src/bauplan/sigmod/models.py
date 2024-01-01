"""

A simple Python model to try out Bauplan with the Prophet library, and
get some baseline numbers ("napkin math") to compare iteration time with
Python runtimes compared to other standard toolchains.

"""

import bauplan


@bauplan.model(columns=['*'])
@bauplan.python('3.11', pip={'prophet': '1.1.5'})
def try_out_prophet(
    data=bauplan.Model(
        'retrieve_columns',
        columns=['*']
    )
):
    import prophet
    from importlib.metadata import version
    
    # verify prophet version
    assert version('prophet') == '1.1.5'
    
    return data

