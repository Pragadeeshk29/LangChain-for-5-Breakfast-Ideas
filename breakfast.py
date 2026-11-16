import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set in the .env file")

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = """
Give exactly 5 healthy south Indian breakfast ideas.
Format rules:
- Numbered list
- One line each
- No preamble
- No extra explanation
"""

reply = llm.invoke(prompt)
print(reply.content)
