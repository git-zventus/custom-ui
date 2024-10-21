import streamlit as st

# Set the title of the app
st.title('Zventus Custom UI')

st.markdown("""
Here goes your custom content           
""")

# Embed an iframe (example: Google homepage)
iframe_url = "https://6xwdyl10.chat.qbusiness.us-east-1.on.aws/"
st.components.v1.iframe(iframe_url, width=1000, height=600)