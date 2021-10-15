import pandas as pd
from datetime import datetime
from django.shortcuts import render

# Create your views here.
SEASONS = {
    'Spring': {
        'start': {'month': 3, 'day': 19},
        'end': {'month': 6, 'day': 19},
    },
    'Summer': {
        'start': {'month': 6, 'day': 20},
        'end': {'month': 9, 'day': 21},
    },
    'Fall': {
        'start': {'month': 9, 'day': 22},
        'end': {'month': 12, 'day': 20},
    },
    'Winter': {
        'start': {'month': 12, 'day': 21},
        'end': {'month': 3, 'day': 18},
    },
}


def str_2_date(str_date):
    """
    Convert a date_string to date type
    :param str_date: String date
    :return (datetime): Datetime object
    """
    str_format = "%m/%d/%y"
    return datetime.strptime(str_date, str_format)


def set_season(date_obj):
    """
    Select season for given date
    :param date_obj (datetime): datetime object
    :return (str): Season string
    """
    date_year = date_obj.year

    for key, val in SEASONS.items():
        start = datetime(year=date_year, month=val['start']['month'], day=val['start']['day'])
        end = datetime(year=date_year, month=val['end']['month'], day=val['end']['day'])
        if key == 'Winter':
            start_year = date_year - 1 if date_obj.month in [1, 2, 3] else date_year
            end_year = date_year + 1 if date_obj.month == 12 else date_year
            start = datetime(year=start_year, month=val['start']['month'], day=val['start']['day'])
            end = datetime(year=end_year, month=val['end']['month'], day=val['end']['day'])

        if start <= date_obj <= end:
            return key


def gen_dataset():
    """
    Generate sample dataset
    :return (dataframe): Pandas dataframe containing data to anallyze
    """
    data = {
        'ORD_ID': ['113-8909896-6940269', '114-0291773-7262677', '114-0291773-7262697', '114-9900513-7761000',
                   '112-5230502-8173028', '112-7714081-3300254', '114-5384551-1465853', '114-7232801-4607440'],
        'ORD_DT': ['9/23/19', '1/1/20', '12/5/19', '9/24/20', '1/30/20', '5/2/20', '4/2/20', '10/9/20'],
        'QT_ORDD': [1, 1, 1, 1, 1, 1, 1, 1],
    }

    return pd.DataFrame(data=data)


def get_result(dataset=None):
    """
    Analize data and return a dict containing results
    :param dataset (DataFrame): DataFrame containing info about order dates
    :return (Dict): Dict containing records with seasons
    """
    if dataset is None:
        data = gen_dataset()
    else:
        data = pd.DataFrame(data=dataset)

    data['SEASON'] = data.apply(lambda x: set_season(str_2_date(x['ORD_DT'])), axis=1)

    data.drop('ORD_DT', axis=1, inplace=True)
    data.drop('QT_ORDD', axis=1, inplace=True)

    return data.to_dict('records')

