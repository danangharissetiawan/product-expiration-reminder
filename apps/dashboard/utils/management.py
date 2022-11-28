import datetime


def get_expiry_date():
    today = datetime.date.today()
    expiry_date = today + datetime.timedelta(days=365)
    return expiry_date


def label_expiry_date(expiry_date):
    today = datetime.date.today()
    delta = expiry_date - today
    if 7 >= delta.days > 0:
        return 'W'
    elif delta.days > 7:
        return 'S'
    else:
        return 'D'