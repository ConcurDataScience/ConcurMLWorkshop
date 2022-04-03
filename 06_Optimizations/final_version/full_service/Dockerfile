#####
# DOCKERFILE
#####
#   This Dockerfile specifies how to create a docker image for the ml service using ubuntu
#   as the base image. It installs python3, creates a service user, and installs all python
#   requirements needed.
#####
# HOW TOs:
# - Build: docker build . -t mlservice
# - Build ignoring cache: docker build -t mlservice --no-cache .
# - Running the service: docker run -p 8080:8080 mlservice:latest
# - Starting a interactive shell inside the image: docker run -it mlservice:latest /bin/bash
#####
# FUTURE STEPS:
# - Minimize the number of layers and follow best practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# - For SAP Concur projects, make sure to use a compliant base image: https://github.concur.com/cbi/python
# - Follow image hardening and security guidelines:
#     - SAP Concur Docker-Hardening-Standards: https://github.concur.com/containerhosting/image-hardening/tree/master/docs/external/application-developer/Docker-Hardening-Standards
#     - SAP Global Security Best Practices: https://wiki.wdf.sap.corp/wiki/display/itsec/SAP+Global+Security+Good+Practices
#         - How to develop a secure Container Application: https://wiki.wdf.sap.corp/wiki/display/itsec/How+to+develop+a+secure+Container+Application?src=sidebar
#         - How to handle privileged Container Applications: https://wiki.wdf.sap.corp/wiki/display/itsec/How+to+handle+privileged+Container+Applications?src=sidebar
#         - Security Recommended Container Base Images: https://wiki.wdf.sap.corp/wiki/display/itsec/Security+Recommended+Container+Base+Images?src=sidebar
#     - SAP Global Security Procedures: https://wiki.wdf.sap.corp/wiki/display/itsec/SAP+Global+Security+Procedures?src=sidebar
#         - Docker Engine - Hardening: https://wiki.wdf.sap.corp/wiki/display/itsec/Docker+Engine+-+Hardening?src=sidebar
####

# In this class, we will use ubuntu base images, but in our production service,
# we use compliant base images provided by SAP concur, usually based on Red Hat.
FROM ubuntu:20.04

# Let's update the package list from ubuntu's repositories
RUN apt-get update

# Make sure we have python 3.X installed
RUN apt-get install -y curl python3 python3-pip

# Install tf-serving
RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
    curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
RUN  apt-get update && apt-get install -y tensorflow-model-server

# Remove the apt-get cache to save space in the image
RUN apt-get clean

# We don't want to run the application as root, so we will create a service user
RUN groupadd -r servicegroup && useradd -r -g servicegroup -m -d /app service

# Switch to our service user
USER service

# Install the project requirements using pip3 as the service user
RUN pip install --user flask nltk "tensorflow>=2.6.1"

# Install the NLTK data
RUN python3 -m nltk.downloader stopwords wordnet omw-1.4

# Create the app folder and copy the repository files
COPY . /app

# Switch to the /app dir
WORKDIR /app

# Add an command to be executed when the docker container starts
CMD /bin/bash ./start.sh

# Expose the 8080 port
EXPOSE 8080
