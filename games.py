import streamlit as st
import random

st.title("🎮 Number Guessing Game")

st.write("Welcome to the Number Guessing Game!")
st.write("Guess a number between 1 and 100.")
st.write("You have only 7 attempts.")

# Start game
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# User input
user_input = st.text_input(
    "Enter your number:",
    placeholder="Enter a number from 1 to 100"
)

# Guess button
if st.button("Guess"):

    # Check empty input
    if user_input.strip() == "":
        st.error("❌ Please enter a number.")

    # Check characters
    elif not user_input.strip().isdigit():
        st.error("❌ Invalid input! Please enter numbers only.")

    else:
        number = int(user_input.strip())

        # Check range
        if number < 1 or number > 100:
            st.error("❌ Please enter a number between 1 and 100.")

        # Check game status
        elif st.session_state.game_over:
            st.warning("⚠️ Game over! Please restart the game.")

        else:
            # Increase attempt
            st.session_state.attempts += 1

            # Check guess
            if number > st.session_state.secret_number:
                st.warning("⬆️ Your number is higher!")

            elif number < st.session_state.secret_number:
                st.info("⬇️ Your number is lower!")

            else:
                st.success("🎉 Congratulations! Your guess is correct!")
                st.success(
                    f"You found the number in "
                    f"{st.session_state.attempts} attempts!"
                )
                st.session_state.game_over = True

            # 7 attempts completed
            if (
                st.session_state.attempts >= 7
                and not st.session_state.game_over
            ):
                st.error("❌ Sorry! Your 7 trials are over.")
                st.write(
                    f"The correct number was "
                    f"{st.session_state.secret_number}"
                )
                st.session_state.game_over = True

# Show attempts
st.write(
    f"🎯 Attempts: {st.session_state.attempts}/7"
)

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()
