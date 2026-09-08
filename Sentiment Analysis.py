positive = [
    "good",
    "great",
    "excellent",
    "happy",
    "amazing",
    "love"
]

negative = [
    "bad",
    "poor",
    "sad",
    "hate",
    "worst",
    "terrible"
]

text = input("Enter a sentence: ")

words = text.lower().split()

score = 0

for word in words:

    if word in positive:
        score += 1

    elif word in negative:
        score -= 1


if score > 0:
    print("Positive Sentiment")

elif score < 0:
    print("Negative Sentiment")

else:
    print("Neutral Sentiment")
