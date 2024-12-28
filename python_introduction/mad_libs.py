#On a beautiful (adjective) day, I went to the zoo. I saw a funny (adjective) monkey swinging from the trees. 
#Then, I spotted a majestic (adjective) lion lounging in the sun.  What a wild and (adjective) experience! 

print("Mad Lib Game: 4 words is all it takes to create change.")
user_choice = input("Choose your strong point; A for Adjective, B for Adverb: ")
if user_choice == "A":
    first_word = input("Enter the first adjective:")
    second_word = input("Enter the second adjective:")
    third_word = input("Enter the third adjective:")
    fourth_word = input("Enter the fourth adjective:")
    print("On a beautiful", first_word, "day, I went to the zoo. I saw a funny ", second_word, "monkey swinging from the trees. \nThen, I spotted the majestic", third_word, "lion lounging in the sun. What a wild and", fourth_word, "experience!")
elif user_choice == "B":
    first_word = input("Enter the first adverb:")
    second_word = input("Enter the second adverb:")
    third_word = input("Enter the third adverb:")
    fourth_word = input("Enter the fourth adverb:")
    print("Just beacause you ran", first_word, "10km today doesn't mean you are now", second_word, "ready. \nTo achieve that you must practise", third_word, "everyday then slowly and ", fourth_word, "you will be fit to run even a marathon")
else:
    print("Game ended due to wrong input.")
    
