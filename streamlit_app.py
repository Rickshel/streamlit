import streamlit as st
import time
import pandas as pd

# Title and Subtitle
st.title("My Autobiography & Portfolio")
st.subheader("Welcome to my personal page!")

# Autobiography Section
st.header("Autobiography")
st.write("""
Hi, I'm Xevery Jan C. Bolo, a passionate web developer with a love for creating intuitive and impactful web applications.
Born and raised in Sanagat Sanfernado Cebu, I discovered my passion for technology at a young age. I am currently a BSIT 4th year student
in Cebu Intitute of Technology University where I honed my skills.
""")

# Adding a Divider
st.markdown("---")

# Portfolio Section
st.header("Portfolio")

# Project 1
st.subheader("1. Project One: Library Management System")
st.write("""
Developed a full-stack Library Management System using Spring Boot and React. The system includes features like 
user authentication, book reservations, and administrative controls. Integrated MySQL for database management and 
used Docker for containerization.
""")

# Project 2
st.subheader("2. Project Two: Visual Novel App with Interactive Learning")
st.write("""
Created a React Native app featuring a visual novel game with interactive learning elements. The app includes 
mini-games for matching Japanese characters and constructing sentences using Japanese grammar.
""")

# Project 3
st.subheader("3. Project Three: Spam Classifier")
st.write("""
Developed a spam classifier using Streamlit and Scikit-learn. The app allows users to input messages and 
predicts whether they are spam or not using a trained machine learning model.
""")

# Adding a Contact Form with your information
st.header("Contact Me")
st.write("Feel free to reach out to me through the information below:")

# Displaying contact information
st.write("**Name:** Xevery Jan C. Bolo")
st.write("**Email:** xeverybolo126@gmail.com")
st.write("**Contact no:** 09369555607")

contact_form = """
<form action="https://formsubmit.co/xeverybolo126@gmail.com" method="POST">
    
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Adding Social Media Links
st.header("Find me on Social Media")
st.write("""
- [FaceBook](https://www.facebook.com/profile.php?id=100008734368411)
- [GitHub](https://github.com/Bolo1232)
""")

# Adding an Expander Section for Skills
st.header("Skills")
with st.expander("Programming Languages"):
    st.write("""
    - Python
    - Java
    - JavaScript
    - TypeScript
    """)
with st.expander("Frameworks & Libraries"):
    st.write("""
    - Spring Boot
    - React
    - Streamlit
    - TensorFlow
    """)
with st.expander("Tools & Platforms"):
    st.write("""
    - Docker
    - MySQL
    - Git
    - AWS
    """)

# Adding a Map centered on Sangat, San Fernando, Cebu
st.header("Location")

# Coordinates for Sangat, San Fernando, Cebu
location_data = pd.DataFrame({
    'lat': [10.194],
    'lon': [123.7208]
})

st.map(location_data)

st.write("Thank you for visiting my page!")
