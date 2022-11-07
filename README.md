#            Face Detection Using Viola-Jones Object Detection Framework


```
      AKASH GHIMIRE     BIJAY PARIYAR    KESHAV ADHIKARI      THAPA PRADIP

        12194814           12194945          12194874           12194940
        
```
## Project Objective:

In this project we implement the face-based object detection algorithm proposed by Viola and Jones (2001). This Project uses Haar Cascade technique along with adaBoost training system for face detection by taking hundreds of positive face images with respect to thousands of negative non-face images.  

Face detection employs classifiers, which are algorithms that determine whether something in a picture is a face(1) or not a face (0). To improve accuracy, classifiers have been trained to recognize faces in tens of thousands to millions of photo. Haar Cascade is one of the most common classifiers in OpenCV.     


## Haar Cascade:

The Haar Cascade classifier divides the pixels in the image into squares depending on their functions using the Haar Wavelet approach. The "features" that are detected are computed using "integral image" principles. The Ada-boost learning algorithm is used by Haar Cascades, which picks a small number of crucial features from a huge set to get an effective output. Cascading techniques are then used by classifiers to recognize faces in images. Some Haar-Features are listed below.


![image](https://github.com/team-spiders/images/blob/main/face%20detection%201.png)



## Datasets:

There are two types of data set we have used for this project:

I) _**Custom dataset**_:
      
For custom dataset we have used Q51 13 megapixels camera, in order to maintain picture quality and capture several images per minute we have used photo burst application.


 
 For custom dataset we have divided each team members image dataset into 6 sub folders of 6 challenging aspects of object detection according to the variations and orientations and illumination conditions:


1) ***Viewpoint variation***
![image](https://github.com/team-spiders/images/blob/main/face%209%20viewpoint.png)


2)***Deformation***
![image](https://github.com/team-spiders/images/blob/main/face%2014%20deformation.png)

3) ***Occlusion***
![image](https://github.com/team-spiders/images/blob/main/face%2010%20occlusion.png)


4) ***Illumination conditions***
![image](https://github.com/team-spiders/images/blob/main/face%2012%20illumination.png)

5) ***Cluttered or textured background***
![image](https://github.com/team-spiders/images/blob/main/face%2011%20cluttered.png)

6) ***Intra class variation***
![image](https://github.com/team-spiders/images/blob/main/face%2013%20intra-class.png)



we have taken various wide range as well as short range images along with vertical orientations.



![image](https://github.com/team-spiders/images/blob/main/face%202.png)



## **Positive and Negative Images**



*In our case, for positive images we have taken self made face images into account, and for negative images we have taken images of non-face object that are available inside of our houses*.

A positive image is one containing an object that must be detected.

![image](https://github.com/team-spiders/images/blob/main/face%207.png)

For example,  the above figure is the examples of our custom-made positive images that we will be putting as an object that needs to be detected using classifier.

---------------------------------------------------------------------------------

And a negative image is everything else which we don't have to detect.

 ![image](https://github.com/team-spiders/images/blob/main/face%208.png)
 
 *above mentioned figure represents custom made negative images*

 
 ## II) Public Dataset:

1. ***Positive Samples***
```
a:  CelebA Dataset

b: 10,177 of identities

c: 202,599 Samples of Faces

d: Variation: Eyeglasses, Hat, Bangs. Different emotion,and so on.
```
2. ***Negative Sample***
```
a: Datasets from kaggle

b: Datasets involves relevant pictures in the
surrounding like furniture,vegetables, Notebooks and so on.  
```
 

## **DATA PREPROCESSING** 

***Custom positive dataset***

![image](https://github.com/team-spiders/images/blob/main/FACE%203.png)


*Public  Positive Dataset*

Except Augmentation all the preprocessing step is same as that of Custom Positive Dataset preprocessing.



*Negative Samples*

All the Negative samples were converted to gray scale and cropped to same size as that of positive training samples

## Code Snippets for Positive Dataset Preprocessing

 --------------------------------------------------------------------------------------- 

i) augmentation

![image](https://github.com/team-spiders/images/blob/main/face%204.png)


***Each image is augmented to further increasing the training samples size as well as to add***

-------------------------------------------------------------------------------------------

ii) conversion of RGB to Grayscale

![image](https://github.com/team-spiders/images/blob/main/face%205.png)
 
 ***Convert image from RGB to Grayscale***
 
 ---------------------------------------------------------------------------------------
 
 iii) Shuffling the custom positive samples and cropping
 
 ![image](https://github.com/team-spiders/images/blob/main/face%206.png)
 
 ***the above 1st information shows Before the train and test split of the dataset images are randomly shuffled for fair evaluation.similarly, followed by  pretrained haar cascade is used to cropp the faces from each sample positive images. Then each image is resized to (96,96) size. Only train datasets are cropped not the test***


----------------------------------------------------------------------------------

## *contribution of team member*
 
| TEAM MEMBER  | STUDENT ID  | CONTRIBUTION  |
|------------- | ----------- | ----------    |
| Akash Ghimire|   12194814  |  Haar Cascade classifier training, evaluation & testing |
| Bijay pariyar | 12194945   |  Data-set collection and report writing |
| Keshav Adhikari | 12194874 | GitHub related work and management |
| Pradip Thapa | 12194940    |  Environment setup and research  |


