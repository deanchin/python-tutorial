''' Day 23 Example code '''

SAMPLE_DICT = {
    "name": "Dean"
}


def func_one():
    try:
        return SAMPLE_DICT['names']

    except KeyError as kerr:
        print(f'Got an KeyError exception {kerr}')
        return None

    except ValueError as verr:
        print(f'Got an Value error exception {verr}')
        return None

    finally:
        print('Closing database connection')


print(func_one())

row = input('Give me row: ')
# col = input('Give me col: ')

# if not row.isdigit():
#     print('This is not an integer')

try:
    print(float(row))
except ValueError:
    print(f'{row} is not a valid number')
