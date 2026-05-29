# Disaster Recovery Mechanism in Cloud

This project demonstrates a Disaster Recovery system using:

- Active Storage Replication
- DNS Failover
- Azure Virtual Machines
- Django Web Application
- Nginx + Gunicorn Deployment

## Objective
To achieve high availability and automatic failover between primary and backup servers.

## Features
- Multi VM setup in Azure
- Automatic traffic switching
- Django-based web application
- PostgreSQL database integration
- Production deployment using Nginx + Gunicorn

## Architecture
- Primary VM (Production)
- Backup VM (CNR)
- DNS Failover System
- Load Balancer

## Tech Stack
- Azure Cloud
- Django (Python)
- Nginx
- Gunicorn
- PostgreSQL
- Linux (Ubuntu)

## How it Works
1. User connects via DNS
2. Request goes to active VM
3. Data is replicated to backup VM
4. If failure occurs → DNS redirects traffic