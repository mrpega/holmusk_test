#from main import Reader
from ..reader import Reader
import pytest
import pandas as pd

@pytest.fixture
def mock_person_table():
    mock_person_table_data = pd.read_csv('tests/mock_person_table.csv')
    return mock_person_table_data

# # these tests are only applicable if we have access to database:
# def test_query_data_with_limit_1():
#     read_obj = Reader()
#     query = "select * from cdm_schema.person LIMIT 1"

#     res_df = read_obj.query_data(None,query)
#     assert res_df.shape[0] == 1

# def test_get_person_with_known_id():
#     read_obj = Reader()

#     res_df = read_obj.get_person(None, [1, 123, 456])
#     assert res_df.shape[0] == 1

# def test_get_person_with_unknown_id():
#     read_obj = Reader()

#     res_df = read_obj.get_person(None, [999, 888])
#     assert res_df.shape[0] == 0

def test_get_person_with_empty_list(mocker):
    read_obj = Reader()

    # create mocked database connection
    mocker.patch('psycopg2.connect', return_value = None)

    # make sure that it's throwing value error
    with pytest.raises(ValueError):
        res_df = read_obj.get_person(None, [])


# test with mock data - in the absent of database connection, which is likely in the case of test env.
def test_get_person_with_mock_data(mocker, mock_person_table):
    read_obj = Reader()

    # create mocked database connection
    mocker.patch('psycopg2.connect', return_value = None)
    
    # create mocked data table
    mocker.patch('pandas.io.sql.read_sql_query', return_value = mock_person_table)
    res_df = read_obj.get_person(None, [1, 123, 456])
    assert res_df.shape[0] == 1
