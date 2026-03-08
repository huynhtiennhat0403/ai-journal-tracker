from pydantic import BaseModel, Field, ConfigDict

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

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "date_time": "2024-01-15",
                "title": "Nhật ký ngày đầu tuần",
                "content": "Hôm nay tôi đã bắt đầu tuần mới với nhiều năng lượng..."
            }
        }
    )