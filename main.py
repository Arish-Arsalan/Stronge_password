import streamlit as st
import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    number_error = not re.search(r"[0-9]", password)
    
    errors = {
        "Minimum 8 characters": length_error,
        "At least one uppercase letter": uppercase_error,
        "At least one lowercase letter": lowercase_error,
        "At least one number": number_error,
    }
    
    passed_checks = sum(not error for error in errors.values())
    
    if passed_checks == 4:
        strength = "Strong"
        color = "green"
    elif passed_checks == 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"
    
    return strength, color, errors

def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter your password", type="password")
    
    if password:
        strength, color, errors = check_password_strength(password)
        
        st.markdown(f"**Password Strength: <span style='color:{color}; font-size:20px;'>{strength}</span>**", unsafe_allow_html=True)
        
        st.write("### Password Requirements:")
        for requirement, failed in errors.items():
            if failed:
                st.markdown(f"❌ {requirement}")
            else:
                st.markdown(f"✅ {requirement}")
    
if __name__ == "__main__":
    main()
