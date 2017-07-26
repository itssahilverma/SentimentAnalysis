'''author @itssahilverma
training data : label in x and sentence in y
expected output : label from 6 basic emotion for a given input sentence
 '''

from sklearn import tree    # Labeling data using Decision Tree

train_x = []                # setting up the train sets
train_y = []

# If having a small set to train directly enter to the list
# If importing data from a specific file
'''with open('') as file:       # file name in ''
    l = file.readline()         # assuming the first word or letter is the label
    l.split()
    for line in file:
        temp = line.split()
        n = len(temp)
        train_x.append(int(temp[0]))
        train_y.append(" ".join(temp[1:n]))'''



clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_x, train_y)         # training the model, for x vs y


y_test = input("Enter the test sentence : \t")
output=clf.predict(y_test)



