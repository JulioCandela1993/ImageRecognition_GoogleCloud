# Lab session #8: Advanced Analytics as a Service in the Cloud

In this lab we use Google Cloud Platform in order to take advantage of the numerous analytical APIS already implemented by Google. 

## Group Information
* Candela Caceres, Julio Christians (julio.christians.candela@est.fib.upc.edu)
* Maatouk, Karim (karim.maatouk@est.fib.upc.edu)

## Task 8.1: Google Cloud Vision

#### 8.3.1 Cloud Platform sign up

In order to harness the benefits of Google Cloud Platform for Computer Vision we need to set up the initial environment which includes enabling the Cloud Vision API, create a bucket accessible for all users and, finally, create the credentials to connect directly from Python. The advantages of these machine learning APIs is that offers powerful and simple tools to perform complex anallytical tasks.

1) Enable Cloud Vision API: You can go to API & Services in the left panel and select library. Then type the name of the API and enable it in your project.

![8.1.1](Images/8.1.1.Vision.PNG)

2) Create a bucket and change to permissions to be accessed by everyone.

![8.1.1](Images/8.1.1.Bucket.PNG)

3) Create the credentials which will allows to call the API from an external programming environment (Python)

![8.1.1](Images/8.1.1.Credentials.PNG)

#### 8.3.2 Python environment setup

The first step is to download the python scripts from the reposiroty: https://github.com/CCBDA-UPC/google-cloud-vision-example.git cloud-vision
As soon as we have the scripts, we can activate the python environment and add all the libraries required to manage google services. The file requirements includes all the python libraries

```
pip install -r requirements.txt
```

Additionally, we need to create an environmental variable which will contain the path of the credenials json:
- SET GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json (Microsoft) or also set as a system/user variable and restart the computer
- export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json (Linux)

#### 8.3.3 Quick Start: Running the Example

In this section, we are going to test the Cloud Vision service with a demo image extracted from twitter. We have to execute the python script with the image path as an argument.

```
python label.py Lab10-Tweet-MN.png
```

The result shows that the image is principally related to Technology, Font, Engineering, Electronic device and cable management which is almost correct. A great advantage is that we don't have to code complex algorithms, we only have to use what is working fine!

![8.1.2](Images/8.3.InitialTest.PNG)



