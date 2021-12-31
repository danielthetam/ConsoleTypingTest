import datetime
import time
import random
import math


def pick_random_phrase():
    with open("phrases.txt", "r") as f:
        sentences = f.readlines()
        
        random_line = random.randint(0, len(sentences) - 1)

        return sentences[random_line]

def calculate_accuracy(user_answer, original_phrase):
    user_phrase = list(user_answer)
    original_phrase = list(original_phrase)

    accuracy = 0

    for key, letter in enumerate(user_phrase):
        if key > (len(original_phrase) - 1):
            continue

        if letter == original_phrase[key]:
            accuracy += 1

    return math.ceil((accuracy/len(original_phrase)) * 100)
    

def calculate_wpm(start_time, end_time, original_phrase, accuracy):
    start_time = datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
    end_time = datetime.timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)

    time = end_time - start_time
    words_typed = len(original_phrase.split())

    wpm = ((words_typed/time.total_seconds()) * 60) * (accuracy/100)
    raw_wpm = (words_typed/time.total_seconds()) * 60
    return (math.ceil(wpm), math.ceil(raw_wpm))



# Welcoming the Player
print("=================")

print("Welcome to the Console Typing Test")
start = input("Press enter to begin")

time.sleep(0.8)

print("=================")
print("")

print("Begin typing this phrase on the count of 3")

time.sleep(0.8)

random_phrase = pick_random_phrase()
print(random_phrase)

time.sleep(0.8)

for i in range(3):
    print(str(i + 1))
    time.sleep(1)

start_time = (datetime.datetime.now() + datetime.timedelta(hours=8)).time()

user_phrase = input(">> ")

end_time = (datetime.datetime.now() + datetime.timedelta(hours=8)).time()

print("Thank you for answering. ")
print("Calculating your results...")

time.sleep(3)

accuracy = calculate_accuracy(user_phrase, random_phrase)
wpm, raw_wpm  = calculate_wpm(start_time, end_time, random_phrase, accuracy)

print("RESULTS")
print("===============")
print("Accuracy: " + str(accuracy) + "%")
print("Words Per Minute: " + str(wpm))
print("Raw Words Per Minute: " + str(raw_wpm))
print("===============")
