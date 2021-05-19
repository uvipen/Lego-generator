# [PYTHON] Lego generator

**New Idea**: Duplicate the lego piece and directly add it to the image, it will remove all the ugly part in spliting the image into piece like the original impl. I'll try it tomorrow

## Introduction

Here is my python source code for Lego generator. To the best of my knowledge, my code is the shortest one you could find out for this goal. With my code, you could: 

* **Given input image, you could generate Lego art stored under image formats (.png, .jpg, ...)**
* **Given input video, you could generate Lego art stored under video formats (.avi, .mp4, ...)**


## Video to video
By running the sript **video2video.py**, we will have following output:
<p align="center">
  <img src="demo/output.gif" width=800><br/>
  <i>Output video</i>
</p>


## Image to image
By running the sript **image2image.py**, we will have following outputs:
<p align="center">
  <img src="demo/output.jpg" width=800><br/>
  <img src="demo/english_output.jpg" width=800><br/>
  <img src="demo/german_output.jpg" width=800><br/>
  <img src="demo/japanese_output.jpg" width=800><br/>
  <img src="demo/french_output.jpg" width=800><br/>
  <img src="demo/korean_output.jpg" width=800><br/>
  <img src="demo/russian_output.jpg" width=800><br/>
  <img src="demo/spanish_output.jpg" width=800><br/>
  <i>Output images</i>
</p>


## Requirements

* **python 3.6**
* **cv2** 
* **numpy**
