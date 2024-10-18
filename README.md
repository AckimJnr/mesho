
# smsGPT
## How to Use

### 1. Start the FastAPI server with Uvicorn

First, ensure that you have `uvicorn` installed. Then, run the server:

---
```bash
uvicorn index:app --host 0.0.0.0 --port 8000


### 2. Make a Request using Curl
Once the server is running, you can interact with the API by making a POST request with curl. Here's an example:

``bash 
curl -X 'POST' \
  'http://0.0.0.0:8000/generate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
```
---