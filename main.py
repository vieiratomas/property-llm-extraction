import json
from src.api.client import create_llm_client
from src.models.schemas import Property
from src.templates.prompt_templates import prompt
from src.prompt_examples.examples import tool_example_to_messages
from src.prompt_examples.examples_data import examples

def run_extraction(transcript_string, messages):
    llm = create_llm_client()
    runnable = prompt | llm.with_structured_output(
        schema=Property,
        method="function_calling",
        include_raw=False
    )

    property_schema = runnable.invoke({"text": transcript_string, "examples": messages})

    return property_schema.json()

def generate_messages_from_examples(examples):
    messages = []
    for text_, tool_call in examples:
        messages.extend(
            tool_example_to_messages({"input": text_, "tool_calls": [tool_call]})
        )
    return messages

def save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":

    transcript_path = "data/transcripts/transcript_2.txt"
    file_path = "data/output/property_schema_2.json"

    with open(transcript_path, 'r') as file:
        transcript_string = file.read()

    messages = generate_messages_from_examples(examples)
    
    property_schema_json = run_extraction(transcript_string, [])
    save_to_file(property_schema_json, file_path)
