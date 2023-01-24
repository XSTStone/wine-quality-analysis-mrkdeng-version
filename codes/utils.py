import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols,glm

def plt_show(type, wine):
    if type == 'white':
        white_wine=wine.loc[wine['type']=='White', 'quality']
        sns.set_style("whitegrid")
        print(sns.histplot(white_wine,kde=True,color="black",label="white wine", stat="density"))
        plt.xlabel("Quality Score")
        plt.ylabel("Density")
        plt.title("Distribution of Quality of White Wine")
        plt.legend()
        plt.show()
    elif type == 'red':
        red_wine = wine.loc[wine['type'] == 'Red', 'quality']
        sns.set_style("whitegrid")
        print(sns.histplot(red_wine, kde=True, color="red", label="red wine", stat="density"))
        plt.xlabel("Quality Score")
        plt.ylabel("Density")
        plt.title("Distribution of Quality of Red Wine")
        plt.legend()
        plt.show()
    elif type == 'both':
        red_wine = wine.loc[wine['type'] == 'Red', 'quality']
        white_wine = wine.loc[wine['type'] == 'White', 'quality']
        sns.set_style("whitegrid")
        print(sns.histplot(red_wine, kde=True, color="red", label="red wine", stat="density"))
        print(sns.histplot(white_wine, kde=True, color="black", label="white wine", stat="density"))
        plt.xlabel("Quality Score")
        plt.ylabel("Density")
        plt.title("Distribution of Quality by Wine Type")
        plt.legend()
        plt.show()


def take_sample(data_frame, replace=False, n=200):
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
