from pyscript import document

def generate_message(event):
# VALUES FROM INDEX.HTML
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

# GENERATE TEXT
    message = f"""
Name : {name}
Age : {age}
School : {school}\n
{name}\'s {age} years old and is currently\nstudying at {school}. This data was collected using\nit\'s input fields and shown as a Python\nmultiline string using PyScript.
"""

# DISPLAY NEW TEXT
    output = document.getElementById("final")
    output.innerHTML = ""
    output.innerHTML = f"<pre>{message}</pre>"
