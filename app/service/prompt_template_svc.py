import os
from typing import List

TEMPLATES_FOLDER = "templates"


def save_prompt_template(template_name: str, template_text: str):
    with open(os.path.join("templates", f"{template_name}.txt"), "w") as file:
        file.write(template_text)


def get_all_prompt_templates() -> List[str]:
    templates: List[str] = []
    entries = os.listdir(TEMPLATES_FOLDER)
    template_files = [f for f in entries if os.path.isfile(os.path.join(TEMPLATES_FOLDER, f))]
    for t_file_name in template_files:
        with open(os.path.join(TEMPLATES_FOLDER, t_file_name), "r") as t_file:
            templates.append(t_file.read())
    return templates
