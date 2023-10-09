print("Welcome to the Quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play!")

answer = input("Whats the capital of France? ")
if answer == "paris":
    print("Correct!")
else:
    print("Incorrect!") 
    
answer = input("Whats the capital of Spain? ")
if answer == "madrid":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Whats the capital of England? ")
if answer == "london":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Whats the capital of Germay? ")
if answer == "berlin":
    print("Correct!")
else:
    print("Incorrect!")               