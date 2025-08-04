import streamlit as st

st.title("Route Ride Questionnaire")

# Section 1: Basic Info
st.header("1. Account Information")
name = st.text_input("What is the Account Name?")
name = st.text_input("What is the machine number?")

# Section 2: Experience
st.header("2. Service Experience")
satisfaction = st.slider("How satisfied are you with our service?", 1, 5)
recommend = st.radio("Would you recommend us to others?", ["Yes", "No", "Maybe"])

# Section 3: Open Feedback
st.header("3. Additional Feedback")
feedback = st.text_area("Please provide any additional comments or suggestions.")

# Submit button
if st.button("Submit"):
    st.success("Thank you for your feedback!")
    st.write("### Summary of your responses:")
    st.write(f"**Name:** {name}")
    st.write(f"**Name:** {name}")
    st.write(f"**Satisfaction:** {satisfaction}/5")
    st.write(f"**Recommendation:** {recommend}")
    st.write(f"**Additional Feedback:** {feedback}")
