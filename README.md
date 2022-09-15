# Report on Creating an Image Project Model
### This report describes how the Image Project Model is created and stored in the main branch of the GitHub repository server

## Milestone 1 
- This Milestone creates the GitHub repository in GitHub server and copies the repository to local desktop folder using following command: 
"git clone https://github.com/udslk/Computer_Vision.git"

## Milestone 2
- This milestone creates the Computer Vision System that detects whether the user is showing Rock, Scissors, Paper or Nothing 
- This system creates an image project model with different four classes: Rock, Scissors, Paper and Nothing
-  It uses "Teachable-Machine" from "https://teachablemachine.withgoogle.com/" to create the Classes
-  Each class is trained with images of the user showing each option to the camera. 
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
## Conclusion

- The milestone 2 shows how the Computer Vision System is created using the "Teachable-Machine" from "https://teachablemachine.withgoogle.com/"
- This System creates two important files, one for the image model called keras_model.h5 and other one for labels called labels.txt. 
- These two files are stored in GitHub repository
- These two files will be used in the Python application in later Milestones 