import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    function.write_todos(todos)
    




st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
  cheackbox =  st.checkbox(todo, key=todo)
  if cheackbox:
      todos.pop(index)
      function.write_todos(todos)
      del st.session_state[todo]
      st.experimental_rerun()
       
st.text_input(label="", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')
        

        