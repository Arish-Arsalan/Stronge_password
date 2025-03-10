
import streamlit as st
import re
import time

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    number_error = not re.search(r"[0-9]", password)
    special_char_error = not re.search(r"[@$!%*?&]", password)
    
    errors = {
        "Minimum 8 characters": length_error,
        "At least one uppercase letter": uppercase_error,
        "At least one lowercase letter": lowercase_error,
        "At least one number": number_error,
        "At least one special character (@, $, !, %, *, ?, &)": special_char_error,
    }
    
    passed_checks = sum(not error for error in errors.values())
    
    if passed_checks == 5:
        strength = "Very Strong"
        color = "#008000"  # Dark Green
    elif passed_checks == 4:
        strength = "Strong"
        color = "#32CD32"  # Light Green
    elif passed_checks == 3:
        strength = "Moderate"
        color = "#FFA500"  # Orange
    else:
        strength = "Weak"
        color = "#FF0000"  # Red
    
    return strength, color, errors

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    st.markdown("""
        <style>
            body {
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            .title {
                text-align: center;
                color: #2E86C1;
                font-size: 36px;
                font-weight: bold;
            }
            .password-box {
                border: 2px solid #2E86C1;
                padding: 15px;
                border-radius: 12px;
                background-color: white;
                box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
                text-align: center;
            }
            .requirements {
                background-color: #fff;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='title'>🔐 Password Strength Meter</p>", unsafe_allow_html=True)
    
    password = st.text_input("Enter your password", type="password")
    
    if password:
        with st.spinner("Checking password strength..."):
            time.sleep(1)  # Simulating processing delay
        
        strength, color, errors = check_password_strength(password)
        
        st.markdown(f"""
            <div class='password-box'>
                <p style='color:{color}; font-size:24px; font-weight:bold;'>Password Strength: {strength}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("### Password Requirements:")
        
        st.markdown("<div class='requirements'>", unsafe_allow_html=True)
        for requirement, failed in errors.items():
            if failed:
                st.markdown(f"❌ {requirement}")
            else:
                st.markdown(f"✅ {requirement}")
        st.markdown("</div>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
