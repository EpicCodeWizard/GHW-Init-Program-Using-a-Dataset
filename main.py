from cohere.classify import Example
import cohere

co = cohere.Client("2H7QHvLLgO1HK4kzz6w7EBLpoEHVJnYOTH0UbGF5")
dataset = [Example(x.split("\t")[1], x.split("\t")[0]) for x in open("preds.txt", "r").read().split("\n")]
classifications = co.classify(model="medium", taskDescription="The following is a sentiment classifier regarding an input the user gives.", outputIndicator="this is:", inputs=input("Input something to be classified as positive or negative. "), examples=dataset).classifications
for class in classifications:
  if class.prediction == "positive":
    print("positive")
  else:
    print("negative")
