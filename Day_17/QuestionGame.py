from Day_17.Question_model import Question_bank


from Question_model import Question_bank, Question_model
from Quiz_brain import Quiz_brain

end_game = False
new_question_bank = Question_bank()
new_quiz_brain = Quiz_brain()
while not end_game:
    your_choice = input("Enter 'quit' if you want to stop game: ")
    if your_choice == 'quit':
        end_game = True 
        break

    if your_choice == 'start':
        
