import streamlit as st
import subprocess
import sys

# Function to run the Pygame game
def run_game():
    # Check if the system uses Python or Python3
    command = [sys.executable, "badminton_game.py"]  # Replace 'badminton_game.py' with your actual file name.
    subprocess.run(command)

# Streamlit UI
st.title("Welcome to the Badminton Game")

st.write("This is a simple 2D badminton game built with Pygame and Streamlit.")
st.write("Click the button below to start the game!")

if st.button("Start Game"):
    st.write("Launching the game...")
    run_game()
