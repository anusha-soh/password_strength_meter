import streamlit as st
import re

def check_password_strength(password: str):
    score = 4
    messages = []

    if len(password) < 8:
        score -= 3
        messages.append("❌ Password should be at least 8 characters long.")
    if not (re.search(r"[a-z]", password) and re.search(r"[A-Z]", password)):
        score -= 2
        messages.append("❌ Include both uppercase and lowercase letters.")
    if not re.search(r"[0-9]", password):
        score -= 1
        messages.append("❌ Add at least one number (0 to 9).")
    if not re.search(r"[!@#$%^&*]", password):
        score -= 1
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    return score, messages

def main():
    st.title("🔐 Password Strength Checker")
    st.header("Test the strength of your password, follow the rules for strong password")
    st.subheader(" Password Strength Criteria")
    st.info("""
            A strong password should: \n
            ✅ Be at least 8 characters long \n
            ✅ Contain uppercase & lowercase letters \n
            ✅ Include at least one digit (0-9) \n
            ✅ Have one special character (!@#$%^&*)\n

            """)

    password = st.text_input("Enter your password", type="password")

    if password:
        score, messages = check_password_strength(password)

        for msg in messages:
            st.warning(msg)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions above.")

if __name__ == "__main__":
    main()
