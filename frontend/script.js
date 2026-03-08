// Khởi tạo thư viện Flatpickr cho ô nhập ngày tháng
flatpickr("#date_time", {
    dateFormat: "d/m/Y", // Tự động ép chuẩn định dạng cho Prompt n8n 
    defaultDate: "today", 
    disableMobile: "true" // Giữ giao diện đẹp trên mọi thiết bị
});

// Bắt sự kiện khi người dùng bấm nút submit form
document.getElementById('journalForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // Tránh việc trình duyệt tải lại trang

    const submitBtn = document.getElementById('submitBtn');
    const resultBox = document.getElementById('resultBox');

    // 1. Đổi trạng thái nút bấm để báo hiệu hệ thống đang chạy
    submitBtn.innerText = "⏳ AI đang quán chiếu...";
    submitBtn.disabled = true;
    resultBox.classList.add('hidden'); // Ẩn kết quả cũ đi

    // 2. Gom dữ liệu từ các ô nhập liệu
    const payload = {
        ngay_thang: document.getElementById('date_time').value,
        tieu_de: document.getElementById('title').value,
        noi_dung: document.getElementById('content').value
    };

    try {
        // 3. Gửi POST request sang FastAPI
        const response = await fetch('http://localhost:8000/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`Lỗi server: ${response.status}`);
        }

        const data = await response.json();
        
        // 4. Vẽ kết quả ra màn hình
        renderResult(data);

    } catch (error) {
        alert("Có lỗi xảy ra khi kết nối với AI: " + error.message);
    } finally {
        // 5. Trả lại trạng thái ban đầu cho nút bấm
        submitBtn.innerText = "Phân Tích Bằng AI";
        submitBtn.disabled = false;
    }
});

// Hàm phụ trợ để in dữ liệu JSON ra giao diện HTML đẹp mắt
function renderResult(data) {
    const resultBox = document.getElementById('resultBox');
    
    // Biến mảng cảm xúc thành các thẻ (tag) HTML
    const emotionsHtml = data.cam_xuc_chinh.map(em => `<span class="emotion-tag">${em}</span>`).join('');

    // Đổ nội dung vào thẻ div resultBox
    resultBox.innerHTML = `
        <h3>Kết quả quán chiếu 🧘</h3>
        <div class="result-item">
            <strong>Nguyên nhân cốt lõi:</strong>
            <p>${data.nguyen_nhan_cot_loi}</p>
        </div>
        <div class="result-item">
            <strong>Gợi ý chánh niệm:</strong>
            <p>${data.goi_y_chanh_niem}</p>
        </div>
        <div class="result-tags">
            ${emotionsHtml}
        </div>
    `;
    
    // Bỏ class 'hidden' để hiện cái hộp lên
    resultBox.classList.remove('hidden');
}