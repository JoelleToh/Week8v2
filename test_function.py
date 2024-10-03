# Set up and run this Streamlit App
import streamlit as st
import pandas as pd

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My testing App"
)

#2.2.1 Show a temporary message with a button
animal_shelter = ['cat', 'dog', 'rabbit', 'bird'] 

animal = st.text_input('Type an animal') 

if st.button('Check availability'): 
	have_it = animal.lower() in animal_shelter 
	'We have that animal!' if have_it else 'We don\'t have that animal.'
	
# 2.2.2 Stateful button
# If you want a clicked button to continue to be True, 
# create a value in st.session_state and use the button to set that value to True in a callback.

if 'clicked' not in st.session_state: 
	st.session_state.clicked = False 
	
def click_button(): 
	st.session_state.clicked = True 
	
st.button('Click me', on_click=click_button) 
# A callback is a function passed as an argument to another function

if st.session_state.clicked: 
	# The message and nested widget will remain on the page 
	st.write('Button clicked!') 
	st.slider('Select a value')

if 'name' not in st.session_state: 
	st.session_state['name'] = 'John Doe' 
	
def change_name(name): 
	st.session_state['name'] = name 
	
st.header(st.session_state['name']) 

st.button('Jane', on_click=change_name, args=['Jane Doe']) 
st.button('John', on_click=change_name, args=['John Doe']) 

st.header(st.session_state['name'])

# Buttons to modify or reset other widgets

# Option 1
# Use a key for the button and put the logic before the widget
# Use the get method since the keys won't be in session_state 
# on the first script run 
# if st.session_state.get('clear'): 
# 	st.session_state['name'] = '' 
	
# if st.session_state.get('streamlit'): 
# 	st.session_state['name'] = 'Streamlit' 
	
# st.text_input('Name', key='name') 

# st.button('Clear name', key='clear') 
# st.button('Streamlit!', key='streamlit')

# Option 2: Use a callback
st.text_input('Name', key='name') 

def set_name(name): 
	st.session_state.name = name 
	
st.button('Clear name', on_click=set_name, args=['']) 
st.button('Streamlit!', on_click=set_name, args=['Streamlit'])
