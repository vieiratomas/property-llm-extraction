from typing import List, TypedDict
import uuid
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
from schemas import Property  # Import the Property model here

class Example(TypedDict):
    """A representation of an example consisting of text input and expected tool calls."""
    input: str
    tool_calls: List[Property]

def tool_example_to_messages(example: Example) -> List[BaseMessage]:
    """Convert an example into a list of messages for a language model."""
    messages: List[BaseMessage] = [HumanMessage(content=example["input"])]
    openai_tool_calls = []
    for tool_call in example["tool_calls"]:
        openai_tool_calls.append(
            {
                "id": str(uuid.uuid4()),
                "type": "function",
                "function": {
                    "name": tool_call.__class__.__name__,
                    "arguments": tool_call.dict(),  # Use .dict() instead of .json() for pydantic models
                },
            }
        )
    messages.append(
        AIMessage(content="", additional_kwargs={"tool_calls": openai_tool_calls})
    )
    tool_outputs = example.get("tool_outputs") or ["You have correctly called this tool."] * len(openai_tool_calls)
    for output, tool_call in zip(tool_outputs, openai_tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
    return messages
