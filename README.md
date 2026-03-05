# IaC-provisioning-Non-profit-System
### Group No:	D6 – Group 04D6
### Project No: DO-15
---
## Project Description
This project focuses on automating the infrastructure provisioning for a Non-Profit Support System using Infrastructure as Code (IaC). By leveraging tools like Terraform, Docker, and Kubernetes, the system eliminates manual configuration errors and ensures a consistent, scalable, and repeatable deployment environment.

The infrastructure is automatically created using scripts that configure the required services and deploy the application environment. This automation enables rapid system setup and simplifies infrastructure management.
The project demonstrates how modern DevOps practices can be used to deploy and manage applications efficiently.

---
## Project Overview

The system acts as a bridge between application deployment requirements and infrastructure setup.
A CI/CD pipeline triggers automated infrastructure provisioning and deployment when code is pushed to the repository.
The system uses:
Terraform to provision infrastructure
Docker to containerize applications
Kubernetes to orchestrate containers
GitHub Actions / Jenkins to automate deployment
The entire lifecycle from code commit to application deployment is managed automatically.

---
## Objectives

Automation  : Replace manual server configuration with automated infrastructure provisioning using code.

Consistency : Ensure that development, testing, and production environments remain identical.

Scalability : Enable the system to handle increasing workloads by dynamically scaling containers using Kubernetes.

Reliability : Reduce configuration errors and ensure reliable deployments using version-controlled infrastructure.

---
## Tech Stack
| Category                     | Tools / Technologies            |
| ---------------------------- | ------------------------------- |
| **Infrastructure as Code**   | Terraform                       |
| **Containerization**         | Docker                          |
| **Orchestration**            | Kubernetes                      |
| **CI/CD Pipeline**           | GitHub Actions / Jenkins        |
| **Version Control**          | Git, GitHub                     |
| **Cloud / Local Deployment** | AWS or Local Docker Environment |

---
## Key Features
Automated Infrastructure : Infrastructure is created automatically using Terraform scripts.

Containerized Applications : Applications run inside Docker containers for portability and consistency.

CI/CD Automation : GitHub Actions or Jenkins automatically builds, tests, and deploys the application.

Scalable Architecture : Kubernetes enables automatic scaling and management of containers.

Version Controlled Infrastructure : Infrastructure configuration is stored in Git, allowing easy tracking of changes.

---
## Group Members
| Name             | Enrollment No |
| ---------------- | ------------- |
| Riddhima Taose   | EN22CS303042  |
| Naman Dwivedi    | EN22CS301627  |
| **Neha Tamboli** | EN22CS301641  |
| Rohan Rawat      | EN23CS3L1016  |
| Uday Patidar     | EN23CS3L1023  |

---
## Conclusion
The IaC Provisioning for Non-Profit System demonstrates how modern DevOps practices can automate infrastructure management and application deployment. By replacing manual configuration with Infrastructure as Code, the system becomes more reliable, scalable, and easier to maintain. This project highlights the importance of automation, containerization, and CI/CD pipelines in building efficient and scalable systems.
