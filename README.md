# AWS IoT Cloud Solutions

This repository documents my journey through the **ALX AWS Cloud Computing Program (C9)**, enhanced with **IoT-focused projects**.

It combines structured AWS Academy learning materials with real IoT integration examples, resulting in a professional portfolio that bridges **embedded systems** and **cloud architecture**.

---


##  Program Context
- **Provider**: ALX in partnership with AWS Academy 
- **Duration**: 6 Months (20–30 hrs/week) 
- **Certifications**: 
  - AWS Certified Cloud Practitioner 
  - AWS Certified Solutions Architect – Associate 

- The program covers AWS fundamentals, cloud economics, architecture, security, and real-world labs. 
=======
##  Program Context
- **Provider**: ALX in partnership with AWS Academy
- **Duration**: 6 Months (20–30 hrs/week)
- **Certifications**:
  - AWS Certified Cloud Practitioner
  - AWS Certified Solutions Architect – Associate

The program covers AWS fundamentals, cloud economics, architecture, security, and real-world labs.

I am aligning this with my **IoT background** (ESP32, BL602, BLE, MQTT, FreeRTOS) to build **IoT–Cloud solutions**.

---

##  Repo Structure

```
aws-iot-cloud-solutions/
│
├── phase1-cloud-practitioner/       # Weeks 1–9
│   ├── week01-intro-cloud-computing/
│   │   ├── README.md                # Week 1 summary (Cloud Concepts)
│   │   ├── notes-week1.md
│   │   ├── aws-docs-scout.md
│   │   └── caf-overview.md
│   └── ...
│
├── phase2-solutions-architect/      # Weeks 9–19
│   └── ...
│
├── capstone-project/                # Weeks 20–22
│   └── ...
│
├── docs/                            # Cheatsheets & references
│   ├── aws-cli-cheatsheet.md
│   ├── boto3-cheatsheet.md
│   ├── mqtt-guide.md
│   ├── glossary.md
│   └── resources.md
│
├── scripts/                         # Automation scripts
│   ├── setup-aws-cli.sh
│   ├── deploy-lambda.sh
│   └── clean-s3-bucket.py
│
├── .gitignore
└── README.md
```

---

##  Week 1 Progress (Cloud Foundations – Introduction)
Based on:
- *AWS Academy Cloud Foundations Course Introduction (v2.0.15)*
- *AWS Academy Cloud Foundations Module 01 – Cloud Concepts Overview (v2.0.13)*

### Key Learnings
- **Cloud Computing**: On-demand IT resources via Internet, pay-as-you-go.
- **Six Advantages of Cloud**: Cost model shift, economies of scale, agility, capacity management, stop running DCs, global reach.
- **Service Models**: IaaS / PaaS / SaaS.
- **Deployment Models**: Cloud / Hybrid / On-Prem.
- **AWS Core Service Categories**: Compute, Storage, Databases, Networking, Security, Monitoring.
- **Cloud Adoption Framework (CAF)**: Business, People, Governance, Platform, Security, Operations.
- **AWS Documentation Practice**: Located EC2, S3, Lambda, Cloud9 docs and ran a “Hello World” serverless example.

---


##  Resources
- [AWS Overview Whitepaper](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)  
- [AWS CAF Whitepaper](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf)  
- [AWS Docs](https://docs.aws.amazon.com/)  
- [AWS Pricing Overview](https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf)  

---

##  Resources
- [AWS Overview Whitepaper](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)
- [AWS CAF Whitepaper](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf)
- [AWS Docs](https://docs.aws.amazon.com/)
- [AWS Pricing Overview](https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf)

---

##  Next Steps

- Week 2 → **Cloud Economics & Billing**
- Extend repo with cost simulation scripts (S3 vs DynamoDB storage costs for IoT telemetry).
- Start first IoT → AWS integration test: ESP32/BL602 publishing to AWS IoT Core → DynamoDB.

---


