import streamlit as st

def contact_us():
    st.title("Contact Us")


    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if name and email and message:
            st.success("Thank you for your message. We will get back to you soon!")


            st.write("Name:", name)
            st.write("Email:", email)
            st.write("Message:", message)
        else:
            st.error("Please fill in all fields!")

if __name__ == "__main__":
    contact_us()
