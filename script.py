# Author: Sahil Verma


'''Importing necessary lib csv for output, watson_developer_cloud for Analyse
    matplotlib for ploting, numpy to make array '''
import csv
from watson_developer_cloud import ToneAnalyzerV3
import matplotlib.pyplot as plt
import numpy as np

# Taking input
texted = input("Enter the sentence to analyse \n")

# API request from IBM Watson
tone_analyzer = ToneAnalyzerV3(
    username='',  # Enter the username and password provided by bluemix
    password='',
    version='2016-05-19 ')
result = tone_analyzer.tone(text=texted)  # Getting output as a file of dictonary

xyz = []

for x in result["document_tone"]["tone_categories"][0].get("tones"):  # Selecting specific Emotion is result
    xyz.append(x)

print(xyz)  # Printing Emotions as text


# Writing Input and Output to csv file
def write2csv():
    f = open("output.csv", "w")

    w = csv.DictWriter(f, ("Input", "e1", "e2", "e3", "e4"))
    w.writeheader()

    x = xyz
    op = {}

    op = {"Input": texted,
          "e1": (x[0].get("tone_name").strip(), x[0].get("score")),
          "e2": (x[1].get("tone_name"), x[1].get("score")),
          "e3": (x[2].get("tone_name"), x[2].get("score")),
          "e4": (x[3].get("tone_name"), x[3].get("score")),
          }

    w.writerow(op)

    f.flush()
    f.close()


write2csv()

# Taking emotions to visulisation creating array and plotting it using matplotlib
emotion = []
values = []
X = [1, 2, 3, 4, 5]
scale = np.array([0.0000, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

for x in xyz:
    emotion.append(x.get("tone_name"))
    values.append(x.get("score"))

plt.plot(X, values, 'ro')  # Plot value
plt.xticks(X, emotion, rotation='vertical')
plt.show()