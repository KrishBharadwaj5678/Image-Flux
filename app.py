import streamlit as st
import requests

# Defining Page Title,Icon
st.set_page_config(
    page_title="Random Image Generator",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1pEGgK2LVKGn4J_nSbdPcP7ciKpujGV1EBw&s",
    menu_items={
        "About":"From the ordinary to the extraordinary, every image is a surprise. Click and discover!"
    }
)

st.write("<h4>Get ready for a visual adventure! Our generator serves up a new surprise with every click, showcasing the diversity and beauty of the world around us. </h4>",unsafe_allow_html=True)

if(st.button(":orange[Generate]",help="Generate Random Image")):
    try:
        data=requests.get("https://picsum.photos/600/500")
        bin_data=data.content
        with open("random.jpeg","wb") as img:
            img.write(bin_data)
            st.image("random.jpeg",use_column_width="always")
    except:
        st.toast("Network Error",icon="🔌")
