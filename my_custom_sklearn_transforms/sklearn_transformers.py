from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pan

# All sklearn Transforms must have the `transform` and `fit` methods
class Bienvenida(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, df,Y=None):
        return df

    def transform(self,df):
        # Copia del Dataframe enviado
        dfcop = df
        return dfcop

#One-Hot Encoding para Variables Categóricas
class Labeling(BaseEstimator, TransformerMixin):
    toEncode=["SEX","EXISTING_SAVINGS","CHECKING_BALANCE","JOB_TYPE",'CREDIT_HISTORY','LOAN_PURPOSE','OTHERS_ON_LOAN','PROPERTY',
          'INSTALLMENT_PLANS','HOUSING']
    def __init__(self):
        pass
        

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X
        # Retornamos One-Hot Encoding
        df_encoded = pan.get_dummies(data, columns=self.toEncode)
        return df_encoded.sort_index(axis=1).to_numpy() 
    

# Un transformador para remover columnas indeseadas
class DropColumns(BaseEstimator, TransformerMixin):    
    columns=["ID","TELEPHONE","ALLOW"]
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return X

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data.drop(labels=self.columns, axis='columns')    
    
