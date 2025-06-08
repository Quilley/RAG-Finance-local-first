from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from function.chunker import chunk_text
from function.ingest import parse_document
from fastapi import UploadFile, File
from typing import List
from pathlib import Path
import uvicorn

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/api/ingestchunk')
async def ingest_chunk(file: UploadFile = File(...)):
    path = f"docs/{file.filename}"
    with open(path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    text = parse_document(path)
    chunks = chunk_text(text)

    return {"chunks": chunks[:3]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)