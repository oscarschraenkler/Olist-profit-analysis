import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist


class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()

    def get_wait_time(self, is_delivered=True):
        """
        Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        and filters out non-delivered orders unless specified
        """
        # Hint: Within this instance method, you have access to the instance of the class Order in the variable self, as well as all its attributes
        df = self.data['orders'].copy()
        df[['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']] = df[['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']].apply(pd.to_datetime)
        df = df.query('order_status == "delivered"')
        df['wait_time'] = (df['order_delivered_customer_date']-df['order_purchase_timestamp']).dt.days
        df['expected_wait_time'] = (df['order_estimated_delivery_date']-df['order_purchase_timestamp']).dt.days
        df['delay_vs_expected'] = (df['wait_time']-df['expected_wait_time'])
        return df[['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected', 'order_status']]

    def get_review_score(self):
        """
        Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        df = self.data['order_reviews'].copy()
        df['dim_is_five_star']=df['review_score'].apply(lambda x: 1 if x == 5 else 0)
        df['dim_is_one_star']=df['review_score'].apply(lambda x: 1 if x == 1 else 0)
        return df[['order_id', 'dim_is_five_star', 'dim_is_one_star', 'review_score']]

    def get_number_products(self):
        """
        Returns a DataFrame with:
        order_id, number_of_products
        """
        df = self.data['order_items'].copy()
        df = df.groupby('order_id').count().reset_index()
        df['number_of_products'] = df['product_id']
        return df[['order_id','number_of_products']]

    def get_number_sellers(self):
        """
        Returns a DataFrame with:
        order_id, number_of_sellers
        """
        df = self.data['order_items'].copy()
        df = df.groupby('order_id').nunique().reset_index()
        df['number_of_sellers'] = df['seller_id']
        return df[['order_id','number_of_sellers']]

    def get_price_and_freight(self):
        """
        Returns a DataFrame with:
        order_id, price, freight_value
        """
        df = self.data['order_items'].copy()
        df = df[['order_id', 'price', 'freight_value']]
        return df.groupby('order_id').sum().reset_index()

    # Optional
    def get_distance_seller_customer(self):
        """
        Returns a DataFrame with:
        order_id, distance_seller_customer
        """
        pass  # YOUR CODE HERE

    def get_training_data(self,
                          is_delivered=True,
                          with_distance_seller_customer=False):
        """
        Returns a clean DataFrame (without NaN), with the all following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_products', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """
        # Hint: make sure to re-use your instance methods defined above
        df = Order().get_wait_time().merge((Order().get_number_sellers()),on='order_id').merge((Order().get_review_score()),on='order_id').merge((Order().get_number_products()),on='order_id').merge((Order().get_price_and_freight()),on='order_id')
        return df.dropna()
