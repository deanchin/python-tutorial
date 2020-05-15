''' Zipcode '''


def is_zipcode(zipcode):
    ''' my function '''
    if not isinstance(zipcode, str):
        return False

    if len(zipcode) == 5:
        if not zipcode.isdigit():
            return False
        return True
    return False
