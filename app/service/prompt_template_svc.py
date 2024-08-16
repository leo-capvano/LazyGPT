import os
from typing import List, Dict

TEMPLATES_FOLDER = "templates"


def save_prompt_template(template_name: str, template_text: str):
    with open(os.path.join("templates", f"{template_name}.txt"), "w") as file:
        file.write(template_text)


def get_all_prompt_templates() -> list[dict[str, str]]:
    templates: List[Dict[str, str]] = list()
    entries = os.listdir(TEMPLATES_FOLDER)
    template_files = [f for f in entries if os.path.isfile(os.path.join(TEMPLATES_FOLDER, f))]
    for t_file_name in template_files:
        with open(os.path.join(TEMPLATES_FOLDER, t_file_name), "r") as t_file:
            templates.append({"pt_name": t_file_name, "pt_text": t_file.read()})
    return templates


def get_all_prompt_template_names() -> list[str]:
    entries = os.listdir(TEMPLATES_FOLDER)
    return [f.split(".")[0] for f in entries if os.path.isfile(os.path.join(TEMPLATES_FOLDER, f))]


def get_prompt_template_text(pt_name: str) -> str:
    with open(os.path.join(TEMPLATES_FOLDER, f"{pt_name}.txt"), "r") as pt_file:
        return pt_file.read()


def delete_prompt_template(pt_file_name: str):
    os.remove(os.path.join(TEMPLATES_FOLDER, pt_file_name))
    print(f"File '{pt_file_name}' deleted successfully.")
