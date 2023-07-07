from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(openai_api_key="OPENAI_API_KEY")
llm = OpenAI(temperature=0.5)

text = "hola chat gpyt estoy probando crear apps contigo :D gratis , puedo ? "
print(llm(text))