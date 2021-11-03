<h1 align="center">Collaborative Development of Data Explorer Web App</h1>

## Description
This interactive Python web application is built using Streamlit and hosted in a Docker container. The app allows a user to upload a CSV file and to perform some EDA (exploratory data analysis) on it.

## Authors
* Darren Li
* Jason Nguyen
* Liam Huang
* Nick Drage

## Structure
```
.
├── app
│   └── streamlit_app.py			<- contains the main code to run the streamlit EDA app
├── src
│   ├── test
│   │   ├── test_data.py			<- contains code to test class Dataset
│   │   ├── test_datetime.py			<- contains code to test class DateColumn
│   │   ├── test_numeric.py			<- contains code to test class NumericColumn
│   │   └── test_text.py			<- contains code to test class TextColumn
│   ├── __init__.py				<- marks the directory of the package src
│   ├── data.py					<- contains code to construct class Dataset
│   ├── datetime.py				<- contains code to construct class DateColumn
│   ├── numeric.py				<- contains code to construct class NumericColumn
│   └── text.py					<- contains code to construct class TextColumn
├── docker-compose.yml				<- contains instructions to build a docker image for the app
├── dockerfile					<- contains instructions to build a docker image for the app
├── README.md					<- contains general information of the project
└── requirements.txt				<- specifies the required packages and their versions
```

## Instructions
CLI:  
	1. `cd \path\to\the\project_folder`: changes a current working directory to the project folder  
	2. `docker build -t streamlit_assignment03:latest .`: builds a docker image called *streamlit_assignment03* with the tag *latest*  
	3. `docker run -dit --rm --name eda_app -p 8501:8501 -v "${PWD}":/app streamlit_assignment03:latest`: creates a container called *eda_app* from the image built in step 2

## Notes
Use `csse_covid_19_daily_reports_us_01-01-2021.csv` or `dummy_trim.csv` to test the app's functionalities.

*(Written by jason and Liam)*
