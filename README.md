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

```python
python label.py Lab10-Tweet-MN.png
```

The result shows that the image is principally related to Technology, Font, Engineering, Electronic device and cable management which is almost correct. A great advantage is that we don't have to code complex algorithms, we only have to use what is working fine!

![8.1.2](Images/8.3.InitialTest.PNG)

#### 8.3.4 Classify images

This section of the lab consists on scraping images from a website related to a topic of our preference and analyze it using Cloud Vision API in order to get insights about the topic's profile and content. For this purpose, we decided to find information about our favorite topic __Peru__

Since we had some problems scrapping from Twitter and Pinterest, we decided to use the following website full of images: [gettyimages.es](https://www.gettyimages.es/fotos/peru?mediatype=photography&phrase=peru&sort=mostpopular)



#### Q81: What problems have you found developing this section? How did you solve them?

Firstly, when we tried to create a Google Account, we had problems to validate our credit cards. Google accounts doesn't accept prepaid cards. We had to change to other mean of payment.

Moreover, we tried to scrap images from Twitter or Pinterest with the __scrapy__ library, but we found problems since the "scrapy robots" were blocked because we didn't have the authorization. In the case of twitter, we should preferably use the library we learned at the begining of the course __tweepy__ or __twitterscraper__ .  At the end, we decided to scrap from a different website to ease the process.
 

#### Q82: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them?