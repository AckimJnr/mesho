
# EdgeAI
## Project Descript
Edge AI is a technology that introduces accessibility to Artificially intelligent Chabot's to all mobile platforms including  basic phones.

Users interact with Llamma3.2 light weight model through SMS service featured in almost every mobile phone.

The project aims to drive meaningful change by increasing accessibility to unlimited knowledge powered by llama3.2 models to all.

## How to Use

### 1. Start the FastAPI server with Uvicorn

First, ensure that you have `uvicorn` installed. Then, run the server:

---
```bash
uvicorn index:app --host 165.227.90.229 --port 8000
```
---

### 2. Make a Request using Curl
Once the server is running, you can interact with the API by making a POST request with curl. Here's an example:

---
```bash
curl -X 'POST'   'http://165.227.90.229:8000/generate/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{"prompt": "your prompt here"}'
```
---
