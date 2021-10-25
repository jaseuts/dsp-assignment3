<h1 align="center">Collaborative Development of Data Explorer Web App</h1>

## Description
This interactive Python web application is built using Streamlit and hosted in a Docker container. The app allows a user to upload a CSV file and to perform some EDA (exploratory data analysis) on it.

## Authors
* Darren Li
* Jason Nguyen
* Liam Huang
* Nick Drage

# Structure

# Instructions
Bash Command: 
	1. use 'cd' command, change the path to folder dsp-assignment3 
	2. $ docker build -t streamlit_assignment03:latest .
	3. $ docker run -dit --rm --name assignment03_2 -p 8501:8501 -v "${PWD}":/app streamlit_assignment03:latest
Step to stop docker:
	1. $ docker stop assignment03_2
Order to rebuild app:
	1. stop docker
	2. run the script under Bash Command (2 and 3)

# Notes
1. Use 'csse_covid_19_daily_reports_us_01-01-2021.csv' or 'dummy_trim.csv' to do the premilinary run