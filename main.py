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
        color = "#00C853"  # Bright Green
    elif passed_checks == 4:
        strength = "Strong"
        color = "#64DD17"  # Light Green
    elif passed_checks == 3:
        strength = "Moderate"
        color = "#FFD600"  # Yellow
    else:
        strength = "Weak"
        color = "#D50000"  # Red
    
    return strength, color, errors

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #1E1E2F, #121212);
                font-family: 'Poppins', sans-serif;
                color: #EAEAEA;
            }
            .title {
                text-align: center;
                color: #FF4081;
                font-size: 42px;
                font-weight: bold;
                text-shadow: 2px 2px 10px rgba(255, 64, 129, 0.8);
            }
            .password-box {
                border: none;
                padding: 20px;
                border-radius: 15px;
                background: rgba(255, 255, 255, 0.1);
                box-shadow: 0px 4px 20px rgba(255, 64, 129, 0.4);
                text-align: center;
                backdrop-filter: blur(10px);
            }
            .requirements {
                background: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(8px);
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
                <p style='color:{color}; font-size:26px; font-weight:bold;'>Password Strength: {strength}</p>
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
