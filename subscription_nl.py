import streamlit.components.v1 as components
import streamlit as st


def display_newsletter_subscription():
    """
    Display the newsletter subscription section.
    """
    st.subheader("Restez dans la boucle 📩")
    st.write(
        "Inscrivez-vous à ma newsletter pour suivre l'évolution de l'application "
        "et découvrir en avant-première les nouvelles fonctionnalités."
    )

    # Integrate a centered iframe for the newsletter subscription
    components.html(
        """
        <div style="text-align: center;">
            <iframe src="https://mathieumtt.substack.com/embed"
                    width="480"
                    height="320"
                    style="border:1px solid #EEE; background:white;"
                    frameborder="0"
                    scrolling="no">
            </iframe>
        </div>
        """,
        height=320,  # Specifies the height of the iframe container
    )

    st.write("")
    st.write("")
    st.write("")
