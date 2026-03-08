from fastapi import FastAPI

app = FastAPI(
    title="Mindfulness Journal API",
    description="API tự động phân tích cảm xúc nhật ký bằng Prompt Engineering & n8n"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mindfulness Journal API!"}