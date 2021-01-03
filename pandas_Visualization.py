import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import vaex # use for load and process large dataset
import Dtale #Exploratry data analysis


from pandas_visual_analysis import VisualAnalysis
dataset = sns.load_dataset('iris')
VisualAnalysis(dataset)
