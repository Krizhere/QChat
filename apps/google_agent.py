
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st

load_dotenv()

# Initialize the web search tool
search = GoogleSerperAPIWrapper()

# Initialize the LLM
llm = ChatGroq(model="openai/gpt-oss-120b",streaming=True)

# Create a proper LangChain tool
from langchain_core.tools import Tool

search_tool = Tool(
    name="WebSearch",
    func=search.run,
    description="Search the web for current information."
)

#Memory Saver
if "memory" not in st.session_state:
    st.session_state.memory = InMemorySaver()
    st.session_state.history = []

# Create the agent
agent = create_agent(
    model=llm,
    tools=[search_tool],
    checkpointer=st.session_state.memory,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the WebSearch tool when current information is needed."
    )
)

st.title("Qchat: Response made faster")

# Display chat history
for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


#input from user
query=st.chat_input("Ask me anything!")
if query:

    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query}) #chat history of user

    response = agent.stream({
        "messages": [
            {"role": "user", "content": query}
        ]},
        {"configurable": {"thread_id":"1"}},
        stream_mode="messages"
    )

    ai_container = st.chat_message("Ai")
    
    with ai_container:
        space=st.empty()
        message=""

        for chunks in response:
            message=message+chunks[0].content
            space.write(message)

    
    # answer=response['messages'][-1].content
    # st.chat_message("Ai").markdown(answer)
        st.session_state.history.append({"role": "Ai", "content": message}) #chat history of ai
