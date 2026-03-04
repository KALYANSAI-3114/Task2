import streamlit as st

st.set_page_config(page_title="PlayZone9", layout="wide")

st.markdown("""
<style>

/* Remove Streamlit padding */
.block-container{
padding-top:0rem;
padding-bottom:0rem;
width:100%;
max-width:100%;
}

/* Background */
.stApp{
background: linear-gradient(180deg,#1679A7,#0E5F84);
width:100%;
min-height:100vh;
display:flex;
align-items:center;
justify-content:center;
padding:0;
padding-bottom:150px;
}

/* Center container */
.center-box{
text-align:center;
display:flex;
flex-direction:column;
align-items:center;
justify-content:center;
}

/* Logo */
.logo{
font-size:50px;
font-weight:bold;
color:white;
margin-top:30px;
margin-bottom:20px;
}

/* Login Card */
.login-card{
background:white;
width:380px;
padding:30px;
border-radius:8px;
box-shadow:0px 6px 25px rgba(0,0,0,0.25);
}

/* Login Title */
.login-title{
font-size:20px;
font-weight:bold;
margin-bottom:20px;
}

/* Input fields */
.input{
width:100%;
padding:10px;
margin-bottom:15px;
border:1px solid #ccc;
border-radius:5px;
}

/* Button */
.button{
background:#1679A7;
color:white;
width:100%;
padding:10px;
border:none;
border-radius:5px;
font-size:16px;
cursor:pointer;
}

.button:hover{
background:#0E5F84;
}

/* Links */
.link{
font-size:13px;
margin-top:10px;
}

/* Footer */
.footer{
position:fixed;
bottom:0;
left:0;
right:0;
width:100%;
text-align:center;
color:white;
background:#87CEEB;
padding:20px 0;
margin:0;
}

.support{
font-size:22px;
font-weight:bold;
margin:0;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="center-box">

<div class="logo">PLAYZONE9</div>

<div class="login-card">

<div class="login-title">LOGIN</div>

<input class="input" placeholder="Username">

<input class="input" type="password" placeholder="Password">

<button class="button">Login</button>

<div class="link">
<a href="#">Forgot Password?</a>
</div>

<div class="link">
Don't have User? <a href="#">Register here</a>
</div>

<br>

<small>
This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
</small>

</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
<div class="support">24X7 Support</div>
https://wa.link/playzone9
</div>
""", unsafe_allow_html=True)