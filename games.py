import streamlit as st
import random

st.title("🎯 Number Guessing Game")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0

st.write("Guess a number between 1 and 100")

number = st.number_input(
    "Enter your number:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Guess"):
    st.session_state.attempts += 1

    if number > st.session_state.secret:
        st.warning("Your number is higher!")

    elif number < st.session_state.secret:
        st.info("Your number is lower!")

    else:
        st.success(
            f"🎉 Congratulations! You guessed the number "
            f"in {st.session_state.attempts} attempts!"
        )

if st.button("Restart Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()

st.write(f"Attempts: {st.session_state.attempts}/7")