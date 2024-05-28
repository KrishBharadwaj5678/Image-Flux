import streamlit as st
import requests

st.title(":green[Random Image Generator]")

if(st.button(":orange[Generate]",help="Generate Random Image")):

    data=requests.get("https://picsum.photos/600/500")

    bin_data=data.content

    with open("random.jpeg","wb") as img:
        img.write(bin_data)
        st.image("random.jpeg",use_column_width="always")