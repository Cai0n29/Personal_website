import streamlit as st
st.title("Jickle Ong")

st.write("""
<p style="font-family:Monospace; color:black; font-size: 14.5px;">Greetings! I'm Jickle. But can also call me Cai. 
<br>
I'm a homeschooler and highschool student from the Philippines.
<br>
I'm a tech ethusiast and I enjoy creating ideas and make it out of coding.
<br>
Fun fact about me, I enjoy trying new activities.
<br>
But most of all I do it everything for the Glory of the Lord!</p>
""", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns([0.12, 0.12, 0.5, 0.14])

with col1:
    
    st.write("""
    <p style ="font-family:Monospace; color:black; font-size: 18px; ">
    <a href='https://github.com/Cai0n29' id='personal-website-link'>Github</a></p>
    """, unsafe_allow_html=True)
with col2:
     st.write("""
     <p style ="font-family:Monospace; color:black; font-size: 18px;">
     <a href ='mailto:capellakratos@gmail.com' id ='email'>Email</a></p>
    """, unsafe_allow_html=True)

with col3:
    st.write("""
             <p style ="font-family:Monospace; color:black; font-size: 18px;">
     <a href ='https://www.linkedin.com/in/jickle-ong-ba9276304/' id ='email'>Linkedin</a></p>
    """, unsafe_allow_html=True)
    
with col4:
    page1 = st.button("Projects")
    
if page1:
    st.write("""
             <p style ="font-family:Courier; color:black; font-size: 18px;"><b>UNDER MAINTENANCE🚧</p>""",unsafe_allow_html=True)
    st.write(" ")
    back = st.button("Back")

else:

    st.title("")

    st.write("""
    <p style="font-family:Lucida Console, Courier New, monospace; color:black; font-size: 23px;">MY HIGHLIGHTS SO FAR
    </p>
    """, unsafe_allow_html=True)


    col1,col2,col3= st.columns([0.2,5,1,])

    with col1: 
        st.write(" ")
    with col2:
        st.image('Accenture.jpg', caption='Accenture: Girls Breaking Barriers Hackathon - Team Leader of Team Homeschool Global, Finalist and Best Protype award. With Luna, Jameela, and Jana', width = 550)
    

    st.write("")

    col1,col2,col3= st.columns([0.2,5,1,])

    with col1: 
        st.write(" ")
    with col2:
        st.image('Ateneo.jpg', caption='Summer Camp in Ateneo De Manila University', width = 550)
    
    
    st.write(" ")

    col1,col2,col3= st.columns([0.2,5,1,])

    with col1: 
        st.write("")
    with col2:
        st.image('devcon.jpg', caption='She is Devcon 2024 Bootcamp - Selected Participant', width = 550)
    
    st.write(" ")


    
    
    



