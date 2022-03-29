# Packing and Deploying ML models using Python and Docker 

## Summary

This class aims to produce an API for serving inference results using Flask based on the trained model.
We will pack the service into a docker image that can run as a local container.

By the end of the session, participants will have a GitHub repository with their service code and a docker file capable of creating the docker image with the service and model baked into it. 

## Setup

Participants will need to download the saved model and pre/post-processing code created in the previous workshop sessions. 

Also, in their local environment, they need to have the following tools:
- A python 3.8 environment (an anaconda environment, for example)
- docker
- Some Python IDE (Pycharm, VScode, etc.)
- Postman

Link to each of the tools used can be found in the useful links section.
  
## Tasks

### Part 1: Develop a Rest API using Flask to serve the models results

#### Description:
Let's write an API to receive requests from our customers and send back the model predictions.

#### Artifacts:
- service/*
- main.py

#### Topics:
- What is a REST API, and why use it?
- Service architecture overview
- Writing the main.py file and starting the Flask server
- Writing the pre-process and post-process code
- Loading the model and making predictions
- Writing schemas using marshmallow
- Testing the service with Postman

### Part 2: Running the service code as a Docker container

#### Description: 
This session will demonstrate how to create a docker image and run the service in a container.

#### Artifacts:
- Dockerfile

#### Topics:
- What is Docker, and why using it?
- Demonstration on how to build a docker image for the service
- Running the container and testing it using Postman

### Part 3: Demonstrate how our deployment pipeline works at SAP Concur

#### Description: 
During the last part of the class, we will show how the data science team deploys services to our production environments in SAP Concur.

#### Artifacts:
- SAP Concur - Data Science team deployment overview

#### Topics:
- Step-by-step datascience deployment workflow overview

## Outputs

All artifacts created during the session can be downloaded via the following public GitHub repository:  [ConcurMLWorkshop](https://github.com/ConcurDataScience/ConcurMLWorkshop/tree/main/05_Service_Building)

## Useful links

- **Downloading docker:** https://www.docker.com/products/docker-desktop/
- **Download postman:** https://www.postman.com/downloads/
- **Anaconda:** https://www.anaconda.com/products/distribution
- **Obtaining pycharm:** https://www.jetbrains.com/pycharm/download/#section=mac
- **Visual Studio Code download:** https://code.visualstudio.com/download
- **Creating a new environment with Anaconda:** https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands 
