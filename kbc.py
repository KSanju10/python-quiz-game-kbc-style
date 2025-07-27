questions=[
    [
        " Which of the following is a supervised learning algorithm?",
        "K-Means Clustering","Apriori Algorithm","Linear Regression","PCA","None",3
    ],
    [
        "What does the “p” in a p-value stand for in hypothesis testing?",
        "Proportion","Probability","Precision","Prediction","None",2
    ],
    [
        "Which library is most commonly used for data manipulation in Python?",
        "NumPy","Pandas","Matplotlib","Scikit-learn","None",2
    ],
    [
        " What is the output of df.describe() in pandas?",
        "Count of null values","Summary statistics","Column names","Data types","None",2
    ],
    [
        "What does overfitting in a model indicate?",
        "The model performs well on unseen data","The model is too simple","The model memorized the training data"," The model underestimates the noise","None",3
    ],
    [
        "Which of the following is a measure of model accuracy for regression?",
        "Confusion Matrix","ROC Curve","Mean Squared Error (MSE)","F1 Score","None",3
    ],
    [
        " What does the term “dimensionality reduction” refer to?",
        "Increasing data size","Reducing number of rows","Converting string to integers","Reducing number of features","None",4
    ],
    [
        "Which of the following techniques is used for classification?",
        "Decision Trees","K-Means","PCA","Apriori","None",1
    ],
    [
        "What type of chart is most appropriate for showing the distribution of a single variable?",
        "Bar Chart","Scatter Plot","Histogram","Line Chart","None",3
    ],
    [
        "What is the full form of NaN?",
        "New and Normal"," Not a Number","Number at Null","Null and Negative","None",2
    ],
    [
        " Which algorithm is best for detecting outliers in a dataset?",
        "Logistic Regression"," Isolation Forest","KNN","Linear Regression","None",2
    ],
    [
        "What is the purpose of train-test split?",
        "To shuffle the data","To convert data into numeric format","To evaluate model performance on unseen data","To save memory","None",3
    ],
    [
        " What does the .fit() function do in Scikit-learn?",
        "Splits the dataset"," Displays model summary","Trains the model","Normalizes the dataset","None",3
    ],
    [
        "Which activation function is most commonly used in deep learning?",
        "Sigmoid","ReLU","tanh","Softmax","None",2
    ],
    [
        "What type of plot is used to show correlation between two continuous variables?",
        "Box Plot","Scatter Plot","Line Plot","Pie Chart","None",2
    ]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,500000,1000000,2000000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestions for RS.{levels[i]} : ")
    print("\n"+ question[0] +"\n")
    print(f"a. {question[1]}             b. {question[2]}")
    print(f"c. {question[3]}             d. {question[4]}")
    replay=int(input("Enter your answer (1-4): "))
    if replay==question[-1]:
        print("Correct Answer!" + f"You won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
            print("Congratulations! You have won the game!")
            print("Final amount won: Rs. 10,000,000")
    else:
        print("Wrong Answer!")
        break
    
print(f"You took home Rs.{money} in winnings from this game. Thank you for playing!")
