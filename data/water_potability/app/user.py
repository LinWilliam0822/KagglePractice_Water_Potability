# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:25:24 2022

@author: Owner
"""
from urllib import response
import requests
import random
#res = requests.get("http://127.0.0.1:8002/page5")
#res = requests.post("http://127.0.0.1:8002/page10")
data = {
        'data':
        [
            [0.1,0.1,0.1,0.1],
            [0.1,0.2,0.2,0.2],
            [0.1,0.1,0.1,0.1],
            [0.1,0.2,0.2,0.2],
            [0.1,0.1,0.1,0.1],
            [0.1,0.2,0.2,0.2]
        ]
        }
    
data = {
        'data':
        [
            [random.uniform(0, 0.5) for i in range(0,4)],
            [random.uniform(0, 0.5) for i in range(0,4)],
            [random.uniform(0, 0.5) for i in range(0,4)],
            [random.uniform(0, 0.5) for i in range(0,4)]
        ]
    }
    
data = {'data': [
    [8.316765884,214.3733941,22018.41744,8.059332377,356.8861356,363.2665162,18.4365245,100.3416744,4.628770537],
    [9.092223456,181.1015092,17978.98634,6.546599974,310.1357375,398.4108134,11.55827944,31.99799273,4.075075425]
    ]
    }
#res = requests.post("http://192.168.43.210:5000/detect",json=data)
res = requests.post("http://192.168.43.210:5000/detect",json=data)

print(res.json())

#print(res.json())