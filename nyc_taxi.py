if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

      # Remove rows where passenger_count is  0 and trip_distance is  0
    df = data[(data['passenger_count'] !=  0) & (data['trip_distance'] !=  0)]

     # Convert lpep_pickup_datetime to date and create a new column lpep_pickup_date
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date

    
    # Assuming df is your DataFrame
    df.columns = df.columns.str.replace('(?<=[a-z])(?=[A-Z])', '_').str.lower()

    return df


@test
def test_output(output, *args) -> None:
    # Assuming output is a pandas DataFrame
    df = output

    # Assertion   1: Check if vendor_id is either   1 or   2
    assert df['vendor_id'].isin([1,   2]).all(), "vendor_id must be either   1 or   2."

    # Assertion   2: Ensure passenger_count is greater than   0
    assert df['passenger_count'].min() >   0, "All passenger counts must be greater than   0."

    # Assertion   3: Verify trip_distance is greater than   0
    assert df['trip_distance'].min() >   0, "All trip distances must be greater than   0."