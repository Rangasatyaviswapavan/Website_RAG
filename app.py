import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from create_data import get_data_from_web
from dotenv import load_dotenv
load_dotenv()

def get_answer(query):
    return "give me money$$"


st.set_page_config(page_title="Website RAG",page_icon="🪦")
st.title("Chat with websites!!")
if "chat_history" not in st.session_state:
    st.session_state.chat_history= [
        AIMessage(content="Hi! gimme Money$$$"),
    ]


with st.sidebar:
    st.header("Website")
    url = st.text_input("url")
    key = st.text_input("open ai api key")
if url is None  or url =="" or key is None or key =="":
    st.info("Please Enter Details!!")
else:
    docs= get_data_from_web(url)
    with st.sidebar:
        st.write(docs)
    query = st.chat_input("Ask Website RAG...")
    if query is not None and query!="":
        answer= get_answer(query)
        st.session_state.chat_history.append(HumanMessage(content=query))
        st.session_state.chat_history.append(AIMessage(content=answer))
        
    for message in st.session_state.chat_history:
        if isinstance(message,AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message,HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
            
