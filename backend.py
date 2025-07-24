from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import sys
import os

# Add the parent directory to path so we can import from splitwise_gemini_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your existing Splitwise agent
from splitwise_gemini_agent.main import agent_executor

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    try:
        # Process the message using your existing agent
        response = agent_executor.invoke({"input": message.message})
        return {"response": response.get("output", "I didn't understand that.")}
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        return {"response": f"Error: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)