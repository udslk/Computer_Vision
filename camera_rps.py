import cv2 
import time
import random
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class CVG:

    '''
    Computer Vision Game is defined as class CVG. It has following parameters, attributes and methods:
    
    Parameters:
    ----------
    winner: str
        This stores the winner of the game, user , computer or no-one.
    user_wins: int
        This stores the number of times user wins the game
    computer_wins: int
        This stores the number of times computer wins the game
    
    Attributes:
    ----------
    prediction_list: list
        A list of options that computer can choose randomly

    Methods:
    -------
    __init__()
        Initialises the above parameters and attribute.
    
    get_computer_choice()
        Computer randomly selects the options from the list, Rock, Paper, Scissors and Nothing and returns it to the calling function.

    get_prediction(prediction)
        This function takes list variable prediction which contains the output of the image model and returns the index of the option that has highest probability.  
    
    get_user_choice()
        This method calls the get_prediction function to predict the user's selection from the frames captured by computer.

    get_winner(computer_choice, user_choice)
        This method takes two input variables, computer_choice and user_choice, and decides who is the winner and returns the winner

    '''
    def __init__(self):
        self.winner = ''
        self.user_wins = 0
        self.computer_wins = 0
        self.prediction_list = ['Rock', 'Paper', 'Scissors','Nothing']
        

    def get_computer_choice(self):
        return random.choice(self.prediction_list)

    def get_prediction(self, prediction):
        nr = np.argmax(prediction)
        return  self.prediction_list[nr]

    def get_user_choice(self):
        '''
        This method calls the get_prediction function to predict the user's selection from the frames captured by computer.
        It uses start_time variable to stor the start time of the camera is on to capture the frames of the user and gives 5 sec to user to show the trained image on the camera.
        In the while loop it checks the time_lapped parameter whether it took 5 sec. During this 5 sec it prints the count down value to let user know remaining time to show the trained image. 
        After 5 sec it calls the get_prediction() function to return the most trained image by the user.
        '''
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
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return self.get_prediction(prediction)
           
    def get_winner(self, computer_choice, user_choice):
        '''
        This method takes two input variables, computer_choice and user_choice, and decides who is the winner and returns the winner:
        It applies following rules to choose the winner:
            -  Rock beats Scissors
            -  Paper beats Rock
            -  Scissors beats Paper
        If user wins it increments the variable user_wins by one and likewise does the same for variable computer_wins when computer wins in a round.
        '''
        if [computer_choice,user_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
            self.winner = 'Computer'
            self.computer_wins +=1
        elif [user_choice,computer_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
            self.winner = 'User'
            self.user_wins +=1
        else:
            self.winner = 'No One'
        return self.winner
        
def play_game(total_wins=3):
    '''
    The main play_game() creates the game object of CVG class and starts the game. It runs until either user or computer wins in three rounds.
    For each round, it prints following:
        - if user wins it prints - "User wins the game, CONGRATULATIONS", along with the score 
        - if computer wins it prints - "Computer win the game", along with the score
        - if there is no results, it prints - "NO one wins this round"
    After three wins of either from use or computer it prints winner with the final score.
    '''
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

if __name__ == '__main__':
    play_game()
