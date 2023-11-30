from openai import OpenAI

from .models import ChatRequest, ChatResponse

client = OpenAI()


def chat_completion(request: ChatRequest) -> ChatResponse:
    messages: list[dict] = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in request.messages
    ]

    response = client.chat.completions.create.create(
        model=request.model,
        messages=messages,
        temperature=request.temperature,
    )

    return ChatResponse(**response)
