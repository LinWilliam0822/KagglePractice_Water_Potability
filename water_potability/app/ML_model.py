# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:30:20 2022

@author: Owner
"""
#from keras.models import load_model
from tensorflow import keras
from tensorflow.keras.models import load_model
import joblib
import numpy as np

#import matplotlib.pyplot as plt

def DNN_model(input_X):
    
    scaler = joblib.load('scaler.save')
    input_X_scaled = scaler.fit_transform(input_X['data'])
    
    model = load_model("WaterQuality.h5")
    #result = model.predict(input_X_scaled).reshape(1,-1)
    result = model.predict(input_X_scaled)
    result = np.argmax(result,axis=1)
    result = np.array(result)
    result = np.reshape(result,(result.shape[0],1))
    result = np.concatenate([input_X['data'],result],axis=1)
    
    print(result)
    
    # 把結果放進字典裡
    result = {'data':result.tolist()}
    return result

if __name__ == "__main__":
    X  = {'data': [
    [8.316765884,214.3733941,22018.41744,8.059332377,356.8861356,363.2665162,18.4365245,100.3416744,4.628770537],
    [9.092223456,181.1015092,17978.98634,6.546599974,310.1357375,398.4108134,11.55827944,31.99799273,4.075075425]
    ]
    }
    DNN_model(X)
