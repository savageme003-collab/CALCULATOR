import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("🧮 Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Select operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate result
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.success(f"Result: {result}")
