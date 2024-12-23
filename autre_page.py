import streamlit as st
from subscription_nl import display_newsletter_subscription
from metadata import get_html_metadata


# Inject HTML metadata
st.markdown(get_html_metadata(), unsafe_allow_html=True)

# Display newsletter bloc
display_newsletter_subscription()