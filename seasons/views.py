import pandas as pd
from datetime import datetime
from django.shortcuts import render

# Create your views here.
SEASONS = {
    'Spring': {
        'start': datetime(month=3, day=19),
        'end': datetime(month=6, day=19),
    },
    'Summer': {
        'start': datetime(month=6, day=20),
        'end': datetime(month=9, day=21),
    },
    'Fall': {
        'start': datetime(month=9, day=22),
        'end': datetime(month=12, day=20),
    },
    'Winter': {
        'start': datetime(month=12, day=21),
        'end': datetime(month=3, day=18),
    },
}


def str_2_date(str_date):
    """
    Convert a date_string to date type
    :param str_date: String date
    :return (datetime): Datetime object
    """
    str_format = "%-m/%-d/%y"
    return datetime.strptime(str_date, str_format)


def set_season(date_obj):
    """
    Select season for given date
    :param date_obj (datetime): datetime object
    :return (str): Season string
    """
    date_year = date_obj.year

    for key, val in SEASONS.items():
        start = datetime(year=date_year, month=val['start'].month, day=val['start'].day)
        if key != 'Winter':
            end = datetime(year=date_year, month=val['end'].month, day=val['end'].day)
        else:
            end = datetime(year=date_year + 1, month=val['end'].month, day=val['end'].day)

        if start <= date_obj <= end:
            return key


def gen_dataset():
    """
    Generate sample dataset
    :return (dataframe): Pandas dataframe containing data to anallyze
    """
    data = {
        'ORD_ID': ['113-89098966940269', '114-0291773-7262677', '114--0291773--7262697', '114-9900513-7761000',
                   '112-5230502-8173028', '112-7714081-3300254', '114-5384551-1465853', '114-7232801-4607440'],
        'ORD_DT': ['9/23/19', '1/1/20', '12/5/19', '9/24/20', '1/30/20', '5/2/20', '4/2/20', '10/9/20'],
        'QT_ORDD': [1, 1, 1, 1, 1, 1, 1, 1],
    }

    return pd.DataFrame(data=data)


def get_result(dataset=None):
    if dataset is None:
        data = gen_dataset()
    else:
        data = pd.DataFrame(data=dataset)

    data['SEASON'] = data.apply(lambda x: set_season(str_2_date(x['ORD_DT'])), axis=1)

    data.drop('ORD_DT', axis=1, inplace=True)
    data.drop('QT_ORDD', axis=1, inplace=True)

    return data.to_dict('records')

