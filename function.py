import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#first function

def plot_prevention_method (the_first_graph, dataset):
    """ this function is used to plot the frequencies of methods that used to successfully detected Jihadist attacks into a bar plot
    """
    Jihadist_attack = dataset[dataset['plot_ideology']=='Jihadist']
    Prevented= Jihadist_attack[Jihadist_attack['plot_status']=='Prevented']
    methods = Prevented[the_first_graph].value_counts()
    methods.plot(kind = 'bar')
    return methods


#second function

def plot_casualties_tendency (the_first_variable, the_second_variable, dataset):
    """ this function is ucsed to plot the casuality caused by Jihadist attacks each time over the year to try to explore its tendency by adding a regression line"""
    Jihadist_attack = dataset[dataset['plot_ideology']=='Jihadist']
    Prevented= Jihadist_attack[Jihadist_attack['plot_status']=='Prevented']
    Not_Prevented= Jihadist_attack[Jihadist_attack['plot_status']=='Not Prevented']
    Not_Prevented['victims_wounded'] =Not_Prevented['victims_wounded'].fillna(Not_Prevented['victims_wounded'].mean())
    Not_Prevented['victims_killed']= Not_Prevented['victims_killed'].fillna(Not_Prevented['victims_killed'].mean())
    Not_Prevented ['victims_casualties'] = Not_Prevented ['victims_wounded'] + Not_Prevented.victims_killed
    Not_Prevented= Not_Prevented.dropna(subset=['plot_ID'])
    Not_Prevented['attack_time'] = Not_Prevented['attack_date'].apply(lambda x: pd.to_datetime(x))
    Not_Prevented = Not_Prevented.dropna(subset=['attack_time'])
    Not_Prevented.sort_values('attack_time')


    plt.scatter(x= Not_Prevented[the_first_variable], y=Not_Prevented[the_second_variable])

    reg= linear_model.LinearRegression()
    reg.fit(Not_Prevented[[the_first_variable]], Not_Prevented[the_second_variable])
    plt.plot(Not_Prevented[the_first_variable], reg.predict(Not_Prevented[[the_first_variable]]))

    


#third function
def the_final_graph (inputs, dataset):
    """ this function is used to plot a bar graph to show the terrorist attacks frequency over years"""
    dataset= dataset.dropna(subset=['attack_date'])
    dataset['attack_year'] = dataset['attack_date'].apply(lambda x: pd.to_datetime(x).year)
    dataset.sort_values('attack_year')
    times=dataset[inputs].value_counts().sort_index()
    times.plot(kind= 'bar')
    return times

    