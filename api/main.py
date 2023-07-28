import os

import openai
from fastapi import FastAPI
from dotenv import load_dotenv

from .models import OpenAIBody, OpenAIResponse

app = FastAPI()

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


@app.post("/query")
async def make_query(body: OpenAIBody) -> OpenAIResponse:
    chat_completion = await openai.ChatCompletion.acreate(
        model=body.open_ai_model,
        messages=[
            {
                "role": "system",
                "content": "Supply only the Ubuntu command for the following statements. "
            },
            {
                "role": "user",
                "content": body.statement
            }
        ]
    )

    chat_response = None
    ok_response = False
    if len(chat_completion["choices"]) >= 1:
        ok_response = True
        chat_response = chat_completion["choices"][0]["message"]["content"]

    return OpenAIResponse(
        ok_response=ok_response,
        command=chat_response
    )
