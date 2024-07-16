from tqdm import tqdm
import numpy as np
import pandas as pd
from itertools import accumulate
import matplotlib.pyplot as plt
import seaborn as sns
def warn(*args,**kwargs):
    pass
import warnings
warnings.warn=warn
warnings.filterwarnings('ignore',category=DeprecationWarning)
warn()
!pip install scikit-plot
import scikitplot as skplt
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
sns.set_style('white')
sns.set_context('notebook')
#%matplotlib inline

