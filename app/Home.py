import streamlit as st

from service.llm_svc import generate_response

st.title("LazyGPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Input a message"):
    st.chat_message("human").markdown(user_input)
    st.session_state.messages.append({"role": "human", "content": user_input})

    # process input with llm
    assistant_output_stream = generate_response(user_input=user_input)
    st.chat_message("assistant").write_stream(assistant_output_stream)
    st.session_state.messages.append({"role": "assistant", "content": assistant_output_stream})
