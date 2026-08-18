# Image Comparison Tool

### Requirements for install:
  - Python 3.12.5
  - Microsoft Visual Studio Code

### Install:
  - Clone the repo: 
    - https://github.com/User/Repo
  - Create Virtual Environment
    -Hit (Ctrl + Shift + P) then type "Python: Create Environment" and select it then select .venv then 3.12. It should prompt you to install the requirements.txt file. Please select this to save the next step.

### Run the Program
  - Navigate to the cloned github directory on your computer then go into the "src" directory
  - Activate your virtual environment
    - Usually automatically activates, if not make your way to your virtual environment directory then run "activate"
  - Run the command
    - "python main.py"

### Program instructions
  - This is an image comparison tool, where a user can upload a "golden" picture and a batch of up to 20 other pictures, then compare them manually or use an algorithm to determine if they are similar.
  - Click "Upload Golden" and select an image to display your golden image
  - Click "Upload Batch" and select up to 20 images to display your batch images. Navigate between them with the arrows under the batch image viewer.
  - Click "Similar" or "Dissimilar" to manually grade images, or click "Algorithm" to have an algorithm make a guess
  - Under the menu bar at the top, there are some options:
    - Save will allow you to save a .json file including the index, image path, and if the images were similar or not. It also includes the path to the golden image
    - Auto will go through every uploaded image and use the algorithm to grade them all. This will not preserve manually graded images
    - Load will take your saved .json file and load it into the program so you can look through and grade the images again. 
      - This only works if the file paths are not changed since the save.