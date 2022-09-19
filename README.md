Training the model
    The model is trained in Google Colab. The file (RTFSC Training.ipynb) is uploaded in to the GitHub directory. Run the cells in the order, following the explanation in the file.
How to run the code?
    1.	Download the rtfsc from GitHub
    GitHub Link: https://github.com/Harikrishnan-Vijayan/rtfsc.git
    2.	Download the video for testing from Google Drive to the above floder
    Google Drive Link: https://drive.google.com/drive/folders/1zeAeG00g-alVaN_bGQQ0rFe8TzUX-wj8?usp=sharing
    3.	Set up the environment as per the requirements, install anaconda, CUDA, PyTorch and MySQL
    4.	Open an anaconda terminal in the downloaded folder
    5.	Install requirements.txt in the environment
    >>pip install requirments.txt
    6.	Then run server.py in an anaconda terminal. Keep the program running
    >>python server.py
    7.	Open another anaconda terminal and run camera_1.py with the required arguments
    >> python camera_1.py --weights best.pt --img 416 --conf 0.1 –source video1.mp4
    In which,
    camera_1.py: the program name
    --weight: the trained model (best.pt)
    --source: location of the input file
    --img: images size
    --conf: confidence threshold

    The report (report.txt) will be generated in the same folder after the completion of execution.
