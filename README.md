############################################################################################
Project Name: CapstoneFinalProject
Programe: Cloud DevOps Nano-Degree (Udacity)

Submitted By: Prashant Kumar Tripathi
Date of Submission: 18 July 2022

this project is using below tools and technologies

1) AWS 
2) GitHUB: version control tool
3) CircleCI to Implement Continuous Integration and Continuous Deployment
4) Building Docker containers in pipelines
5) Building Kubernetes clusters
6) Python

#########################################################################################
Steps to Deply my Application
#########################################################################################


Step-1) Tested docker file using hadolint

Step-2) Build Docker image for python flask app and upload docker Hub

Step-3) Create Kubernetes cluster in AWS (EKS) 

Step-4) Create Service as loadbalancer and web hosts for  high availability

Step-5) Deploy a docker container from a docker HUB 

Step-5) Application is deployed and running on EKS cluster

Step-6) Now...there is an update to the webpage and it has to be re-deployed. Just to minimsse the downtime for the users I am using rolling update strategy. 
It is a gradual process that allows you to update your Kubernetes system with only a minor effect on performance and no downtime. In this strategy, the Deployment selects a Pod 
with the old programming, deactivates it, and creates an updated Pod to replace it.

Step-7) Take backup and use the tagging approach to TAG the docker image as V1,V2,V3 etc. So in case of roll back can change the build order version and 
re-apply the settings
   
Step-8) v1 tag is old-application, v2 tag us updated version 

Step-9) Once the v2 is ready, push it to docker hub with v2 tag. Modify the Kubernetes configuration to pull
    updated version, then add the rolling strategy configuration so whenvever a changes in application it uses
    rolling update strategy to redeploy a update code

Step-10) CircleCI is being used to deploy the latest version by pulling the code gitrepo

###########################################################################################
Output (ULRs)
###########################################################################################

GitHub Url: https://github.com/tripathi011/Project5-CapStone-Prashant

