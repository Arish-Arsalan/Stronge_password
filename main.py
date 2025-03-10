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
        color = "#00C853"
    elif passed_checks == 4:
        strength = "Strong"
        color = "#64DD17"
    elif passed_checks == 3:
        strength = "Moderate"
        color = "#FFD600"
    else:
        strength = "Weak"
        color = "#D50000"
    
    return strength, color, errors

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #1E1E2F, #252542);
                font-family: 'Poppins', sans-serif;
                color: #EAEAEA;
            }
            .title {
                text-align: center;
                color: #00E5FF;
                font-size: 48px;
                font-weight: bold;
                text-shadow: 3px 3px 15px rgba(0, 229, 255, 0.9);
                margin-bottom: 20px;
            }
            .password-box {
                border: none;
                padding: 25px;
                border-radius: 20px;
                background: rgba(255, 255, 255, 0.1);
                box-shadow: 0px 6px 25px rgba(0, 229, 255, 0.5);
                text-align: center;
                backdrop-filter: blur(15px);
            }
            .requirements {
                background: rgba(255, 255, 255, 0.1);
                padding: 18px;
                border-radius: 12px;
                box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.3);
                backdrop-filter: blur(10px);
                font-size: 16px;
            }
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 80vh;
            }
            .input-box {
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='container'><p class='title'>🔐 Password Strength Meter</p>", unsafe_allow_html=True)
    
    password = st.text_input("Enter your password", type="password", help="Must be at least 8 characters, with uppercase, lowercase, a number, and a special character.")
    
    if password:
        with st.spinner("Checking password strength..."):
            time.sleep(1)
        
        strength, color, errors = check_password_strength(password)
        
        st.markdown(f"""
            <div class='password-box'>
                <p style='color:{color}; font-size:30px; font-weight:bold;'>Password Strength: {strength}</p>
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
    
    st.markdown("</div>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
