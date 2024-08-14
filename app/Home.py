import streamlit as st

from service.app_config_svc import load_config, edit_config
from service.llm_svc import generate_response
from service.prompt_template_svc import get_all_prompt_template_names

st.set_page_config(layout="wide")

with st.container(border=True):
    cfg = load_config()
    st.markdown(f"#### Selected prompt template: {cfg.get("selected_pt")}")

    with st.popover("Select prompt template"):
        pt_names = get_all_prompt_template_names()
        if selected_pt := st.selectbox("Available prompt templates", pt_names):
            edit_config(cfg_key="selected_pt", cfg_new_value=selected_pt)

st.title("LazyGPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if user_input := st.chat_input("Input a message"):
    st.chat_message("human").markdown(user_input)
    st.session_state.messages.append({"role": "human", "content": user_input})

    assistant_output_stream = generate_response(user_input=user_input)
    st.chat_message("assistant").write_stream(assistant_output_stream)
    st.session_state.messages.append({"role": "assistant", "content": assistant_output_stream})
