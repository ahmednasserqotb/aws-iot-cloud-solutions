
# Week 1 – Cloud Concepts Overview

##  What I Completed
- AWS Academy Cloud Foundations – Course Introduction (v2.0.15)
- Module 01 – Cloud Concepts Overview (v2.0.13)

##  Key Concepts
- **Cloud definition & benefits** (on-demand, pay-as-you-go, global scale)
- **Six advantages of cloud**: capex→opex, economies of scale, capacity planning, agility, stop running DCs, go global
- **Service models**: IaaS / PaaS / SaaS
- **Deployment models**: Cloud / Hybrid / On‑premises
- **AWS CAF perspectives**: Business, People, Governance, Platform, Security, Operations
- Navigating **AWS Docs & Whitepapers**

##  Hands-on
- Set up Git + SSH to GitHub
- Scaffolded repo and docs
- Installed AWS CLI and Python venv with boto3

##  Notes to Self
- Keep a running AWS CLI cheatsheet in `/docs/aws-cli-cheatsheet.md`
- Tie every concept back to IoT (device → MQTT → AWS → dashboard)
=======
# Week 1 – Notes

##  Modules Covered
- AWS Academy Cloud Foundations – Course Introduction (v2.0.15)
- AWS Academy Cloud Foundations – Module 01: Cloud Concepts Overview (v2.0.13)

---

### Cloud Computing
- On-demand IT resources delivered via the internet.
- Pay-as-you-go model, scalable, global.

### Six Advantages of AWS Cloud
1. Trade capital expense for variable expense.
2. Benefit from economies of scale.
3. Stop guessing capacity.
4. Increase speed and agility.
5. Stop managing data centers.
6. Go global in minutes.

### Service Models
- **IaaS** – Infrastructure as a Service (e.g., EC2, EBS).
- **PaaS** – Platform as a Service (e.g., Elastic Beanstalk).
- **SaaS** – Software as a Service (e.g., QuickSight).

### Deployment Models
- **Cloud** – Fully hosted on AWS.
- **Hybrid** – Mix of on-prem and AWS.
- **On-Premises** – Virtualized but not AWS.

### AWS Core Service Categories
- **Compute**: EC2, Lambda, ECS, EKS
- **Storage**: S3, EBS, EFS, Glacier
- **Databases**: RDS, DynamoDB, Redshift, Aurora
- **Networking & CDN**: VPC, Route 53, CloudFront
- **Security**: IAM, Cognito, KMS
- **Monitoring**: CloudWatch, CloudTrail

### AWS Cloud Adoption Framework (CAF)
- **Business**: Align IT with value.
- **People**: Skills and organizational change.
- **Governance**: Risk, compliance, portfolio mgmt.
- **Platform**: Architecture, provisioning, dev practices.
- **Security**: Identity, access, protection, compliance.
- **Operations**: Monitoring, incident response.

---

##  Hands-On
- AWS Docs Scavenger Hunt (EC2, S3, IoT Core, Lambda runtimes, Cloud9).
- Lambda Hello World tutorial.
- CLI commands:
  ```bash
  aws configure
  aws sts get-caller-identity
  aws s3 ls
  ```

---

##  Insights
- Cloud adoption is a business enabler, not just cost reduction.
- CAF ensures cloud adoption touches people, governance, and operations, not only technology.
- Navigating AWS Docs is a crucial skill for both certification and real-world projects.

---

##  References
- [AWS Docs Home](https://docs.aws.amazon.com/)
- [AWS Overview Whitepaper](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)
- [AWS CAF Whitepaper](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf)

