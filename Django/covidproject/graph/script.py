import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib import style

import urllib.request
import json

from pathlib import Path
import os

import warnings
warnings.filterwarnings("ignore")

url = "https://api.covid19india.org/states_daily.json"
# from graph import models

def make_data():
    with open('data.json') as f:
        data = json.load(f)
    data = data['states_daily']
    df = pd.json_normalize(data)
    return df

def create_pie_chart(df, dir):
    df_pie = df[['status', 'tt']]
    df_pie['tt'] = pd.to_numeric(df_pie['tt'])
    pie_data = []
    for i in df['status'].unique():
        pie_data.append(df_pie[df_pie['status'] == i]['tt'].sum())
    pie_data[0] = pie_data[0] - (pie_data[1] + pie_data[2])
    plt.clf()
    cmap = plt.get_cmap('tab10')
    my_colors = cmap(np.array([1, 2, 3]))
    plt.pie(pie_data, labels = df['status'].unique(), autopct = "%.2f%%",
            radius = 1.3, shadow = True, startangle = 180,
            colors = my_colors, wedgeprops = dict(width = 0.4), pctdistance = 0.5);
    path = os.path.join(dir, 'images')
    plt.savefig(os.path.join(path, 'pie.png'))

def create_line_chart(df, dir):
    df_ = df.copy(deep = True)
    df_['date'] = pd.to_datetime(df_['date'])
    df_ = df_[['date', 'status', 'tt']]
    df_['Cases'] = pd.to_numeric(df_['tt'])
    cmap = plt.get_cmap('tab10')
    my_colors = cmap(np.array([1, 2, 3]))
    plt.clf()
    fig = plt.gcf()
    fig.set_size_inches(15, 6)
    svm = sns.lineplot('date', 'Cases', data = df_,
                 hue = 'status',
                 palette = {'Confirmed':my_colors[0], 'Recovered':my_colors[1], 'Deceased':my_colors[2]});
    path = os.path.join(dir, 'images')
    figure = svm.get_figure()
    figure.savefig(os.path.join(path, 'area.png'))
    plt.xticks(rotation = 45);

def create_dataset(df):
    df_bar = df.tail(3)
    df_bar.set_index('status', inplace = True)
    df_bar.drop('date', axis = 1, inplace = True)
    df_bar.drop('tt', axis = 1, inplace = True)
    df_bar = df_bar.apply(pd.to_numeric)
    df_bar = df_bar.T
    return df_bar

def overall_info(df):
    df_states = df.copy(deep = True)
    df_states['date'] = pd.to_datetime(df_states['date'])
    df_states.drop('tt', axis = 1, inplace = True)
    ########## ALL States Confirmed Data #############################
    df_C = df_states[df_states['status'] == 'Confirmed'].copy(deep = True)
    df_C.drop('status', axis = 1, inplace = True)
    df_MC = pd.melt(df_C, id_vars = 'date', value_vars = list(df_C.columns).remove('date'),
                var_name = 'state', value_name = 'Confirmed')
    df_MC['Confirmed'] = pd.to_numeric(df_MC['Confirmed'])
    df_MC.drop('date', axis = 1, inplace = True)
    df_MC = df_MC.groupby('state').sum()
    df_MC = df_MC['Confirmed']
    ##################################################################
    ########## ALL States Recovered Data #############################
    df_R = df_states[df_states['status'] == 'Recovered'].copy(deep = True)
    df_R.drop('status', axis = 1, inplace = True)
    df_MR = pd.melt(df_R, id_vars = 'date', value_vars = list(df_R.columns).remove('date'),
                var_name = 'state', value_name = 'Recovered')
    df_MR['Recovered'] = pd.to_numeric(df_MR['Recovered'])
    df_MR.drop('date', axis = 1, inplace = True)
    df_MR = df_MR.groupby('state').sum()
    df_MR = df_MR['Recovered']
    ##################################################################
    ########## ALL States Deceased Data ##############################
    df_D = df_states[df_states['status'] == 'Deceased'].copy(deep = True)
    df_D.drop('status', axis = 1, inplace = True)
    df_MD = pd.melt(df_D, id_vars = 'date', value_vars = list(df_D.columns).remove('date'),
                var_name = 'state', value_name = 'Deceased')
    df_MD['Deceased'] = pd.to_numeric(df_MD['Deceased'])
    df_MD.drop('date', axis = 1, inplace = True)
    df_MD = df_MD.groupby('state').sum()
    df_MD = df_MD['Deceased']
    ##################################################################
    return df_MC, df_MR, df_MD

def start():
    urllib.request.urlretrieve(url, 'data.json');
    df = make_data()

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    create_pie_chart(df, STATIC_DIR)
    create_line_chart(df, STATIC_DIR)
    df_bar = create_dataset(df)
    df_MC, df_MR, df_MD = overall_info(df)
    return df_bar, df_MC, df_MR, df_MD
