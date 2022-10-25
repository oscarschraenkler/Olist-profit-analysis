import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        csv_path = os.path.dirname(os.path.dirname(__file__))
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your username
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        file_names = os.listdir(os.path.join(csv_path, 'data/csv/'))

        file_names = [csv for csv in file_names if csv.endswith('.csv')]
        key_names = [x.replace("_dataset.csv","").replace(".csv","").replace("olist_","") for x in file_names]
        values = [pd.read_csv(os.path.join(csv_path, f'data/csv/{x}')) for x in file_names]
        data = {}

        for k,v in zip(key_names, values):
            data[k] = v

        return data


    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")

# lst=Olist()
# print(lst.get_data())
