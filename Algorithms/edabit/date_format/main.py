# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

def format_date(date):
    new_date = date.split('/')

    result = ''.join(new_date[::-1])

    return result
