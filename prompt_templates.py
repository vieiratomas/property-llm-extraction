from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized extraction algorithm trained to analyze real estate descriptions. "
            "Your task is to identify and extract specific property details from the provided text accurately. "
            "Extract attributes like location, number of bedrooms, bathrooms, floor number, elevator access, and parking availability. "
            "If an attribute is not mentioned in the text, you should return 'null' for that attribute. "
            "Focus on the precision and relevance of the information extracted."
        ),

        MessagesPlaceholder("examples"),
        
        ("human", "{text}"),
    ]
)