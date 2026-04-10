import streamlit as st
import boto3

# CONFIG 
KNOWLEDGE_BASE_ID = "KB123ABC45"
REGION = "us-east-1"

# Bedrock client (uses EC2 IAM role automatically)
client = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)

st.set_page_config(page_title="Enterprise Q&A", layout="wide")

st.title("📄 Enterprise Knowledge Base Q&A")

query = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if query:
        try:
            response = client.retrieve_and_generate(
                input={
                    "text": query
                },
                retrieveAndGenerateConfiguration={
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                        "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
                    }
                }
            )

            answer = response["output"]["text"]

            st.subheader("Answer:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")