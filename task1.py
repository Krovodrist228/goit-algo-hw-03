import datetime


def get_days_from_today(date):
    while True:
        try:
            date_format = datetime.datetime.strptime(date, "%Y-%m-%d")
            break
        except:
            print('Enter in a YYYY-MM-DD format')
            date = input()
            continue

    now = datetime.datetime.now()

    difference = now.toordinal() - date_format.toordinal()
    
    return difference



print(f'Days from today: {get_days_from_today(input('Enter date in a YYYY-MM-DD format: '))}')