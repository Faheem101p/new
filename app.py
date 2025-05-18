import streamlit as st
from model import predict_career
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="Career Counselor", layout="centered")
st.title("🎓 Intelligent Career Counselor System")

st.write("Answer the questions below to get a career recommendation:")

skills = st.selectbox("Select your primary skill:", ['Python SQL', 'Drawing Design', 'Excel Stats', 'Writing Reading', 'Java C++', 'Photoshop Illustrator', 'PowerBI Excel', 'Creative Writing', 'Coding Debugging', 'Sketching Painting', 'Accounting Excel', 'Story Writing'])
interests = st.selectbox("Select your interest area:", ['Tech', 'Art', 'Business', 'Literature'])
math_score = st.slider("Math Score", 0, 100, 70)
english_score = st.slider("English Score", 0, 100, 70)
logical_score = st.slider("Logical Thinking Score", 0, 100, 70)
creativity = st.slider("Creativity Level", 0, 100, 70)
communication = st.slider("Communication Skills", 0, 100, 70)
programming = st.slider("Programming Skill Level", 0, 100, 70)
work_style = st.selectbox("Preferred Work Style", ['Team', 'Alone'])

if st.button("Get Career Recommendation"):
    career = predict_career(skills, interests, math_score, english_score, logical_score, creativity, communication, programming, work_style)
    st.success(f"🎯 Recommended Career: **{career}**")

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Career Counseling Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Skillset: {skills}", ln=True)
    pdf.cell(200, 10, txt=f"Interest Area: {interests}", ln=True)
    pdf.cell(200, 10, txt=f"Math Score: {math_score}", ln=True)
    pdf.cell(200, 10, txt=f"English Score: {english_score}", ln=True)
    pdf.cell(200, 10, txt=f"Logical Score: {logical_score}", ln=True)
    pdf.cell(200, 10, txt=f"Creativity: {creativity}", ln=True)
    pdf.cell(200, 10, txt=f"Communication: {communication}", ln=True)
    pdf.cell(200, 10, txt=f"Programming: {programming}", ln=True)
    pdf.cell(200, 10, txt=f"Work Style: {work_style}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f" Recommended Career: {career}", ln=True)

    # Save and create download button
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        with open(tmp_file.name, "rb") as f:
            st.download_button(
                label="📄 Download PDF Report",
                data=f,
                file_name="Career_Report.pdf",
                mime="application/pdf"
            )

