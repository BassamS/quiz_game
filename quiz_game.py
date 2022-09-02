print("Welcome to my computer quiz!")

playing = input("Do you know about computer hardware? You want to play (yes/no)? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

answer = input("\nWhat does CPU stand for? ")
if answer.lower() == "central processing unit":
  score += 1
  print(f"\nCorrect! Your score now is: {score}")
else:
  print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  score += 1
  print(f"\nCorrect! Your score now is: {score}")
else:
  print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  score += 1
  print(f"\nCorrect! Your score now is: {score}")
else:
  print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  score += 1
  print(f"\nCorrect! Your score now is: {score}")
else:
  print("Incorrect!")
answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
  score += 1
  print(f"\nCorrect! Your score now is: {score}")
else:
  print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score / 5) * 100} %.")