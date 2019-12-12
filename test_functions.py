import pytest
import pandas as pd
import function as func

def test_plot_prevention_method():
    dataset = pd.read_csv('../plots.csv')
    methods = func.plot_prevention_method('prevention_method', dataset)
    assert isinstance(methods, pd.Series)
    
    
def test_the_final_graph():
    dataset = pd.read_csv('../plots.csv')
    times = func.the_final_graph('attack_year', dataset)
    assert 1==1
    assert isinstance (times, pd.Series)
    
