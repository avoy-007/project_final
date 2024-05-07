import numpy as np
import pandas as pd
import pickle
from pyforest import *

# def train_model():
#     print('Training the model...')
#     df = pd.read_csv(r'C:\Users\aarya\Desktop\project_final\concrete_data.csv')
#     df.columns = ['cement', 'slag', 'ash', 'Water', 'superplastic', 'coarseagg', 'fineagg', 'age', 'strength']

#     for cols in df.columns[:-1]:
#       Q1 = df[cols].quantile(0.25)
#       Q3 = df[cols].quantile(0.75)
#       iqr = Q3 - Q1

#       low = Q1-1.5*iqr
#       high = Q3+1.5*iqr
#       df.loc[(df[cols] < low) | (df[cols] > high), cols] = df[cols].median()
#     X = df.drop('strength', axis = 1)
#     y = df['strength']++++++++++++++++++++++++++++++++++++++++++
#     from scipy.stats import zscore

#     Xscaled = X.apply(zscore)
#     Xscaled_df = pd.DataFrame(Xscaled, columns=df.columns)

#     X_train, X_test, y_train, y_test = train_test_split(Xscaled,y, test_size= 0.3, random_state= 1)

#     model = RandomForestRegressor()
#     model.fit(X_train, y_train)
#     k = 20

#     kfold = KFold(n_splits=k, random_state=70, shuffle = True)
#     K_results = cross_val_score(model, X, y, cv=kfold)
#     accuracy=np.mean(abs(K_results))
#     return model

def load_model(path):
    model = pickle.load(open(path,'rb'))
    return model

def predict_slump(model, featureDict={}):
    print('Predicting the value...')
    # print("Enter the following parameters for the concrete mix:")
    # cement = float(input("Cement (kg/m^3): "))
    # slag = float(input("Slag (kg/m^3): "))
    # ash = float(input("Fly ash (kg/m^3): "))
    # water = float(input("Water (kg/m^3): "))
    # superplastic = float(input("Superplasticizer (kg/m^3): "))
    # coarseagg = float(input("Coarse Aggregate (kg/m^3): "))
    # fineagg = float(input("Fine Aggregate (kg/m^3): "))
    # age = int(input("Age (days): "))

    # Create an array with the input values
    cement = featureDict['cement'] 
    slag = featureDict['slag'] 
    ash = featureDict['ash'] 
    water = featureDict['water'] 
    superplastic = featureDict['superPlastic'] 
    silicafumes = featureDict['silicafumes']
    coarseagg = featureDict['coarseAgg'] 
    fineagg = featureDict['fineAgg']  
    input_data = np.array([[cement, slag, ash, water, superplastic, coarseagg, fineagg, silicafumes]])

    # Make prediction
    prediction = model.predict(input_data)
    return f"{prediction[0]:.2f} MPa"

if __name__ == '__main__':
    # Example usage:
    # model = train_model()
    # # print(predict_concrete_strength(model))
    savePath = r'models\grad_boost.sav'
    # # print(type(pickle.dumps(model)))
    # # print(pickle.dumps(model))
    # with open(savePath, 'w') as fout:
    #    fout.write(str(pickle.dumps(model)))
    model2 = load_model(savePath)
    print(predict_slump(model2))
