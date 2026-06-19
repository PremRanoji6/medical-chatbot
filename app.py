from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"

#loading the index

docsearch = PineconeVectorStore(
    index_name=index_name,
    embedding=embeddings,
    pinecone_api_key=PINECONE_API_KEY
)

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context","question"])

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})

retriever = docsearch.as_retriever(search_kwargs={"k": 2})

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

qa = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | PROMPT
    | llm
    | StrOutputParser()
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form.get("msg") or request.args.get("msg", "")
    if not msg:
        return "No message received", 400
    result = qa.invoke(msg)
    return str(result)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug= True)