import streamlit as st

st.title("Employee Knowledge Assistant")

question = st.text_input("Ask a question")

if question:

    if "leave" in question.lower():

        st.write(
            "Employees can carry forward up to 10 annual leaves."
        )

        st.write(
            "Source: Leave Policy.pdf"
        )

    elif "travel" in question.lower():

        st.write(
            "Travel reimbursements require manager approval."
        )

        st.write(
            "Source: Travel Policy.pdf"
        )

    elif "it" in question.lower():

        st.write(
            "Raise an IT ticket through the company portal."
        )

        st.write(
            "Source: IT Policy.pdf"
        )

    else:

        st.write(
            "I could not find relevant information."
        )