# Enterprise Knowledge Base Q&A System (RAG) using Amazon Bedrock

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Question-Answering system built using **Amazon Bedrock Knowledge Bases**. It enables users to query internal company documents using natural language and receive accurate, context-aware responses grounded in proprietary data.

The system overcomes limitations of traditional keyword-based search and reduces hallucinations in Large Language Models by combining semantic retrieval with LLM-based answer generation.

---

## Features

* Semantic search over internal documents
* Accurate, context-aware answers using RAG
* Fully managed retrieval using Amazon Bedrock Knowledge Bases
* Streamlit-based interactive web interface
* Secure deployment using AWS EC2 with IAM roles
* No external APIs (data remains within AWS)

---

## Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python (Boto3)
* **LLM:** Amazon Bedrock (Claude model)
* **RAG Engine:** Bedrock Knowledge Bases
* **Cloud:** AWS EC2, S3, IAM

---

## Architecture

1. User enters a question via Streamlit UI
2. Query is sent to Amazon Bedrock Knowledge Base
3. Relevant document chunks are retrieved using vector search
4. LLM generates a grounded response based on retrieved context
5. Final answer is displayed to the user

---

## Project Structure

```
project/
│── app.py
│── requirements.txt
│── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd <project-folder>
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Variables

Update in `app.py`:

```
KNOWLEDGE_BASE_ID = "YOUR_KB_ID"
REGION = "us-east-1"
```

---

## Running the Application

### Local Run

```
streamlit run app.py
```

### EC2 Deployment

```
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Access:

```
http://<EC2-PUBLIC-IP>:8501
```

---

## IAM Permissions Required

Ensure EC2 instance role includes:

* `bedrock:*`
* `bedrock-agent-runtime:*`
* `s3:*` (restricted to your bucket)

---

## Example Queries

* What is the company leave policy?
* How can I apply for reimbursement?
* What are the benefits offered to employees?
* Explain onboarding process

---

## Key Advantages

* Eliminates irrelevant keyword-based search results
* Reduces hallucination by grounding responses in real data
* Scalable and fully managed RAG implementation
* Secure handling of enterprise data

---

## Limitations

* Requires properly configured Knowledge Base
* Accuracy depends on quality of uploaded documents
* Initial setup in AWS can be complex

---

## Future Enhancements

* Add citation display for retrieved sources
* Chat history support
* Document upload from UI
* Role-based access control

---

## Conclusion

This project demonstrates a production-ready implementation of RAG using Amazon Bedrock Knowledge Bases, enabling organizations to unlock value from internal data through intelligent, conversational search.

---
