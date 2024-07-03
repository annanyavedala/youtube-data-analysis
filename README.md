# YouTube Trending Videos Analysis

Data Engineering YouTube Analysis Project 

This project focuses on collecting and analyzing structured and semi-structured data from YouTube videos. The goal is to conduct a thorough analysis based on video categories, geographic regions, and trending metrics.

Project walkthrough

- **AUTHENTICATION**: Setting up essential authentication and permissions using IAM USERS AND ROLES.
- **DATA INGESTION**: Developed a mechanism to ingest data from different sources into s3 buckets.
- **EXTRACT, TRANSFORM, LOAD**: Transform the raw data by performing necessary joins, removing null values and reformatting using Serde. 
These steps were undertaken using AWS GLUE, ATHENA and LAMBDA FUNCTIONS.
- **DATA LAKE**: We store data that we obtain from multiple sources into a centralized data lake.
- **SCALABILITY**: As the size of our data increases, we make sure our system scales with it.
- **REPORTING**: Built a data dashboard that helps us leverage significant insights regarding youtube video metrics.


## AWS Services Used

- **Amazon S3**: Amazon S3 is an object storage service that provides industry-leading scalability, data availability, security, and performance.
- **AWS IAM**: Identity and Access Management (IAM) enables us to securely manage access to AWS services and resources.
- **Amazon QuickSight**: A scalable, serverless, and embeddable business intelligence (BI) service powered by machine learning, built for the cloud.
- **AWS Glue**: A serverless data integration service that simplifies discovering, preparing, and combining data for analytics, machine learning, and application development.
- **AWS Lambda**: A compute service that allows you to run code without provisioning or managing servers.
- **Amazon Athena**: An interactive query service for Amazon S3, allowing you to analyze data directly in S3 without needing to load it into a separate storage system.

## Dataset Used

This project utilizes a dataset from Kaggle containing statistics on daily popular YouTube videos over several months. Each day, up to 200 trending videos are recorded for various regions, with each region's data stored in its own CSV file. The dataset includes:
- Video title
- Channel title
- Publication time
- Tags
- Views
- Likes and dislikes
- Description
- Comment count
- A `category_id` field (which varies by region and is detailed in a corresponding JSON file)

This comprehensive dataset enables detailed analysis of YouTube's trending content across different regions and time periods.


https://www.kaggle.com/datasets/datasnaek/youtube-new

Architecture Diagram
 
