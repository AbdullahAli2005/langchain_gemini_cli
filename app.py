import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

llm= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=api_key,
)

prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the question: {question}"
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    output_parser=StrOutputParser(keep_whitespace=False)
)

print("🤖 Gemini CLI is ready! Type your question or 'exit' to quit.\n")
while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("Exiting Gemini CLI. Goodbye!")
        break
    response = chain.run(question=question)
    print("\nAI:", response, "\n")