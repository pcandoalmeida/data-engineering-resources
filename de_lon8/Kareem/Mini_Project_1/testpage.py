import codetest
from unittest.mock import Mock
from unittest.mock import patch

#Checking if my input patch works.
@patch('builtins.input')
def test_createNew(mock_input):
    mock_input.return_value = 'fanta'

    result = codetest.createNew()

    assert(result == 'fanta')
    assert mock_input.call_count == 1

#Checking the patch works with capital letters. 
@patch('builtins.input')
def test_createNew_caps(mock_input):
    mock_input.return_value = 'ceREAl'

    result = codetest.createNew()

    assert(result == 'cereal')
    assert mock_input.call_count == 1

#Making sure that the patch cannot be empty
@patch('builtins.input')
def test_createNew_none(mock_input):
    mock_input.return_value = ''

    result = codetest.createNew()

    assert(result != '')
    assert mock_input.call_count == 1
