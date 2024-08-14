import os
import sys

import streamlit as st

sys.path.append(os.path.join("..", "service"))

from service.prompt_template_svc import get_all_prompt_templates
from service.prompt_template_svc import save_prompt_template

st.title("Prompt Templates Management")

st.markdown("## Save a new prompt template")
pt_name = st.text_input("Choose a name for the prompt template")
pt_text = st.text_area("Prompt template text", height=300)
if st.button("Save") and pt_name and pt_text:
    save_prompt_template(pt_name, pt_text)

st.divider()
st.markdown("## Prompt Templates Catalog")
prompt_templates = get_all_prompt_templates()
for pt in prompt_templates:
    st.write(pt)
