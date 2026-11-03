import math

#fictional next-token logits
logits = [3.0, 4.0, 0.5, -1.0]
tokens = ["Dhaka", "Chittagong", "London", "Banana"]

#Numerically stable softmax
max_logit = max(logits)
exps = [math.exp(x - max_logit) for x in logits]
total = sum(exps)

probabilities = [x / total for x in exps ]

for token, probability in zip(tokens, probabilities):
    print(f"{token:12} {probability:.2%}")