# 🌿 Mindfulness AI Journal (Nhật Ký Tĩnh Tâm)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ed)
![n8n](https://img.shields.io/badge/n8n-Workflow-ff6c37)
![Gemini](https://img.shields.io/badge/AI-Gemini_2.5_Flash-8e43e7)

Một ứng dụng web ghi chú nhật ký kết hợp Trí tuệ Nhân tạo (AI). Hệ thống tự động phân tích nội dung người dùng nhập vào để trích xuất cảm xúc chính, tìm ra nguyên nhân cốt lõi làm xao động tâm trí, và đưa ra các lời khuyên thực hành chánh niệm (mindfulness) phù hợp.

Dự án được thiết kế với kiến trúc Microservices, đóng gói hoàn toàn bằng Docker để đảm bảo khả năng triển khai "1-click" trên mọi môi trường.

---

## 🚀 Tính năng nổi bật
* **Giao diện tối giản (Vanilla JS/CSS):** Tập trung vào trải nghiệm viết nhật ký không phân tâm.
* **Tích hợp n8n Workflow:** Quản lý luồng xử lý AI (Prompt Engineering) tách biệt hoàn toàn khỏi code Backend.
* **AI Analysis (Gemini 2.5):** Phân tích ngôn ngữ tự nhiên, trả về dữ liệu chuẩn JSON (Structured Output).
* **Tự động lưu trữ (SQLite):** Lưu giữ lịch sử nhật ký và kết quả quán chiếu từ AI.
* **Containerization (Docker):** Toàn bộ Frontend, Backend và hệ thống n8n được đóng gói và giao tiếp qua mạng nội bộ bảo mật.

---

## 🏗️ Kiến trúc Hệ thống

Dự án gồm 3 dịch vụ (services) chạy song song:
1. **Frontend (Nginx):** Phục vụ giao diện người dùng tại cổng `8080`.
2. **Backend (FastAPI):** Xử lý API, lưu trữ vào SQLite và giao tiếp với n8n tại cổng `8000`.
3. **AI Engine (n8n):** Orchestrator xử lý Prompt và gọi sang Google Gemini API tại cổng `5678`.

---

## 🛠️ Hướng dẫn Cài đặt & Triển khai (Local)

### Yêu cầu hệ thống
* Đã cài đặt [Docker](https://www.docker.com/) và Docker Compose.
* Có sẵn 1 API Key của Google Gemini (Lấy miễn phí tại [Google AI Studio](https://aistudio.google.com/)).

### Bước 1: Khởi động hệ thống
Clone repository này về máy và chạy lệnh khởi tạo vũ trụ Docker:
```bash
git clone https://github.com/huynhtiennhat0403/ai-journal-tracker
cd ai-journal-tracker
docker compose up --build -d
```

### Bước 2: Thiết lập luồng AI (n8n)
Lần đầu tiên chạy hệ thống, bạn cần nạp luồng cấu hình AI vào n8n:

1. Truy cập vào http://localhost:5678 và tạo một tài khoản quản trị nội bộ.

2. Tại màn hình chính, chọn Import from File.

3. Chọn file n8n_setup/diary-demo.json có sẵn trong mã nguồn.

4. Mở node HTTP Request trong luồng vừa nạp, thay thế đoạn NHAP_API_KEY_CUA_BAN_VAO_DAY bằng Gemini API Key của bạn.

5. Nhấn vào button "Publish" góc trên bên phải của luồng.

### Bước 3: Trải nghiệm
* Giao diện Web: http://localhost:8080
* Tài liệu API (Swagger UI): http://localhost:8000/docs