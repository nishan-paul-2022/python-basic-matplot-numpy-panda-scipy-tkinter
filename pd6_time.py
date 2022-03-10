from datetime import datetime
import pandas as pd


def fst():
    x = datetime.now()
    print('fst', x.month, x.year)


def sec():
    ts = pd.Timestamp(year=2011, month=11, day=21, hour=10, second=49, tz='US/Central')
    print('sec', ts)


def thrd():
    data = pd.date_range('1/1/2011', periods=10, freq='D')
    print('thrd', data)


def frth():
    rng = pd.DataFrame()
    rng['date'] = pd.date_range('1/1/2011', periods=72, freq='H')
    print('frth', rng[:5])

    rng['year'] = rng['date'].dt.year
    rng['month'] = rng['date'].dt.month
    rng['day'] = rng['date'].dt.day
    rng['hour'] = rng['date'].dt.hour
    rng['minute'] = rng['date'].dt.minute
    print('frth', rng)


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()


# https://www.geeksforgeeks.org/python-pandas-tseries-offsets-dateoffset/
# https://www.geeksforgeeks.org/python-working-with-date-and-time-using-pandas/