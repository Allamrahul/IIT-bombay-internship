# IIT-bombay-internship
The code for both problem statements have been written in python using pycharm and opencv2.You will also need to have the face cascade
and eye cascade xml files and the oscar selfie code you are running in the same folder.You also need to have the image you
are toying with in the same folder.I have attached both the xml files.


Oscarselfie:
For the detection of face and eyes i have used the haar cascade xml files.Then the program would loop through all the detected faces.If the 
face gets detected,it would insert a bounding rectangle around the face.
As the objective was to get the RGB value of ellens eyes,i used the the xml file of eyes to detect them.Then i found out the centroid
of the bounding rectange around the eye using the coordinates of the bounding rectangle.
Now the only thing left is to get the RGB value which has been done using an inbuilt function.Refer code for further details.

Jellyfish:
As most of the jellyfish are purple in color inorder to detect them i used "cv2.inrange" function.After getting the binary mask i blurred
the image to remove the gaussian noise present.
Now for marking the jellyfish i find out all the contours that fall into the purple range.Now looping through each contour i found out
the area of every contour and only selected those whose area is above a particular threshold.I found out the centroid of each contour who
se area is above particular threshold.Outline of the contour area has been marked outlined by a green boundary detecting the jelly fish.
The centre has been marked with a red cross which was the intial problem statement to begin with.Refer code for further details.

Since my exams are going on ,i really dint have much time to make my code more efficient and robust.
