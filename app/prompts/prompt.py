from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

system_prompt = """
you are expert in giving response of users questions
Give Text string response
here is users question:{question}
"""

prompt = ChatPromptTemplate.from_messages(
  [
    ("system",system_prompt),
    ("user","{question}")
  ]
)