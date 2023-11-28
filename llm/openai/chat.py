import openai

from .models import ChatRequest, ChatResponse


def chat_completion(request: ChatRequest) -> ChatResponse:
    messages: list[dict] = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in request.messages
    ]

    response = openai.ChatCompletion.create(
        model=request.model,
        messages=messages,
        temperature=request.temperature,
    )

    return ChatResponse(**response)
