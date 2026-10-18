import random
from tkinter.constants import TRUE

print("Welcome to quiz app -  ")

while True:
    marks = 0
    ###---- SCIENCE ----###
    S_question1 = ["1, Au","2. Go","3. Ag","4. Gu"]
    S_question2 = ["1. Venus","2. Mars","3. Jupiter","4. Saturn"]
    S_question3 = ["1. Oxygen","2. Nitrogen","3. Hydrogen","4. Carbon Dioxide"]
    while True :
        random.shuffle(S_question1)
        index_S_Q_1 = S_question1.index("Au")
        random.shuffle(S_question2)
        index_S_Q_2 = S_question2.index("Mars")
        random.shuffle(S_question3)
        index_S_Q_3 = S_question3.index("Carbon Dioxide")
        if (index_S_Q_1 != index_S_Q_2 != index_S_Q_3) and (index_S_Q_1 != index_S_Q_3):
            break
    Science = {index_S_Q_1:"What is the chemical symbol for gold?",index_S_Q_2:"Which planet in our solar system is known as the Red Planet?",index_S_Q_3:"What gas do plants primarily absorb from the atmosphere for photosynthesis?"}

    ###---- MATHS ----###
    M_question1 = [3.12,3.14,3.16,3.18]
    M_question2 = [10,11,12,14]
    M_question3 = [40,50,60,70]
    while True :
        random.shuffle(M_question1)
        index_M_Q_1 = M_question1.index(3.14)
        random.shuffle(M_question2)
        index_M_Q_2 = M_question2.index(12)
        random.shuffle(M_question3)
        index_M_Q_3 = M_question3.index(50)
        if (index_M_Q_1 != index_M_Q_2 != index_M_Q_3) and (index_M_Q_1 != index_M_Q_3):
            break
    Maths = {index_M_Q_1:" What is the value of π (pi) rounded to two decimal places?",index_M_Q_2:"What is the square root of 144?",index_M_Q_3:"If two angles of a triangle measure 60° and 70°, what is the measure of the third angle?"}

    ###---- ENGLISH ----###
    E_question1 = ["Cruel","Generous","Hostile","Selfish"]
    E_question2 = ["Noun","Adjective","Adverb","Verb"]
    E_question3 = ["Childs","Children","Childrens","Childi"]
    while True :
        random.shuffle(E_question1)
        index_E_Q_1 = E_question1.index("Generous")
        random.shuffle(E_question2)
        index_E_Q_2 = E_question2.index("Adverb")
        random.shuffle(E_question3)
        index_E_Q_3 = E_question3.index("Children")
        if (index_E_Q_1 != index_E_Q_2 != index_E_Q_3) and (index_E_Q_1 != index_E_Q_3):
            break
    English = {index_E_Q_1:"Which of the following words is a synonym for 'benevolent' ?",index_E_Q_2:"What part of speech is the word 'quickly' in the sentence: “She ran quickly to the store.”?",index_E_Q_3:"What is the correct plural form of the word 'child'?"}

    try:
        what = int(input("Please enter 1 to do Science quiz, 2 for Maths, 3 for English & 4 for quiting : "))
    except:
        print("Please enter a valid input!!")
        continue
    if what == 1 :
        test_dic = Science
        index_test1 = index_S_Q_1
        index_test2 = index_S_Q_2
        index_test3 = index_S_Q_3
        index_mcq1 = S_question1
        index_mcq2 = S_question2
        index_mcq3 = S_question3
    elif what == 2 :
        test_dic = Maths
        index_test1 = index_M_Q_1
        index_test2 = index_M_Q_2
        index_test3 = index_M_Q_3
        index_mcq1 = M_question1
        index_mcq2 = M_question2
        index_mcq3 = M_question3
    elif what == 3:
        test_dic = English
        index_test1 = index_E_Q_1
        index_test2 = index_E_Q_2
        index_test3 = index_E_Q_3
        index_mcq1 = E_question1
        index_mcq2 = E_question2
        index_mcq3 = E_question3
    elif what == 4 :
        break
    else:
        print("Please enter a valid input!!")
        continue
    count = 1
    q_num = 1
    for test in test_dic :
        if count == 1 :
            current_test = index_test1
            current_mcq = index_mcq1
        elif count == 2 :
            current_test = index_test2
            current_mcq = index_mcq2
        elif count == 3 :
            current_test = index_test3
            current_mcq = index_mcq3
        else :
            break
        count += 1
        try:
            ans = int(input(f" Q{q_num}) {test_dic[test]} enter 1 for first 2 for second and so on {current_mcq} : "))
        except:
            print("Please enter a valid input!!")
            print("SKIPING TO NEXT QUESTION!!")
            continue
        if ans < 1 or ans > 4 :
            print("Please enter a valid input!!")
            print("SKIPING TO NEXT QUESTION!!")
            continue
        if ans == (current_test+1)  :
            print("correct!")
            marks +=1
        else:
            print("wrong!")
        print(f"marks -> {marks}")
        q_num +=1
    print(f"You scored {marks} out of 3 in the quiz.")
