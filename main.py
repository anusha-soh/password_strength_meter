import streamlit as st
import re

def main():

    def check_password_strength(password : str):
        
        score = 4


        if len(password) < 8:
            score -= 3
            print("❌ Password should be at least 8 characters long.")
        elif not (re.search(r"[a-z]" , password) and re.search(r"[A-Z]" , password)):
            score -= 2
            print("❌ Include both uppercase and lowercase letters.")
        
        elif not re.search(r"[0-9]" , password):
            score -= 1
            print("❌ Add at least one number (0 to 9).")
        elif not re.search(r"[!@#$%^&*]", password):
            score -= 1
            print("❌ Include at least one special character (!@#$%^&*).")
        

        if score == 4:
            print("✅ Strong Password!")
        elif score == 3:
            print("⚠️ Moderate Password - Consider adding more security features.")
        else:
            print("❌ Weak Password - Improve it using the suggestions above.")

    my_pass = input("Enter your password: ")
    check_password_strength(my_pass)



    


if __name__ == "__main__":
    main()
