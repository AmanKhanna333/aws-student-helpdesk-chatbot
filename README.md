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

| Service | Role |
|---|---|
| Amazon Lex V2 | NLU engine — 20 intents, natural language processing |
| AWS Lambda (Python) | Connector between API Gateway and Lex |
| Amazon API Gateway | POST /chat endpoint with CORS |
| Amazon S3 | Hosts the chat interface frontend |
| Amazon CloudFront | HTTPS delivery via CDN |
| AWS IAM | 3 team IAM users with least-privilege policies |

## Intent Categories

| Category | Intents | Built by |
|---|---|---|
| Exam Schedule | ExamScheduleIntent, ExamDetailIntent | Aman |
| Subject Exams | CN, CC, DBMS, AIML, OOPS intents | Aman |
| Courses | CourseDetailsIntent | Moksha |
| Admissions | AdmissionIntent + 6 branch intents | Moksha |
| Fees | FeeStructureIntent | Moksha |
| Library | LibraryIntent | Krithika |
| Campus | CampusServicesIntent | Krithika |
| Fallback | FallbackIntent | Moksha |

## Key Concepts Practiced
- Amazon Lex V2 intent design with 15+ utterances per intent
- Multi-turn conversation without Lambda slot filling
- IAM least-privilege team collaboration
- Serverless Lambda connector in Python using boto3
- API Gateway CORS for cross-domain browser requests
- CloudFront HTTPS in front of S3
- Debugging IAM authentication issues for team members
