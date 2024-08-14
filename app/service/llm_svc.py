from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

base_prompt_template = "You are a helpful assistant that responds to user's input."
translator_prompt_template = "You are a helpful assistant that translates every user's input from italian to english."

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", translator_prompt_template),
        ("human", "{user_input}"),
    ]
)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


def generate_response(user_input: str) -> str:
    for chunk in (prompt | llm).stream({"user_input": user_input}):
        yield chunk
