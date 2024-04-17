import json
from api_client import create_llm_client
from schemas import Property
from prompt_templates import prompt

def run_extraction(transcript_path):
    llm = create_llm_client()
    runnable = prompt | llm.with_structured_output(
        schema=Property,
        method="function_calling",
        include_raw=False
    )

    with open(transcript_path, 'r') as file:
        transcript_string = file.read()

    property_schema = runnable.invoke({"text": transcript_string, "examples": []})

    return property_schema.json()

def save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    transcript_path = "transcripts/transcript_6.txt"
    file_path = "output/property_schema_6.json"
    
    property_schema_json = run_extraction(transcript_path)
    save_to_file(property_schema_json, file_path)
