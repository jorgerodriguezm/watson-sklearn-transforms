from sklearn.base import BaseEstimator, TransformerMixin
from pandas import *

# All sklearn Transforms must have the `transform` and `fit` methods
class Bienvenida(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, df,Y=None):
        return df

    def transform(self,df):
        # Copia del Dataframe enviado
        dfcop = df.copy()
        return dfcop

#Transformar para One-Hot Encoding para Variables Categóricas
class Labeling(BaseEstimator, TransformerMixin):
    import pandas as pd
    toEncode=["SEX","EXISTING_SAVINGS","CHECKING_BALANCE","JOB_TYPE",'CREDIT_HISTORY','LOAN_PURPOSE','OTHERS_ON_LOAN','PROPERTY',
          'INSTALLMENT_PLANS','HOUSING']
    def __init__(self):
        pass
        

    def fit(self, df, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        df_encoded = pd.get_dummies(data, columns=toEncode)
        return df_encoded
    

# Un transformador para remover columnas indeseadas
class DropColumns(BaseEstimator, TransformerMixin):    
    columns=["ID","TELEPHONE","ALLOW"]
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return X

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data.drop(labels=self.columns, axis='columns')    
    
