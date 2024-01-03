from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


class B(BaseModel):
    n_1 : float
    n_2 : float
    n_3 : float
    n_4 : float

model = pickle.load(open('p.pkl','rb'))



app = FastAPI()


@app.post('/p')
async def p(i : B):
    n = pd.DataFrame([[i.n_1,i.n_2,i.n_3,i.n_4]] , columns =['Variance',	'Skewness',	'Curtosis',	'Entropy'])
    prediction = model.predict(n)
    print(prediction[0])
    if prediction[0] == 0 :
        return {'DecisionTreeClassifier':'output - 0'}
    return {'DecisionTreeClassifier':'output - 1'}