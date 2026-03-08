from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class JournalEntry(Base):
    __tablename__ = "journals"

    # Khóa chính 
    id = Column(Integer, primary_key=True, index=True)
    
    # Dữ liệu người dùng nhập vào
    date_time = Column(String, nullable=False)
    title = Column(String, nullable=True)  # Cho phép bỏ trống
    content = Column(Text, nullable=False)
    
    # Kết quả phân tích từ AI (n8n)
    emotions = Column(String, nullable=True) # Lưu dạng chuỗi cách nhau bằng phẩy: "tức giận, mất kiểm soát"
    root_cause = Column(Text, nullable=True)
    mindfulness_advice = Column(Text, nullable=True)
    
    # Dấu thời gian hệ thống tự động ghi nhận lúc lưu
    created_at = Column(DateTime, default=datetime.now)