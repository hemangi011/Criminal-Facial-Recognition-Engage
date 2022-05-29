
# CRIMINAL FACIAL RECOGNITION

The program accepts an image from the user in the form of an uploaded file or a live picture from the web camera. It then compares the facial features to those in our dataset to check if any matches are found. 

# SETUP

Clone the repository or download the zip file and then install the necessary libraries and run the program using the command python manage.py runserver.

# DEPENDENCIES

This module relies on the following Python libraries:

1. OpenCV - to install open command prompt and execute the command pip install opencv-python

2. Numpy - to install open command prompt and execute the command pip install numpy

3. dlib - to install open command prompt and execute the command pip install dlib

4. face recognition - to install open command prompt and execute the command pip install face recognition

Once these libraries have been installed, the code can simply be run by running the command python manage.py runserver

# IMPLEMENTATION

In this program, the police officer logs in with their respective username and password. Then, they have the option to either upload the image of a criminal or click a real-time picture of the criminal which gets saved.

Then, the facial vector of the image of the criminal is compared with the facial vectors of the pre-existing criminals in the database. The closest match found is assumed to be the criminal.

Then, the personal details such as Name, Date of Birth, No. of cases etc. are displayed of the criminal.