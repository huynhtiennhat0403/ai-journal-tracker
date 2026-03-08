from fastapi import FastAPI, HTTPException
import httpx
from backend.app.schemas import JournalInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mindfulness Journal API",
    description="API tự động phân tích cảm xúc nhật ký bằng Prompt Engineering & n8n"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

N8N_WEBHOOK_URL = "http://localhost:1234/webhook/diary"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mindfulness Journal API!"}

@app.post("/api/analyze")
async def analyze_journal(entry: JournalInput):
    payload = {
        "ngay_thang": entry.date_time,
        "tieu_de": entry.title,
        "noi_dung": entry.content
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(N8N_WEBHOOK_URL, json=payload)
            response.raise_for_status() 

            # Trả nguyên dữ liệu JSON từ n8n về cho Frontend
            return response.json()
        
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Lỗi từ n8n: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Không thể kết nối n8n: {e}")