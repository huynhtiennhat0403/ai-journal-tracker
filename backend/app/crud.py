from sqlalchemy.orm import Session
from app import models
from app.schemas import JournalInput

def create_journal_entry(db: Session, entry: JournalInput, ai_result: dict|list):
    """
    Hàm này nhận dữ liệu nhật ký của người dùng và kết quả từ n8n,
    sau đó đóng gói lại và lưu vào database.
    """
    # 1. AI trả về mảng cảm xúc (ví dụ: ["tức giận", "buồn"]), 
    # ta nối nó thành một chuỗi "tức giận, buồn" để lưu vào cột String.

    data = ai_result[0] if isinstance(ai_result, list) else ai_result
    emotions_str = ", ".join(data.get("cam_xuc_chinh", []))
    
    # 2. Khởi tạo một đối tượng (Row) mới dựa trên model đã thiết kế
    db_journal = models.JournalEntry(
        date_time=entry.date_time,
        title=entry.title,
        content=entry.content,
        emotions=emotions_str,
        root_cause=ai_result.get("nguyen_nhan_cot_loi", ""),
        mindfulness_advice=ai_result.get("goi_y_chanh_niem", "")
    )
    
    # 3. Thêm vào phiên làm việc (Session) và lưu (Commit) xuống ổ cứng
    db.add(db_journal)
    db.commit()
    
    # 4. Làm mới đối tượng để lấy ID vừa được database tự động tạo ra
    db.refresh(db_journal)
    
    return db_journal