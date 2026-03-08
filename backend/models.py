from pydantic import BaseModel, Field

class JournalInput(BaseModel):
    date_time: str = Field(
        ...,
        description="Date of journal entry",
        examples=["2024-01-15"],
    )

    title: str = Field(
        '',
        description="Journal entry's title",
        example="Một ngày tuyệt vời",
        max_length=30
    )

    content: str = Field(
        ...,
        description="Content of journal entry",
        example="Hôm nay là một ngày rất đẹp trời...",
        min_length=1,
        max_length=10000
    )

    class Config:
        schema_extra = {
            "example": {
                "ngay_thang": "2024-01-15",
                "tieu_de": "Nhật ký ngày đầu tuần",
                "noi_dung": "Hôm nay tôi đã bắt đầu tuần mới với nhiều năng lượng..."
            }
        }
