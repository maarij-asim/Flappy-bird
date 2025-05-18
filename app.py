# import streamlit as st
# import random

# # Set page config
# st.set_page_config(page_title="Love Calculator ❤️", page_icon="💘", layout="centered")

# # Custom styles using Markdown
# st.markdown("""
#     <style>
#         .title {
#             font-size: 36px;
#             text-align: center;
#             font-weight: bold;
#             color: #e91e63;
#         }
#         .subtitle {
#             font-size: 20px;
#             text-align: center;
#             color: #555;
#             margin-bottom: 30px;
#         }
#         .result {
#             font-size: 28px;
#             text-align: center;
#             color: #4caf50;
#             font-weight: bold;
#             margin-top: 20px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # App Title and Subtitle
# st.markdown('<div class="title">💖 Love Calculator 💖</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Find out how much they are into you!</div>', unsafe_allow_html=True)

# # User Inputs
# name1 = st.text_input("Enter Your Name:")
# name2 = st.text_input("Enter Your Partner's Name:")

# # Calculate Button
# if st.button("Calculate ❤️"):
#     if name1.strip() == "" or name2.strip() == "":
#         st.warning("Please enter both names to calculate love percentage.")
#     else:
#         # Generate a random percentage (more meaningful than just digits)
#         love_percent = random.randint(50, 100)
#         st.markdown(f'<div class="result">💘 Love between {name1} and {name2} is: {love_percent}% 💘</div>', unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.caption("Made with ❤️ using Streamlit by Maarij Zeeshan")
import streamlit as st

def love_score(name1: str, name2: str) -> int:
    # Simple deterministic calculation based on character codes
    combined = (name1 + name2).lower()
    total = sum(ord(char) for char in combined if char.isalpha())
    return total % 101  # Result between 0 and 100

def main():
    st.set_page_config(page_title="Love Calculator", page_icon="❤️", layout="centered")

    # Set gray background using inline CSS
    st.markdown(
        """
        <style>
        .main {
            background-color: #808080; /* Gray background */
            color: white;
            min-height: 100vh;
            padding: 2rem;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
        }
        .stButton>button {
            background-color: #e75480;
            color: white;
            font-size: 20px;
            padding: 10px 0;
            width: 100%;
            border-radius: 12px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #d0436c;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.title("❤️ Love Calculator")
    st.write("Enter two names and find out the love compatibility score!")

    name1 = st.text_input("Enter first name")
    name2 = st.text_input("Enter second name")

    if st.button("Calculate Love Score"):
        if not name1.strip() or not name2.strip():
            st.warning("Please enter both names to calculate the love score.")
        else:
            score = love_score(name1.strip(), name2.strip())
            st.success(f"The love score between **{name1}** and **{name2}** is: 💖 {score}% 💖")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()


