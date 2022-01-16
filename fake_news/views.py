from django.shortcuts import render

import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split


tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model = pickle.load(open(os.path.join(os.getcwd(), 'fake_news/model.pkl'), 'rb'))
dataframe = pd.read_csv(os.path.join(os.getcwd(), 'fake_news/news.csv'))
x = dataframe['text']
y = dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


def fake_news_det(news):
    tfid_x_train = tfvect.fit_transform(x_train)
    tfid_x_test = tfvect.transform(x_test)
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

def fake_news(request):
    pred = ""
    if request.method == 'POST':
        message = request.POST['message']
        pred = fake_news_det(message)[0]
        print(pred)
    else:
        pred = ""

    return render(request, 'index.html', {"prediction":pred})
