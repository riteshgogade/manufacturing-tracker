import streamlit as st

# 1. Define your user roles and passwords (Use hashes in production!)
# For now, we use a simple dict for the prototype.
USER_DATA = {
    "admin": {"name": "CMD", "role": "CMD"},
    "pmg_user": {"name": "PMG", "role": "PMG"},
    "workshop_user": {"name": "Workshop", "role": "Workshop"}
}

def login_page():
    st.title("Manufacturing Tracker Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Dummy authentication logic
        if username in USER_DATA:
            st.session_state['logged_in'] = True
            st.session_state['role'] = USER_DATA[username]['role']
            st.session_state['username'] = username
            st.rerun()
        else:
            st.error("Invalid username or password")

def main():
    # 2. Check if logged in
    if 'logged_in' not in st.session_state:
        login_page()
    else:
        # 3. Main Application Logic based on role
        st.sidebar.success(f"Logged in as: {st.session_state['role']}")
        
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.rerun()
            
        render_dashboard(st.session_state['role'])

def render_dashboard(role):
    st.title(f"{role} Dashboard")
    if role == "CMD":
        st.write("Displaying Global Analytics and Bottlenecks...")
    elif role == "PMG":
        st.write("Displaying Schedule and Variance Reports...")
    else:
        st.write("Displaying Departmental Tasks...")

if __name__ == "__main__":
    main()
