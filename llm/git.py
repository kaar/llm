from llm import ChatRequest, Models, SystemMessage, UserMessage, chat_completion


def commit_msg(
    input_diff: str,
    history: list,
    model: str = Models.DEFAULT_MODEL,
    temperature: float = 0.2,
) -> str:
    """This function takes a git diff as input and returns a git commit message"""

    COMMIT_INSTRUCTION = """
You will receive a git diff and respond with a git commit message.
Provide a clear and concise commit message that summarizes the changes made in this diff.
Separate subject from body with a blank line.
Limit the subject line to 50 characters.
Capitalize the subject line.
Do not end the subject line with a period.
Use the imperative mood in the subject line.
Wrap the body at 72 characters.
Use the body to explain what and why vs. how.
"""
    history = history or []

    system_message = SystemMessage(COMMIT_INSTRUCTION)
    input_message = UserMessage(input_diff)

    response = chat_completion(
        request=ChatRequest(
            model=model,
            messages=[
                system_message,
                *history,
                input_message,
            ],
            temperature=temperature,
        )
    )
    return response.message.content
