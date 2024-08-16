from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


def generate_response(user_input: str) -> str:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that responds to everything the user wants"),
            ("human", "{user_input}"),
        ]
    )
    for chunk in (prompt | llm).stream({"user_input": user_input}):
        yield chunk
