import codetest
from unittest.mock import Mock
from unittest.mock import patch

#TESTS FOR PERSISTING DATA
#***********************************************
#CHECK TO SEE IF THE FILE IS OPENING
#CHECK TO SEE IF THE FILE CLOSES
#CHECK TO SEE IF THE DATA HAS BEEN STORED PROPERLY
#CHECK IF IT DOESNT OPEN 



#TESTS FOR CREATING SOMETHING TO PUT INTO A LIST
#***********************************************
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

#Making sure that the inputs are a string. 
@patch('builtins.input')
def test_createNew_string(mock_input):
    mock_input.return_value = 'coke'

    result = codetest.createNew()

    assert (isinstance(result, str))
    assert mock_input.call_count == 1


#TEST TO ADD SOMETHING TO A LIST
#*******************************************
'''The append functoin is called here and therefore does not need
testing for it as it is called in a single line.'''

#TEST TO VIEW ALL PRODUCTS
#******************************************
'''This can be done in a nicer way later but it is not a core requirment at this stage'''




