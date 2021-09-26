#-------------------------------------------------------------------------
# AUTHOR: Nate Colbert
# FILENAME: naive_bayes
# SPECIFICATION: implements naive bayes algorithm
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2-3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
weather_training = []

with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            weather_training.append (row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
tempList = []

transform = {'Sunny': 1, 'Overcast': 2, 'Rain': 3, 
             'Hot': 1, 'Mild': 2, 'Cool': 3, 
             'High': 1, 'Normal': 2, 
             'Strong': 1, 'Weak': 2,
             'Yes': 1, 'No':2}

for i in range(len(weather_training)):
    for j in range(4):
        tempList.append(transform[weather_training[i][j+1]])
    X.append(tempList)
    tempList = []

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for i in range(len(weather_training)):
    Y.append(transform[weather_training[i][5]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
weather_test = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            weather_test.append (row)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
predictVal = []
testNums = []

for i in range(len(weather_test)):
    for j in range(4):
        tempList.append(transform[weather_test[i][j+1]])
    testNums.append(tempList)
    tempList = []
#print(testNums)

for i in range(len(testNums)):
    predicted = clf.predict_proba([testNums[i]])[0]
    predictVal.append(predicted)
#print(predictVal[0])
#print(predictVal[0][0],predictVal[0][1])

for i in range(len(testNums)):
        if (predictVal[i][0] > predictVal[i][1]) and (predictVal[i][0] >= 0.75):
            #predictVal[i] = "Yes"
            print(weather_test[i][0].ljust(15), weather_test[i][1].ljust(15), weather_test[i][2].ljust(15), weather_test[i][3].ljust(15), weather_test[i][4].ljust(15), "Yes".ljust(15), round(predictVal[i][0], 2), "\n")
        elif (predictVal[i][0] < predictVal[i][1]) and (predictVal[i][1] >= 0.75):
            #predictVal[i] = "No"
            print(weather_test[i][0].ljust(15), weather_test[i][1].ljust(15), weather_test[i][2].ljust(15), weather_test[i][3].ljust(15), weather_test[i][4].ljust(15), "No".ljust(15), round(predictVal[i][1], 2), "\n")

