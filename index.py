import subprocess
from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from twilio.rest import Client

app = FastAPI()


#class PromptRequest(BaseModel):
#    data: str

@app.post("/generate/")
async def generate_text(Body: str = Form(...), From: str = Form(...)):
    prompt_text = Body
    account_sid = '{AccountSID}'
    auth_token = '{Account_auth_token}'
    client = Client(account_sid, auth_token)


    try:
        # Ollama CLI to generate a response
        result = subprocess.run(
            ["ollama", "run", "llama3.2", "--", prompt_text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        # Return the response from the Ollama CLI
        response_text = result.stdout.strip()
        message = client.messages.create(
                from_='+18603564557',
                body=response_text,
                to=From
        )

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error calling Ollama: {e.stderr}")

    if not response_text:
        raise HTTPException(status_code=500, detail="Failed to generate response")

    return message
