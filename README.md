# shadow_art_creator
This program converts regular videos into a shadow art version of the original video. 
The video background will be white, while the main subject will be filled in with black, resembling a shadow.
The project was inspired by the music video [Bad Apple](https://www.youtube.com/watch?v=FtutLA63Cp8).
I thought the style of art looked neat and so I tried making something similar.

## How it works
### Video to Images
In order to create the shadow art, the video must first be converted into images. 
The CaptureVideo method from the open CV library had to be used to capture the image sequence of a video file.

### Edge detection
For each Image, the edge of the focal point should be detected.
To do this, the Canny edge detection algorithm was used.
In order for the edge detector to work more effeciently, the image was converted into gray scale.
This also helped optomize the program by using less memory and sped up the whole process.

### Flooding
Each image was flood filled using the flood fill algorithm.
The seed point was in the top left corner, which is the starting point of the filling process.
The background is filled with white.

### Images to video
The final step of the process is gathering the images and converting them into a video file format.
After the filling of each image, the image (as a matrix) is appended to a list which contains the image sequence.
This image sequence is written one by one into a VideoWriter object from the open CV library.
After the whole image sequence is written, it is released in the file format selected.
