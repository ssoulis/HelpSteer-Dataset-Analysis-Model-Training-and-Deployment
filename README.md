# HelpSteer-Dataset-Analysis-Model-Training-and-Deployment


## Getting Started

* [Introduction](#introduction)
* [Project Overview](project-overview)
* [Dataset](dataset)
* [Project Structure](#project-structure)
* [Milestones](#milestones)
* [API](#api)


## Introduction
This project is designed to analyze the HelpSteer Dataset, build a regression model to predict the complexity of text responses, and deploy the solution as a Dockerized API. It is structured to assess skills in data exploration, machine learning, and deploying solutions in real-world environments.

## Project Overview

The project is divided into three milestones:
-Exploratory Data Analysis (EDA): Analyze the dataset to understand attribute correlations and data distribution.
-Regression Model Development: Train and evaluate a model to predict the "complexity" attribute using embedding techniques and evaluate performance.
-API and Deployment: Package the trained model into a RESTful API and deploy it using Docker for seamless interaction.

## Dataset

The HelpSteer Dataset, hosted on HuggingFace, provides textual data for analysis and modeling. It can be accessed here![alt text](https://huggingface.co/datasets/nvidia/HelpSteer).

## Project Structure

1. notebooks/: Contains Jupyter Notebooks for EDA and model training.
2. api/: Source code for the RESTful API.
3. Dockerfile: Configuration for containerizing the API and its dependencies.
4. README.md: This document.

## Milestones
1. Exploratory Data Analysis (EDA)
  Objective: Understand dataset characteristics and explore relationships between attributes.
  Tasks:
    -Load and preprocess the dataset.
    -Perform correlation analysis and visualize results using a heatmap.
    -Deliverable: Annotated Jupyter Notebook with insights and visualizations.
2. Regression Model Development
  Objective: Predict the complexity attribute of text responses.
  Tasks:
    -Feature engineering using embedding techniques.
    -Split data into training and testing sets.
    -Train regression models and evaluate using RMSE and MAE.
    -Deliverable: Jupyter Notebook with training and evaluation pipelines.
3. API Development and Deployment
  Objective: Deploy the regression model for real-time predictions.
  Tasks:
     -Develop a RESTful API for user interaction.
     -Dockerize the API for easy deployment.
  Deliverables:
    -Dockerfile for building the container.
    -API source code.
    -Documentation with usage instructions.


## API

The API accepts 2 input in text format the prompt and the response
![alt text](https://github.com/ssoulis/HelpSteer-Dataset-Analysis-Model-Training-and-Deployment/blob/main/example1.png)





