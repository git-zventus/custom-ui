import streamlit as st

# Set the title of the app
st.title('Adding Amazon Q Business to your website')

st.markdown("""
AWS has now made this extremely simple, you only need to add this iframe to your website

```
<iframe src="https://6xwdyl10.chat.qbusiness.us-east-1.on.aws/" width="1000" height="700"></iframe>
```
            
And the authentication will be handled by AWS Identity Center.            
""")



# Embed an iframe (example: Google homepage)
iframe_url = "https://6xwdyl10.chat.qbusiness.us-east-1.on.aws/"
st.components.v1.iframe(iframe_url, width=1000, height=600)