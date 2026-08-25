# KBC programme


questions = ['What gets wetter the more it dries?\n', 'What has a head and a tail, but no body?\n', 
             'What has many keys but cannot open a single lock?\n', 'If you have it, you want to share it. If you share it, you no longer have it. What is it?\n']

answers = ['towel', 'coin', 'piano', 'secret']
gist = zip(questions, answers)


points = 0

for question,answer in gist:
    print(f"Question: {question}\nOptions: {answers}\n")
    
    user_answer = input("Enter the correct option: \n")
    if answer == user_answer:
        points = points + 1
        print(f"correct answer, you get {points} point\n")
    if points == 4:
        print("congrats you win with all 4 points")
    else:
        print(f"wrong spelling, you gets {points} points\n")
        