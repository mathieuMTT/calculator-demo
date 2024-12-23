import streamlit as st

st.set_page_config(layout="wide")

#st.logo("my_logo.png")

# Define all the available pages, and return the current page
current_page = st.navigation({
    "Overview": [
        st.Page("hello.py", title="Hello World", icon=""),
        st.Page("autre_page.py", title="North Star", icon=""),
    ],
    "Tools": [
        st.Page("pages/renta_calculator.py", title="Renta Caclculator", icon=""),
        # ...
    ],
})

# current_page is also a Page object you can .run()
current_page.run()