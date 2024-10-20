
# smsGPT
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
