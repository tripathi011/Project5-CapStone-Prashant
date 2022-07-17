#####################################################################################################
Project Name: CapstoneFinalProject
Programe: Cloud DevOps Nano-Degree 

Submitted By: Prashant Kumar Tripathi
Date of Submission: July 2022
#####################################################################################################

In this Project I am using below sets: 

1) AWS 
2) GitHUB: version control tool
3) CircleCI to Implement Continuous Integration and Continuous Deployment
4) Building Docker containers in pipelines
5) Building Kubernetes clusters
6) Python

#######################################################################################################
Steps to Deply my Application
#######################################################################################################


Step-1) Tested docker file using hadolint

Step-2) Build Docker image for python flask app and upload docker Hub

Step-3) Create Kubernetes cluster in AWS (EKS) 

Step-4) Create Service as loadbalancer and web hosts for  high availability

Step-5) Deploy a docker container from a docker HUB 

Step-5) Application is deployed and running on EKS cluster

Step-6) Now, there is an update to the webpage and it has to be re-deployed. The challenge is what type of deployment strategy needed to use
so that the clients faces the minimal downtime. In this application I am using rolling update strategy. It is a gradual process that allows 
you to update your Kubernetes system with only a minor effect on performance and no downtime.In this strategy, the Deployment selects a Pod 
with the old programming, deactivates it, and creates an updated Pod to replace it.

Step-7) Firstly, as a best practice ensure to take a backup of old application either using version control etc
Here I have used to tagging approach to TAG the docker image as Green/Blue. So in case of roll back can change the build order version and 
re-apply the settings
   
Step-8) Green tag is old-application, Blue tag us updated version 

Step-9) Once the Blue is ready, push it to docker hub with Blue tag. Modify the Kubernetes configuration to pull
    updated version, then add the rolling strategy configuration so whenvever a changes in application it uses
    rolling update strategy to redeploy a update code

Step-10) CircleCI is being used to deploy the latest version by pulling the code gitrepo

#######################################################################################################
Output (ULRs)
#######################################################################################################

