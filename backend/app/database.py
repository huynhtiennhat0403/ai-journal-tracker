import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Định nghĩa đường dẫn thông minh
# Lấy đường dẫn của thư mục chứa file hiện tại
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Đi lùi ra một cấp  rồi  vào thư mục data/
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")

# Nếu thư mục data chưa tồn tại thì tự động tạo mới
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Đường dẫn cuối cùng tới file DB
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(DATA_DIR, 'journal.db')}"

# 2. Khởi tạo Engine kết nối với SQLite
# Tham số check_same_thread=False cần thiết cho FastAPI khi dùng SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Tạo SessionLocal để mỗi request có một phiên làm việc riêng với DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Tạo Base class để các file models kế thừa
Base = declarative_base()

# 5. Hàm dependency để lấy session DB 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()