import wikipedia

topics = ["Philosophy of life", "blue", "Galaxy"]

for topic in topics:
    print(f"--- {topic} ---")
    print(wikipedia.summary(topic, sentences=2))