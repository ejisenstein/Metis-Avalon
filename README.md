# Avalonline
An online multiplayer version of the card game Resistance:Avalon,
Perfect for these desperate, coronavirus filled times

---
## Initial Setup
### 1. Create a Virtual Environment in a New Directory
A new virtual environment is necessary for streamlit. You can use
whatever virtual environment you prefer, I typically use venv
- First create a new directory: `mkdir <dir_name>`
- Create a new environment `python3 -m venv <env_name>`
- Activate the new environment `source <env_name>/bin/activate`

You will need to activate the virtual environment every time you quit the terminal or leave the virtual environment.

To tell whether your environment is active, the environment name should be visible in
parentheses in the first line of your terminal command.

Other necessary dependencies

For Flask
`pip install flask`

 for SQL Alchemy
`pip install flask-sqlalchemy`
