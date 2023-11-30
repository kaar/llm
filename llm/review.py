from llm import ChatRequest, ChatResponse, Models, SystemMessage, UserMessage, chat_completion


def diff(
    diff: str,
    model: str = Models.DEFAULT_MODEL,
    temperature: float = 0.2,
) -> str:
    """
    This function takes a git diff as input and returns a code review
    as output.
    """
    instruction = """
You will receive a git diff.
Respond with a code review of the commit.
Look for bugs, security issues, and opportunities for improvement.
Provide short actionable comments with examples if needed.
If no issues are found, respond with "Looks good to me".
Use markdown to format your review.
"""
    response: ChatResponse = chat_completion(
        request=ChatRequest(
            model=model,
            messages=[
                SystemMessage(instruction),
                UserMessage(diff),
            ],
            temperature=temperature,
        )
    )
    return response.message.content


def code(
    code: str,
    model: str = Models.DEFAULT_MODEL,
    temperature: float = 0.2,
) -> str:
    instruction = """
Respond with a code review of the commit.
Look for bugs, security issues, and opportunities for improvement.
Provide short actionable comments with examples if needed.
Use markdown to format your review.
"""
    response = chat_completion(
        request=ChatRequest(
            model=model,
            messages=[
                SystemMessage(instruction),
                UserMessage(code),
            ],
            temperature=temperature,
        )
    )
    return response.message.content
