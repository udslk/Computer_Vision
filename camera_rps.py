import cv2 
import time
import random
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class CVG:

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
    
    game = CVG()
   
    while True:
        computor_choice =  game.get_computer_choice()
        user_choice = game.get_user_choice()
        winner = game.get_winner(computor_choice, user_choice)
        print(f'Computer choice in this round is {computor_choice}')
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
            print('NO one wins this roud')
        input("Press any key to continue...")
    pass

if __name__ == '__main__':
    play_game()
