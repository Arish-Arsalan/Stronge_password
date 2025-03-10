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
                background: linear-gradient(135deg, #1A1A2E, #16213E, #0F3460);
                font-family: 'Poppins', sans-serif;
                color: #FFFFFF;
            }
            .title {
                text-align: center;
                color: #FF9800;
                font-size: 52px;
                font-weight: bold;
                text-shadow: 4px 4px 20px rgba(255, 152, 0, 0.8);
                margin-bottom: 25px;
            }
            .password-box {
                border: none;
                padding: 30px;
                border-radius: 25px;
                background: rgba(255, 255, 255, 0.1);
                box-shadow: 0px 8px 30px rgba(255, 152, 0, 0.6);
                text-align: center;
                backdrop-filter: blur(20px);
                font-size: 24px;
                font-weight: bold;
            }
            .requirements {
                background: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 6px 20px rgba(255, 152, 0, 0.4);
                backdrop-filter: blur(12px);
                font-size: 18px;
                color: #FFEB3B;
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
                margin-bottom: 25px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='container'><p class='title'>🔐 PasswordStrengthMeter</p>", unsafe_allow_html=True)
    
    password = st.text_input("Enter your password", type="password", help="Must be at least 8 characters, with uppercase, lowercase, a number, and a special character.")
    
    if password:
        with st.spinner("Checking password strength..."):
            time.sleep(1)
        
        strength, color, errors = check_password_strength(password)
        
        st.markdown(f"""
            <div class='password-box' style='color:{color};'>
                PasswordStrength:{strength}
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
