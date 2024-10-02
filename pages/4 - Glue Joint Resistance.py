import streamlit as st



# Set page configuration
st.set_page_config(page_title="Glue Joint Resistance", layout="wide")



st.markdown(
    """
    <style>
    .subsubheader {
        font-size: 1.2em; /* Adjust the font size as needed *
        font-weight: bold;
        margin-top: 0em; /* Adjust the margin as needed */
        color: rgb(49, 51, 63); /* Change the color as needed */
    }
    .text {
        font-size: 1.0em; /* Adjust the font size as needed */
        margin-top: 0em; /* Adjust the margin as needed */
        color: "black"; /* Change the color as needed */
    }p
    </style>
    """,
    unsafe_allow_html=True
)



# Render HTML to include Font Awesome icons
st.image("Sunman_logo.png", width = 300)
st.subheader("SunMan Solar Panels - Ultra-light, Glass-free Technology")
st.write('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
         The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. \
         Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently.')
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns([3,60])
with col1:
    st.image("icon4.png", width=40)
with col2:
    st.header("Glue Joint Resistance")
st.markdown('<h3 class="subsubheader">The glue joint resistance needs to be obtained and verified from a glue manufacturer according to European standards.</h3>', unsafe_allow_html=True)
st.write("")
st.write("")


st.markdown('<h3 class="text"> The design glue joint resistance is either</h3>', unsafe_allow_html=True)
st.markdown("   - not approved by ETAG and needs reduction according to Eurocode based partial safety factors (non-approved products typical rely on testing and data from the manufacturer), or")
st.markdown("   - approved by ETAG, with independent testing and safety factors included in the “design strength” eliminating the need for reduction factors.)")
