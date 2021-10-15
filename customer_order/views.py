import pandas as pd
from django.shortcuts import render

# Create your views here.
def gen_dataset():
    """
    Generate sample dataset
    :return (dataframe): Pandas dataframe containing data to analyze
    """
    data = {
        'order_number': ['ORD_1567', 'ORD_1567', 'ORD_1567', 'ORD_1234', 'ORD_1234', 'ORD_1234', 'ORD_9834', 'ORD_9834',
                         'ORD_7654', 'ORD_7654'],
        'item_name': ['LAPTOP', 'MOUSE', 'KEYBOARD', 'GAME', 'BOOK', 'BOOK', 'SHIRT', 'PANTS', 'TV', 'DVD'],
        'status': ['SHIPPED', 'SHIPPED', 'PENDING', 'SHIPPED', 'CANCELLED', 'CANCELLED', 'SHIPPED', 'CANCELLED',
                   'CANCELLED', 'CANCELLED'],
    }

    return pd.DataFrame(data=data)


def get_uniqueorders(dataframe):
    """
    Get values for unique values order_number
    :param dataframe: Dataframe to analize
    :return (List): List with unique values
    """
    uniqueValues = dataframe['order_number'].unique()

    return uniqueValues


def define_status(dataset):
    """
    Check for status in order and return row
    :param dataset (dataset): filtered dataset to generate status
    :return: dict with results
    """
    order_num = dataset['order_number'].iloc[0]

    counts = dataset['status'].value_counts()

    if (counts.min() == counts.max()) and (counts.min() + counts.max() != len(dataset)):
        return {'order_number': order_num, 'status': dataset['status'].iloc[0]}
    else:
        if dataset.status.isin(['PENDING']).any().any():
            return {'order_number': order_num, 'status': 'PENDING'}
        elif dataset.status.isin(['SHIPPED']).any().any():
            return {'order_number': order_num, 'status': 'SHIPPED'}
        else:
            return {'order_number': order_num, 'status': 'NA'}

def get_result(dataset=None):
    """
    Analize data and return a list containing results as dict
    :param dataset (DataFrame): DataFrame containing info about orders
    :return (List): List containing records like dicts
    """
    if dataset is None:
        data = gen_dataset()
    else:
        data = pd.DataFrame(data=dataset)

    unique_orders = get_uniqueorders(data)

    res = []
    for order in unique_orders:
        filter = data.order_number == order
        filtered_df = data[filter]
        status = define_status(filtered_df)
        res.append(status)

    return res


