from textblob import TextBlob

print("Welcome to the AI Mood Detector!")
userName = input("What's your name? ")
print(f"Nice to meet you, {userName}! Let's analyze the sentiment of your sentences.")
print("Type 'exit' to quit.\n")

while True:
    inputText = input("📝 Enter a sentence: ")
    if inputText.lower() == 'exit':
        print(f"Goodbye, {userName}! Have a great day!")
        break

    sentimentBlob = TextBlob(inputText)
    polarityScore = sentimentBlob.sentiment.polarity

    if polarityScore > 0:
        print("😊 Positive sentiment detected!\n")
    elif polarityScore < 0:
        print("😞 Negative sentiment detected!\n")
    else:
        print("😐 Neutral sentiment detected!\n")
