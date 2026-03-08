// Khởi tạo thư viện Flatpickr cho ô nhập ngày tháng
flatpickr("#date_time", {
    dateFormat: "d/m/Y", // Tự động ép chuẩn định dạng cho Prompt n8n của bạn
    defaultDate: "today", // Mở lên là tự động điền ngày hôm nay
    disableMobile: "true" // Giữ giao diện đẹp trên mọi thiết bị
});