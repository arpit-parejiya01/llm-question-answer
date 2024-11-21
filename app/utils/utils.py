import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from app.prompts.prompt import prompt


load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chain=prompt | llm | StrOutputParser()