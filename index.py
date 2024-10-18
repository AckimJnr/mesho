import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate/")
async def generate_text(request: PromptRequest):
    prompt_text = request.prompt

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
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error calling Ollama: {e.stderr}")

    if not response_text:
        raise HTTPException(status_code=500, detail="Failed to generate response")

    return {"response": response_text}
