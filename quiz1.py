class Quiz:

    def __init__(self):

        self.questions = [
            {
                "question": "Which of the following is an example of reinforcement learning?",
                "options": "A) Chess playing AI\nB) Image classification\nC) Stock price prediction\nD) Spam email filtering",
                "answer": "A"
            },
            {
                "question": "What is the primary purpose of a decision tree in machine learning?",
                "options": "A) To create a linear model for regression\nB)To identify patterns in data without labels\nC) To optimize neural networks\nD) To split data into subsets based on feature values",
                "answer": "D"
            },
            {
                "question": "What is the key idea behind the k-nearest neighbors (KNN) algorithm?",
                "options": "A) Minimize the sum of squared errors\nB) Classify data based on the closest labeled data points\nC) Use a neural network to make decisions\nD) Perform regression using decision trees",
                "answer": "B"
            },
            {
                "question": "In deep learning, what does the term 'backpropagation' refer to?",
                "options": "A) A method of optimizing hyperparameters\nB)A way of visualizing model performance \nC) A technique for updating the weights in a neural network during training\nD) A type of regularization used to prevent overfitting",
                "answer": "C"
            },
            {
                "question": "What is the main advantage of using a convolutional neural network (CNN) for image recognition?",
                "options": "A) CNNs are faster than traditional machine learning algorithms\nB) CNNs automatically learn spatial hierarchies in images\nC) CNNs are better suited for handling sequential data\nD) CNNs don't require large amounts of labeled data",
                "answer": "B"
            }
        ]

        self.score = 0

    def start_quiz(self):
        print("--------------------Welcome to the AI Quiz!--------------------")
        for i, ques in enumerate(self.questions, 1):
            print(f"Question {i}: {ques['question']}")
            print(ques["options"])

            answer = input("Your Answer : ").upper()

            if answer == ques['answer']:
                print("Correct Answer")
                self.score += 2

            else:
                print("Wrong Answer")
                self.score -= 0.5

        print(f"\t\t\tYour Final Score is {self.score} out of 10")

quiz = Quiz()
quiz.start_quiz()
