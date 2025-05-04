import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Love Calculator ❤️", page_icon="💘", layout="centered")

# Custom styles using Markdown
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            text-align: center;
            font-weight: bold;
            color: #e91e63;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #555;
            margin-bottom: 30px;
        }
        .result {
            font-size: 28px;
            text-align: center;
            color: #4caf50;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title and Subtitle
st.markdown('<div class="title">💖 Love Calculator 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find out how much they are into you!</div>', unsafe_allow_html=True)

# User Inputs
name1 = st.text_input("Enter Your Name:")
name2 = st.text_input("Enter Your Partner's Name:")

# Calculate Button
if st.button("Calculate ❤️"):
    if name1.strip() == "" or name2.strip() == "":
        st.warning("Please enter both names to calculate love percentage.")
    else:
        # Generate a random percentage (more meaningful than just digits)
        love_percent = random.randint(50, 100)
        st.markdown(f'<div class="result">💘 Love between {name1} and {name2} is: {love_percent}% 💘</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit by Maarij Zeeshan")
