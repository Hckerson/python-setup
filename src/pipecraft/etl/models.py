from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    PositiveInt,
)


class Row(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    email: EmailStr = Field(min_length=1)
    amount: PositiveInt
    created_at: str
