from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

load_dotenv()

#model = GenerativeModel(model_name="gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))

#client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
#model = client.GenerativeModel('gemini-pro')

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')


# Function to get Gemini response
def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text


# Function to read PDF Content
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# Write a prompt for Gemini model
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the 3D (Job Description) and meticulously identify any missing keywords with utmost accuracy.
resume: {text}
description: {id}
I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.
Mention the title for all the three sections.
While generating the response put some space to separate all the three sections.
"""

#streamlit UI
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

# Set background, text, and widget styling
st.markdown("""
    <style>
    /* Background and Main Area */
    body {
        background-color: #f0f4f8;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
    }
    /* Headers and text */
    h1, h2, h3 {
        color: #003366 !important;
    }
    p, li {
        font-size: 18px !important;
        color: #333333 !important;
    }
    /* Button Styling */
    .stButton > button {
        background-color: #005580;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
    }
    /* Text area and uploader */
    .stTextArea textarea, .stFileUploader, .stTextInput input {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

avs.add_vertical_space(4)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<h1 style='font-size: 48px; color: #003366;'>CareerCraft</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #005580;'>Navigate the Job Market with Confidence!</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: justify; font-size: 18px;'>
        Introducing <strong>CareerCraft</strong>, an ATS-Optimized Resume Analyzer – your ultimate solution for optimizing job applications and accelerating career growth.
        Our innovative platform leverages AI to provide resume-job fit analysis, keyword insights, and optimization guidance.
        </p>
    """, unsafe_allow_html=True)

with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_container_width=True)
avs.add_vertical_space(10)

# Offerings:

col1, col2 = st.columns([3, 2])
with col2:
    st.markdown("<h2 style='color:#003366;'>Wide Range of Offerings</h2>", unsafe_allow_html=True)
    offerings = [
        "✅ ATS-Optimized Resume Analysis",
        "✅ Resume Optimization",
        "✅ Skill Enhancement",
        "✅ Career Progression Guidance",
        "✅ Tailored Profile Summaries",
        "✅ Streamlined Application Process",
        "✅ Personalized Recommendations",
        "✅ Efficient Career Path Navigation"
    ]
    for item in offerings:
        st.markdown(f"<p style='font-size: 18px;'>{item}</p>", unsafe_allow_html=True)

with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_container_width=True)


avs.add_vertical_space(10)

#Resume ATS Tracking Application

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<h2 style='color:#003366;'>📄 Resume Matcher</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Paste your job description and upload your resume in PDF format to analyze compatibility.</p>", unsafe_allow_html=True)

    jd = st.text_area("Paste the Job Description", height=200)
    uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type="pdf")

    submit = st.button("🔍 Submit")

    if submit:
        if uploaded_file is not None and jd and jd.strip() != "":
            text = input_pdf_text(uploaded_file)
            formatted_input = input_prompt.format(text=text, id=jd)  # ✅ FIXED FORMATTING ISSUE
            response = get_gemini_response(formatted_input)
            st.markdown("<h3 style='color:#005580;'>📊 Analysis Result</h3>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color:#e6f2ff;padding:15px;border-radius:8px;'>{response}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please upload a PDF file and provide a job description.")

with col2:
    img2 = Image.open("images/icon2.png")
    st.image(img2, use_container_width=True)

avs.add_vertical_space(10)

# FAQ Section

col1,col2 = st.columns([2, 3])
with col2:
    st.markdown("<h2 style='color:#003366;'>❓ Frequently Asked Questions(FAQs)</h2>", unsafe_allow_html=True)
    st.write("Question:🔍 How does CareerCraft analyze resumes and job descriptions?")
    st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.""")
    avs.add_vertical_space(1)
    st.write("Question:✍️ Can CareerCraft suggest improvements for my resume?")
    st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume based on the analysis of job descriptions and industry standards, including suggestions for missing keywords and alignment with desired job roles.""")
    avs.add_vertical_space(1)
    st.write("Question:👥 Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all levels, offering tailored insights and guidance to enhance their resumes and advance their careers.""")

with col1:
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_container_width=True)
