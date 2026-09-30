from solution import KNNClassifier

model = KNNClassifier(k=1)
model.train([(1.0, "low"), (3.0, "low"), (8.0, "high"), (10.0, "high")])
for value in [2.8, 8.2]:
    print(f"{value}: {model.classify(value)}")
