# LazyGPT
This project is a tool that integrates a generative AI (GenAI) model for conversational interactions.
The tool provides an interface where users can chat with the AI model and save, manage, and reuse prompt templates.
The goal is to streamline the process of generating consistent, high-quality outputs by enabling users to maintain a
library of reusable prompts.

## Features
- Interactive Chat Interface: Engage in conversations with the GenAI model through a user-friendly chat interface.
- Prompt Templates: Create, save, and reuse prompt templates to standardize interactions with the AI model.
- Template Management: Edit, delete, and organize prompt templates for easy access.

### Next Steps
- Template Variables: Define variables within templates to make them adaptable to different contexts.
- Export & Import: Export templates for sharing or backup, and import templates from external sources.
- Categorizing and organizing prompts into folders
- Directly edit the chat input (currently not supported by Streamlit)

# Installation
Prerequisites
- Python 3.12
- Pip (Python package manager)

1. Clone the Repository
2. Install Dependencies (_pip install -r requirements.txt_)

# Usage
Starting the Application
> streamlit run app/Home.py

# Managing Prompt Templates
This section explains how to manage and use the prompt template catalog feature
## Create a new prompt template
Go into the **Prompt Templates Management** page, then use the form 
to save the title and the content of your prompt template:
![img.png](imgs/save_pt.png)

## Show all the saved prompt templates
Scrolling down the same page will show all the saved prompt templates:
![saved_pt.png](imgs/saved_pt.png)

# Using the Chat Interface
This section will show how to use the chat interface with saved prompt templates.
1. Select one of the saved the prompt templates from the top dropdown:
![dropdown.png](imgs/dropdown.png)
2. Copy the prompt template using the copy button 
![img.png](imgs/chat.png)
3. Paste it into the chat to use it
![img.png](imgs/translate.png)

# License
This project is licensed under the GNU GENERAL PUBLIC license. See the LICENSE file for more information.

This README provides an outline for installing, using, and contributing to the LazyGPT Tool with prompt templates. 
Customize the information based on your specific project details.