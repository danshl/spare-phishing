# Spear Phishing Project

## Project Overview

This project aims to simulate a spear phishing attack by leveraging social engineering techniques and advanced natural language processing capabilities. Spear phishing is a targeted attempt to steal sensitive information, such as account credentials or financial information, from a specific individual, often for malicious reasons, by masquerading as a trustworthy entity.

## Project Description

The project is divided into two main parts: the attack simulation and the machine learning model detection.

### Part 1: Attack Simulation

The core objective of this part is to automate the creation of personalized phishing messages. The project performs the following steps:

1. **Company User Extraction:**
   - Given a username or identifier of a company, the system extracts from Facebook a list of individuals who work at the company.
     
2. **Post Extraction:**
   - For each extracted individual, the system retrieves their latest social media post.
   - 
3. **Personalized Message Creation:**
   - Using ChatGPT, the system generates a personalized phishing message for each individual based on their most recent post.

#### Example

Here is a brief example of how the attack simulation works:

1. **Input:**
   - Company Identifier: `example_company`

2. **Process:**
   - Extracted Employee: `John Doe`
   - Latest Post: "Just completed a successful project on cybersecurity!"

3. **Output:**
   - Personalized Message: 
     ```
     Hi John,

     Congratulations on your recent success in cybersecurity! 
     As a fellow enthusiast, I came across a new tool that could enhance your future projects.
     Check it out here [malicious link].

     Best,
     [Fake Name]
     ```

### Part 2: Using the External Dataset for Training and Evaluation

In this section, we utilize the dataset provided by Gaggle to train and evaluate the model. The provided code is designed to be easily run in Google Colab, making it convenient for users to replicate the training process. Additionally, you can use this code to test the model with your own personal emails.

#### Folder Structure
- `trained_model/`: This folder contains the trained model files after the training process is completed.

#### Steps to Follow

1. **Dataset**:
    - Ensure you have `emails.csv` in your working directory. This dataset will be used to train and evaluate the model.
2. **Running the Code**:
    - It is recommended to run `spare_detection_model.py` in [Google Colab](https://colab.research.google.com/) for the best experience and ease of use.
    - The script will first create and train the model using the `emails.csv` dataset.
3. **Testing with Personal Emails**:
    - The code also includes instructions on how to input your own emails for testing.
    - This allows you to see how well the model performs on data outside the provided dataset.

