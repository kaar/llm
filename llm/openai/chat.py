import openai

from .models import ChatCompletionResponse, ChatRequest


def chat_completion(request: ChatRequest) -> ChatCompletionResponse:
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

    return ChatCompletionResponse(**response)
