import pandas as pd
# import numpy as np

# загрузка моделей
#model.load_model('model/model.cbm')

data = pd.read_csv("data/building_20230808.csv")


def predict_type(text):
    '''Предсказание типа письма и типа заявки'''
    data = pd.DataFrame(data={'text': [text]}, index=[0])

    #prediction = model.predict(data)
    #prediction = {"success": true, "query:": ["address": text], "result": [{"target_building_id": 209676 ,"target_address":  "г.Санкт-Петербург, Аптекарский проспект, дом 18, литера А" }]}
    prediction = {"success": "true", "query:": ["address", text], "result": [{"target_building_id", 209676 ,"target_address",  "г.Санкт-Петербург, Аптекарский проспект, дом 18, литера А" }]}

    return prediction


