import streamlit as st
from main import generate_response

st.set_page_config(
    page_title="RAG application using GROQ API",
    page_icon="./assets/ΛV.png",
    layout="wide"
)

# Initialize the session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role" : "ai", "content" : "Hi There, how can I help you?"}]


# create the widget hierarchy
st.title("RAGGLES", anchor=False)
st.write("A personlised RAG Bot for easy access to your data")
base_con = st.container(border=False)
option_con , chat_con = st.columns([1,1])
with option_con.container(border=True):
    # file_uploader = st.file_uploader(
    #     label="PDF Uploader",
    # )
    st.header("""
                This is a simple RAG application that helps you to query your data.
                This application to be specific is implicitly equipped with a certain data which will serve as the knowledge base for it's retrieval process.
""")
    st.link_button(
        label="Follow me on LinkedIn",
        url="www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=abhivandan-radhakrishnan-275a04226"
    )
    st.link_button(
        label="Get the Source",
        url="www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=abhivandan-radhakrishnan-275a04226"
    )
with chat_con.container(height= 450, border=True):
    dialogue = st.container(height=400, border=False)
    with dialogue:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        if user_prompt := chat_con.chat_input("Ask me anything...."):
            
            # Conversation Logic here
            with st.spinner(text="Generating Response..."):
                response = generate_response(query=user_prompt).response

            # Display the query and response
            st.chat_message("user").write(user_prompt)
            st.chat_message("ai").write(response)

            # Update Session State
            st.session_state.messages.append(
                {"role" : "user", "content" : user_prompt}
            )
            st.session_state.messages.append(
                {"role" : "ai", "content" : response}
            )