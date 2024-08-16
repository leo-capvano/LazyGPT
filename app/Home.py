import streamlit as st

from service.app_config_svc import load_config, edit_config
from service.llm_svc import generate_response
from service.prompt_template_svc import get_all_prompt_template_names, get_prompt_template_text

st.set_page_config(layout="wide")
cfg = load_config()

with st.container(border=True):
    with st.popover("Select prompt template", use_container_width=True):
        pt_names = get_all_prompt_template_names()
        if selected_pt_name := st.selectbox("Available prompt templates", pt_names):
            edit_config(cfg_key="selected_pt_name", cfg_new_value=selected_pt_name)
            prompt_template_text = get_prompt_template_text(selected_pt_name)
            edit_config(cfg_key="selected_pt_text", cfg_new_value=prompt_template_text)
    st.markdown(f"Selected prompt template -> {cfg.get("selected_pt_name")}")
    st.code(f"{cfg.get("selected_pt_text")}", language="yaml")

st.title("LazyGPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if user_input := st.chat_input(f"Input a message"):
    st.chat_message("human").markdown(user_input)
    st.session_state.messages.append({"role": "human", "content": user_input})

    assistant_output_stream = generate_response(user_input=user_input)
    st.chat_message("assistant").write_stream(assistant_output_stream)
    st.session_state.messages.append({"role": "assistant", "content": assistant_output_stream})
