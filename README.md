# Report on Creating an Image Project Model and Computer Vision Game
### This report describes how the Image Project Model is created and stored in the main branch of the GitHub repository server. Further, it describes how the Computer Vision Game is developed from this model.

## Milestone 1 
- This Milestone creates the GitHub repository in GitHub server and copies the repository to local desktop folder using following command: 
"git clone https://github.com/udslk/Computer_Vision.git"

## Milestone 2
- This milestone creates the Computer Vision System that detects whether the user is showing Rock, Scissors, Paper or Nothing 
- This system creates an image project model with different four classes: Rock, Scissors, Paper and Nothing
- It uses "Teachable-Machine" from "https://teachablemachine.withgoogle.com/" to create the Classes
- Each class is trained with images of the user showing each option to the camera. 
- The "Nothing" class represents the lack of option in the image
- Downloaded the model from the "Tensorflow" tab in Teachable-Machine.
- This model contained keras_model.h5 file and a label with file name labels.txt
- The model and the label is pushed to GitHub repository:

```
udslk@DESKTOP-UAJ9FVT MINGW64 ~/Desktop/AiCore_git/Computer_Vision (main)
$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.93 MiB | 1.28 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/udslk/Computer_Vision.git
   3eaa58f..c1b0eea  main -> main
```
## Milestone 3
-  In this milestone first the created the my_env environment:
      -  Installed the pandas python package:
         ```
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> conda install pandas
         ```
      -  Installed the python package manager pip:
         ```
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> conda install pip
         ```
      -  Using python package manger pip installed the python libraries, pencv-python, tensorflow, and ipykernel:
         ```
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> pip install opencv-python
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> pip install tensorflow
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> pip install ipykernel
         ```
      -  Created my environment called my_env and activated it:
         ```
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> conda create -n my_env
         (base) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> conda activate my_env
         (my_env) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision>
         ```
      -  Stored all installed dependencies in requirements.txt file:
         ```
         (my_env) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> pip list > requirements.txt
         ```
## Milestone 4
-  Following functions are implemented to develop the game Rock-Paper-Scissors game using the separate python file manual_rps.py:
      -  get_computer_choice: This function chooses an option randomly from a list, "Rock", "Paper" and "Scissors" and returns it. This function uses random library to choose an option from the list:
         ```python 
         def get_computer_choice():
               return random.choice(['Rock', 'Paper', 'Scissors'])
         ```
      - get_user_choice: This function chooses the user option by entering r or R for Rock, p or P Paper, s or S for Scissors and returns "Rock" if user enters r or R, "Paper" if user enters p or P OR "Scissors" if user enters s or S:
         ```python
         def get_user_choice():
            while True:
               letter = input('Enter your choice by typing R for Rock, P for Paper and S for Scissors:')
               if letter.lower() == 'r':
                  return 'Rock'
                  break
               elif letter.lower() == 'p':
                  return 'Paper'
                  break
               elif letter.lower() == 's':
                  return 'Scissors'
                  break
               else:
                  print('It is an incorrect choice')
         ```
      -  get_winner: This function takes two arguments, computer_choice and  user_choice, and returns the winner. If user chosen option is same as computer chosen option, it returns user as winner of the game otherwise it returns computer as winner of the game:
         ```python
        def get_winner(computer_choice, user_choice):
            if [computer_choice,user_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
               winner = 'Computer'
            elif [user_choice,computer_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
               winner = 'User'
            else:
               winner = 'No One'
            return winner
         ```
      -  play: This function calls above three functions and prints who is the winner of the game:
         ```python
         def play():
               computer_choice =  get_computer_choice()
               user_choice = get_user_choice()

               winner = get_winner(computer_choice, user_choice)
               if winner == 'User':
                  print('You win the game, CONGRATULATIONS')
               elif winner == 'Computer':
                  print('Computer wins the game')
               else:
                  print('No one Wins the game')
-  Below screen listing shows the expected results of this game:
   ```
   (my_env) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> python .\manual_rps.py
   Enter your choice by typing R for Rock, P for Paper and S for Scissors:p
   Computer wins the game
   (my_env) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision> python .\manual_rps.py
   Enter your choice by typing R for Rock, P for Paper and S for Scissors:2
   It is an incorrect choice
   Enter your choice by typing R for Rock, P for Paper and S for Scissors:r
   You win the game, CONGRATULATIONS
   (my_env) PS C:\Users\udslk\Desktop\AiCore_git\Computer_Vision>
   ```
## Milestone 5
-  In this milestone created a new python file called camera_rps.py and implemented following to create the Computer Vision Game:
      - Class CVG: Created a class called CVG - Computer Vision Game. This class contains following:
         - init function which initialise following variables: winner, user_wins, computer_wins and prediction_list that contain the options 'Rock', 'Paper', 'Scissors' and 'Nothing':
            ```python
            def __init__(self):
               self.winner = ''
               self.user_wins = 0
               self.computer_wins = 0
               self.prediction_list = ['Rock', 'Paper', 'Scissors','Nothing']
            ```
         - get_computer_choice function selects the one option from prediction list randomly
            ```python
            def get_computer_choice(self):
               return random.choice(self.prediction_list)
            ```
         - get_prediction function predicts the highest probability of trained model in the order, "Rock", "Paper", "Scissors", and "Nothing. Ex. if the first element of the list is 0.8, the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that user showed "Rock" to the camera with a confidence of 0.8:
            ```python
            def get_prediction(self, prediction):
                  nr = np.argmax(prediction)
                  return  self.prediction_list[nr]
            ```
         - get_user_choice function selects the user choice from the trained model using the above get_prediction function. This function uses time function to get the current time and the start time and count downs to zero from 5 sec to allow user to select the user choice:
            ```python
            def get_user_choice(self):
                  model = load_model('keras_model.h5')
                  cap = cv2.VideoCapture(0)
                  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

                  start_time = time.time()
                  time_lapped = 0
                  total_allowed_time = 5
    
                  while True: 
                     ret, frame = cap.read()
                     resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                     image_np = np.array(resized_frame)
                     normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                     data[0] = normalized_image
                     prediction = model.predict(data)
                     cv2.imshow('frame', frame)
               
                     # Press q to close the window
                     if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                     if time.time() - start_time >= time_lapped:
                        time_lapped += 1
                        print(f'Countdown {total_allowed_time - time_lapped}')
        
                     if time_lapped == total_allowed_time:
                        print(f'User selects {self.get_prediction(prediction)}')
                        break

                  # After the loop release the cap object
                  cap.release()
                  # Destroy all the windows
                  cv2.destroyAllWindows()
                  return self.get_prediction(prediction)
            ```
         - get_winner function takes two input variables, user_choice and computer_choice, and returns the winner. It applies following rules to choose the winner:
            -  Rock beats Scissors
            -  Paper beats Rock
            -  Scissors beats Paper
            -  If user wins it increments the variable user_wins by one and likewise does the same for variable computer_wins when computer wins in a round.
            ```python
            def get_winner(self, computer_choice, user_choice):
                  if [computer_choice,user_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
                     self.winner = 'Computer'
                     self.computer_wins +=1
                  elif [user_choice,computer_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
                     self.winner = 'User'
                     self.user_wins +=1
                  else:
                     self.winner = 'No One'
                  return self.winner
            ```
      - The main play_game() function creates the game object of CVG class and starts the game. It runs until either user or computer wins in three rounds:
         ```python
         def play_game(total_wins=3):
    
               game = CVG()
   
               while True:
               computer_choice =  game.get_computer_choice()
               user_choice = game.get_user_choice()
               winner = game.get_winner(computer_choice, user_choice)
               print(f'Computer choice in this round is {computer_choice}')
               print(f'User choice in this round is {user_choice}')
               if winner == 'User':
                  if game.user_wins == total_wins:
                     print('User wins the game, CONGRATULATIONS')
                     print(f'Final score is {game.user_wins} user win(s) and {game.computer_wins} computer win(s)')
                     break
                  else:
                     print('User win this round')
                     print(f'The score is {game.user_wins} user win(s) and {game.computer_wins} computer win(s)')
               elif winner == 'Computer':
                  if game.computer_wins == total_wins:
                     print('Computer win the game')
                     print(f'Final score is {game.computer_wins} computer win(s) and {game.user_wins} user win(s)')
                     break
                  else:
                     print('Computer wins round')
                     print(f'The score is {game.computer_wins} computer win(s) and {game.user_wins} user win(s)')
               else:
                  print('NO one wins this round')
               input("Press any key to continue...")
            pass
      -  Below screenshot shows the output when the user wins the game:
         >![image](https://github.com/udslk/Computer_Vision/blob/main/images/user-wins.PNG?raw=true)
      -  Below screenshot shows the output when the computer wins the game:
         >![image](https://github.com/udslk/Computer_Vision/blob/main/images/computer-wins.PNG?raw=true)




## Conclusion
- The milestone 2 shows how the Computer Vision System is created using the "Teachable-Machine" from "https://teachablemachine.withgoogle.com/"
- This System creates two important files, one for the image model called keras_model.h5 and other one for labels called labels.txt. 
- These two files are stored in GitHub repository
- These two files will be used in the Python application in later Milestones 