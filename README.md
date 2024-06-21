# Spear Phishing Project

## Project Overview

This project aims to simulate a spear phishing attack by leveraging social engineering techniques and advanced natural language processing capabilities.   
Spear phishing is a targeted attempt to steal sensitive information such as account credentials or financial information from a specific individual, often for malicious reasons, by masquerading as a trustworthy entity.

## Project Description

The core objective of this project is to automate the creation of personalized phishing messages. The project performs the following steps:

1. **Company User Extraction:**
   - Given a username or identifier of a company, the system extracts from facebook  a list of individuals who work at the company.
   
2. **Post Extraction:**
   - For each extracted individual, the system retrieves their latest social media post.
   
3. **Personalized Message Creation:**
   - Using ChatGPT, the system generates a personalized phishing message for each individual based on their most recent post.



## Example

Here is a brief example of how the project works:

1. **Input:**
   - Company Identifier: `example_company`

2. **Process:**
   - Extracted Employee: `John Doe`
   - Latest Post: "Just completed a successful project on cybersecurity!"

3. **Output:**
   - Personalized Message: 
     ```
     Hi John,

     Congratulations on your recent success in cybersecurity! As a fellow enthusiast, I came across a new tool that could enhance your future projects. Check it out here [malicious link].

     Best,
     [Fake Name]
     ```

## Conclusion

This project showcases the power of combining data scraping techniques with advanced language models like ChatGPT to create realistic and personalized spear phishing messages. The intent is to highlight the vulnerabilities in social media usage and the importance of maintaining robust cybersecurity practices.

