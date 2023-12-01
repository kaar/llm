from openai import OpenAI
from openai.types import chat

from .models import ChatRequest, ChatResponse

# ChatCompletionMessageParam = Union[
#     ChatCompletionSystemMessageParam,
#     ChatCompletionUserMessageParam,
#     ChatCompletionAssistantMessageParam,
#     ChatCompletionToolMessageParam,
#     ChatCompletionFunctionMessageParam,
# ]


def chat_completion(request: ChatRequest) -> ChatResponse:
    # messages: list[dict] = [
    #     {
    #         "role": message.role,
    #         "content": message.content,
    #     }
    #     for message in request.messages
    # ]
    client = OpenAI()
    # messages_to_send: list[chat.ChatCompletionMessageParam]
    # for message in request.messages:
    #     messages_to_send.append({"role": "content", "content": ""})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
    )

    # ChatCompletionMessageParam = Union[
    #     ChatCompletionSystemMessageParam,
    #     ChatCompletionUserMessageParam,
    #     ChatCompletionAssistantMessageParam,
    #     ChatCompletionToolMessageParam,
    #     ChatCompletionFunctionMessageParam,
    # ]

    # openai_messages = [
    #     {
    #         "role": message.role,
    #         "content": message.content,
    #     }
    #     for message in request.messages
    # ]
    # movie: Movie = {"name": "Inception", "year": 2010}
    # response = client.chat.completions.create(
    #     model=request.model,
    #     # messages=[
    #     #     {
    #     #         "role": message.role,
    #     #         "content": message.content,
    #     #     }
    #     #     for message in request.messages
    #     # ],
    #     temperature=request.temperature,
    # )

    # return ChatResponse(**response)
