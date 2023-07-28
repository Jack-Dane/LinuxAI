from pydantic import BaseModel


class OpenAIBody(BaseModel):
    statement: str
    open_ai_model: str


class OpenAIResponse(BaseModel):
    ok_response: bool
    command: str | None
