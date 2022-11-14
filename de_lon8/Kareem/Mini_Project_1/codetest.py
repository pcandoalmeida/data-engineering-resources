def createNew():
    new_addition = input('')
    new_addition = new_addition.lower()
    if new_addition == '':
        print('You cannot have an empty value.')
    else:
        return new_addition

