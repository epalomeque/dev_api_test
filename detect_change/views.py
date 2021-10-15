import pandas as pd
from django.shortcuts import render


# Create your views here.
def gen_dataset():
    """
    Generate sample dataset
    :return (dataframe): Pandas dataframe containing data to anallyze
    """
    data = {
        'dates': ['01/01/20', '01/02/20', '01/03/20', '01/04/20', '01/05/20', '01/06/20', '01/07/20', '01/08/20',
                  '01/09/20', '01/10/20'],
        'was_rainy': [False, True, True, False, False, True, False, True, True, True]
    }

    return pd.DataFrame(data=data)


def get_result(dataset=None):
    """
    Analize data and return a dict containing results
    :param dataset (DataFrame): DataFrame containing info about weather
    :return (Dict): Dict containing dates and change data
    """
    if dataset is None:
        data = gen_dataset()
    else:
        data = pd.DataFrame(data=dataset)

    data["is_change"] = data["was_rainy"].shift(1, fill_value=data["was_rainy"].head(1)) != data["was_rainy"]

    data_filter = data["was_rainy"] and data["is_change"]

    new_data = data.loc[data_filter]
    new_data.drop("is_change", axis=1, inplace=True)

    return new_data.to_dict('records')
