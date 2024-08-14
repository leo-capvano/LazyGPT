import os
import sys

import streamlit as st

sys.path.append(os.path.join("..", "service"))

from service.prompt_template_svc import get_all_prompt_templates
from service.prompt_template_svc import save_prompt_template
from service.prompt_template_svc import delete_prompt_template


def delete_pt(pt_file_name: str):
    delete_prompt_template(pt_file_name)


st.title("Prompt Templates Management")

st.markdown("## Save a new prompt template")
pt_name = st.text_input("Choose a name for the prompt template")
pt_text = st.text_area("Prompt template text", height=300)
if st.button("Save") and pt_name and pt_text:
    save_prompt_template(pt_name, pt_text)

st.divider()
st.markdown("## Prompt Templates Catalog")
prompt_templates: list[dict[str, str]] = get_all_prompt_templates()
for pt in prompt_templates:
    with st.container(border=True):
        st.write(f"### Prompt template name: {pt.get("pt_name").split(".")[0]}")
        st.code(pt.get("pt_text"))
        st.button("Delete", use_container_width=True, on_click=delete_pt, args=(pt.get("pt_name"),))
