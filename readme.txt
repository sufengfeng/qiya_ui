pyinstaller -F -i logo.ico qiya_GUI.py
pip freeze > requirements.txt
pip install -r requirements.txt