import pandas as pd
import re


class DataLoader(object):
    def __init__(self):
        self.dataset = None
        self.dataset = pd.set_option('mode.chained_assignment', None)

    def fit(self, dataset):
        self.dataset = dataset.copy()

    # apply regex
    def get_title(self, name):
        pattern = ' ([A-Za-z]+)\.'
        title_search = re.search(pattern, name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""

    def load_data(self):
        columns_to_convert = ['hypertension', 'heart_disease', 'stroke']
        self.dataset[columns_to_convert] = self.dataset[columns_to_convert].astype(str)
        self.dataset['stroke'] = self.dataset['stroke'].astype(int)

        self.dataset.drop('id', axis=1, inplace=True)
        self.dataset.drop('Residence_type', axis=1, inplace=True)
        self.dataset.drop('work_type', axis=1, inplace=True)

        self.dataset["bmi"].fillna(self.dataset["bmi"].mean(), inplace=True)

        self.dataset['smoking_status'].replace({'Unknown': 0, 'never smoked': -1, 'formerly smoked': 1, 'smokes': 2}, inplace=True)
        self.dataset['gender'].replace({'Other': 'Female'}, inplace=True)
        self.dataset['gender'].replace({'Male': 1, 'Female': 0}, inplace=True)

        self.dataset['ever_married'].replace({'Yes': 1, 'No': 0}, inplace=True)

        return self.dataset
