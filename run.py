print("Welcome to the Quiz")
score = 0
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")

answer = input("Whats the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 
    
answer = input("Whats the capital of Spain? ")
if answer.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Whats the capital of England? ")
if answer.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Whats the capital of Germay? ")
if answer.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")                   