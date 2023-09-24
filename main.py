import streamlit as st
import random
from collections import deque

# Define the predefined options with associated image URLs
predefined_options = {
    "Baby_Powder": "baby-powder.png",
    "Chocolate_Bar": "chocolate-bar.png",
    "Comb": "comb.png",
    "Cookies": "cookies.png",
    "Cricket_Bat": "cricket-bat.png",
    "Ball": "cricket.png",
    "Gloves": "gloves.png",
    "Pen": "pen.png",
    "Ruler": "ruler.png",
    "Spray": "spray.png",
}

# Shuffle the predefined options to ensure randomness
random.shuffle(list(predefined_options.keys()))

# Create a deque to store the history of the last 15 options
option_history = deque(maxlen=15)

# Create a set to store the options used in the next 15 spins
next_15_options = set(predefined_options.keys())  # Start with all options

# Create a list to store the complete history of spins with user names
complete_spin_history = []

# Create a global variable to store the complete spin history across runs
if "all_spin_history" not in st.session_state:
    st.session_state.all_spin_history = []

# Streamlit UI
st.title("KGISL Institute Of Technology\nDepartment of Artificial Intelligence and Data Science\nPresents\nProduct Marketing")

# Get the user's name as input
user_name = st.text_input("Enter your name:")

if user_name:
    st.write(f"Welcome, {user_name}!")

    def get_unique_option():
        # Ensure the selected option is unique in the last 15 spins
        while True:
            selected_option = random.choice(list(predefined_options.keys()))
            if selected_option not in option_history:
                break
        return selected_option

    if st.button("Spin"):
        selected_option = get_unique_option()
        option_history.append(selected_option)
        next_15_options.remove(selected_option)

        # Add the selected option and user's name to the complete spin history
        complete_spin_history.append({"Name": user_name, "Option": selected_option})

        # Display the selected option's image with a smaller width
        st.image(predefined_options[selected_option], caption=selected_option, use_column_width=True, width=100)

        # Append the complete spin history to the global history
        st.session_state.all_spin_history.append(complete_spin_history)

# Display the complete history of spins with user names and options in a table
if st.session_state.all_spin_history:
    st.write("## Complete Spin History")
    all_history = [entry for history in st.session_state.all_spin_history for entry in history]
    st.table(all_history)
