# 🚀 Two-Tier Web Application with Jenkins CI/CD

A simple two-tier web application built with **Flask and MySQL**, containerized using **Docker and Docker Compose**, and deployed on **AWS EC2** using a **Jenkins CI/CD pipeline**.

This project is part of my journey into learning **DevOps, CI/CD, Docker, Jenkins, and AWS**.

---

## 🏗️ Architecture

```text
                  GitHub
                    │
                    │ Push Code
                    ▼
                 Jenkins
              (AWS EC2)
                    │
                    │ CI/CD Pipeline
                    ▼
             Docker Compose
              ┌─────────────┐
              │             │
              ▼             ▼
        Flask Container  MySQL Container
             :5000
              │
              ▼
           Application