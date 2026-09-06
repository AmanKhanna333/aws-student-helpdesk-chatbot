# AWS Lex — Student Helpdesk Chatbot

An AI-powered university student helpdesk chatbot built on Amazon Lex V2.
Built as a 4-person team project with IAM-based role separation.

## 🌐 Live Site
d3oejv7116hqdi.cloudfront.net

## 📄 Project Report
See `StudentHelpdeskBot_ProjectReport.pdf` for full documentation.

## Team & Roles

| Member | Role | Responsibility |
|---|---|---|
| Aman Khanna | Cloud Architect | IAM, Lambda, API Gateway, CloudFront, Integration |
| Krithika | Intent Developer | Exam and Library intents + utterances |
| Moksha | Response Designer | All bot responses and FallbackIntent |
| Harihar | Frontend Developer | UI design decisions and S3 hosting |

## Features
- 20 intents covering 6 student query categories
- Subject-specific exam details (CN, CC, DBMS, AI/ML, OOPS)
- Branch-specific admissions (CSE, ECE, ME, CE, MBA, MCA)
- Multi-turn conversation — bot follows up with subject menu
- Fee structure for all programs
- Campus services (hostel, transport, canteen)
- Intelligent FallbackIntent with help menu
- IAM least-privilege access for team collaboration

## Architecture
