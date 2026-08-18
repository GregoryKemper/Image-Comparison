# Image Comparison Tool

### Requirements
- Python 3.12.5
- Microsoft Visual Studio Code
- Python extension for VS Code

### Install
- Clone the repo:
  - https://github.com/GregoryKemper/Image-Comparison
- Open the project folder in VS Code.
- Create a virtual environment with Command Palette:
  - Press `Ctrl + Shift + P`
  - Run `Python: Create Environment`
  - Choose `Venv`
  - Choose Python `3.12`
  - Select `requirements.txt` when prompted to install dependencies

### Activate Virtual Environment (if VS Code does not auto-activate)
- PowerShell:
  - `./venv/Scripts/Activate.ps1` (or `./.venv/Scripts/Activate.ps1`)
- Git Bash:
  - `source venv/Scripts/activate` (or `source .venv/Scripts/activate`)

### Run the Program
- From the project root directory, run:
  - `python src/main.py`

### Program Instructions
- This is an image comparison tool where a user uploads one golden image and a batch of up to 20 other images, then compares them manually or with an algorithm.
- The app supports color images only.
- Click `Upload Golden` and select an image.
- Click `Upload Batch` and select up to 20 images.
- Use `Previous` and `Next` to move through the batch.
- Click `Similar` or `Dissimilar` to manually rate the current image.
- Click `Algorithm` to run comparison on the current image.

### Menu Bar Actions
- `Save` writes a JSON file containing:
  - each batch image `id`, `path`, and `similarity`
  - the golden image path under `golden_image.path`
- `Auto` runs the algorithm across the entire currently loaded batch (this overwrites prior manual ratings for those images).
- `Load` reads a previously saved JSON file and reloads images/ratings.
  - Image file paths must still exist at the same locations.