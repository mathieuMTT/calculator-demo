import streamlit as st
from metadata import get_html_metadata

st.set_page_config(layout="wide")

#st.logo("my_logo.png")

# multi pages V2 https://discuss.streamlit.io/t/launched-multi-page-apps-improved-api-and-new-navigation-ui-features/65679
# icon https://emotion-icons.dev/?s=material%2Fmail

# Define all the available pages, and return the current page
current_page = st.navigation({
    "Overview": [
        st.Page("banking_file_generator.py", title="Dossier Bancaire Generator", icon=":material/money:"),
        st.Page("newsletter.py", title="Newsletter", icon=":material/email:"),
    ],
    "Tools": [
        st.Page("pages/renta_calculator.py", title="Renta Calculator", icon=":material/calculate:"),
        # ...
    ],
})

# Inject HTML metadata
st.markdown(get_html_metadata(), unsafe_allow_html=True)

# current_page is also a Page object you can .run()
current_page.run()