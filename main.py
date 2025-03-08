import streamlit as st
import re
st.title("Password Strength Meter")
password = st.text_input("Enter Your Password to Check it's Strength", type="password")
point : int = 0
strength = None
def password_strength():
     global point, strength 

     if len(password) >= 8:
          point += 2
     else:
          st.error("Use Atleast 8 Characters.")

     if re.search(r"\d", password):
          point += 2
     else:
          st.error("Password should have at least one digit.")

     if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
          point += 2
     else:
          st.error("Use Special Characters.")

     if re.search(r"[A-Z]", password):
          point += 2
     else:
          st.error("Use atleast one capital letter.")

     if len(password) >= 10 and re.search(r"\d", password) and re.search(r"[A-Z]", password):
          point += 2

     if point >= 8:
          strength = "Strong"
     elif point >=5 and point <8:
          strength = "Moderate"
     else:
          strength = "Weak"
     
if st.button("Check Strength"):
     password_strength()
     st.write(f"Password: `{password}`")
     st.write(f"Password Rating: {point}/10")
     st.write(f"Password Strength: `{strength}`")


     
     st.write("-------------------------")
     st.write("Made by [Hassaan Arain](https://github.com/muhammadhassaanarain)")