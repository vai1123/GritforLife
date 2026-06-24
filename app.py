import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="GRIT for LIFE",
    page_icon="🏅",
    layout="wide"
)

st.title("🏅 GRIT for LIFE")
st.subheader("Learn a Sport. Own the Journey.")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Learning Contract",
        "Weekly Learning Log",
        "Skill Tracker",
        "Progress Videos",
        "Final Reflection",
        "Teacher Feedback",
        "Certificate"
    ]
)

sports_skills = {
    "Badminton": [
        "Grip",
        "Footwork",
        "Strokes",
        "Serving"
    ],
    "Basketball": [
        "Dribbling",
        "Passing and Catching",
        "Scoring"
    ],
    "Football": [
        "Dribbling",
        "Passing and Trapping",
        "Scoring"
    ],
    "Floorball": [
        "Dribbling",
        "Passing and Trapping",
        "Scoring"
    ],
    "Table Tennis": [
        "Forehand Drive",
        "Forehand Push",
        "Backhand Drive",
        "Backhand Push"
    ],
    "Volleyball": [
        "Digging",
        "Serving",
        "Return the Serve",
        "Setting"
    ],
    "Rope Skipping": [
        "Basic Bounce",
        "Boxer Step",
        "High Knee",
        "Side Straddle",
        "Forward Straddle"
    ]
}

if menu == "Home":

    st.image(
        "https://images.unsplash.com/photo-1517649763962-0c623066013b",
        use_container_width=True
    )

    st.markdown("""
    ### Welcome to GRIT for LIFE

    Complete the following sections:

    ✅ Learning Contract

    ✅ Weekly Learning Logs

    ✅ Skill Tracker

    ✅ Progress Videos

    ✅ Final Reflection

    ✅ Teacher Feedback

    Complete all sections to earn your certificate.
    """)

# --------------------------------------------------------

elif menu == "Learning Contract":

    st.header("Student Learning Contract")

    student = st.text_input("Student Name")
    student_class = st.text_input("Class")

    sport = st.selectbox(
        "Selected Sport",
        list(sports_skills.keys())
    )

    motivation = st.text_area(
        "Why did you choose this sport?"
    )

    goals = st.text_area(
        "My Weekly Goals (Weeks 1–10)"
    )

    practice = st.text_area(
        "Where and how will I practise each week?"
    )

    tracking = st.multiselect(
        "How will you track your progress?",
        ["Written Journal", "Video Journal"]
    )

    st.markdown("### Student Agreement")

    agreement = st.checkbox(
        "I agree to practise regularly and complete my learning logs."
    )

    signature = st.text_input("Student Signature")

    st.markdown("### Parent Acknowledgement")

    parent_name = st.text_input("Parent Name")
    parent_signature = st.text_input("Parent Signature")

    if st.button("Submit Contract"):
        st.success("Learning contract submitted successfully.")

# --------------------------------------------------------

elif menu == "Weekly Learning Log":

    st.header("Weekly Learning Log")

    week = st.selectbox(
        "Week",
        range(1, 11)
    )

    progress = week / 10
    st.progress(progress)

    for session in [1, 2]:

        st.subheader(f"Practice Session {session}")

        session_date = st.date_input(
            f"Date {session}",
            key=f"date{session}"
        )

        duration = st.number_input(
            f"Duration (minutes) {session}",
            0,
            300,
            key=f"duration{session}"
        )

        activity = st.text_input(
            f"Activity Practised {session}",
            key=f"activity{session}"
        )

        good = st.text_area(
            f"What went well? {session}",
            key=f"good{session}"
        )

        improve = st.text_area(
            f"What needs work? {session}",
            key=f"improve{session}"
        )

        challenge = st.text_area(
            f"Challenge faced {session}",
            key=f"challenge{session}"
        )

        next_session = st.text_area(
            f"Plan for next session {session}",
            key=f"next{session}"
        )

    st.subheader("Optional Additional Session")

    notes = st.text_area(
        "Additional notes"
    )

    if st.button("Save Weekly Log"):
        st.success(f"Week {week} saved.")

# --------------------------------------------------------

elif menu == "Skill Tracker":

    st.header("Skill Tracker")

    selected_sport = st.selectbox(
        "Choose your sport",
        list(sports_skills.keys())
    )

    st.write("Tick the skills you have practised.")

    completed = 0

    for skill in sports_skills[selected_sport]:

        if st.checkbox(skill):
            completed += 1

    percentage = completed / len(sports_skills[selected_sport])

    st.progress(percentage)

    st.write(
        f"Skills Completed: {completed}/{len(sports_skills[selected_sport])}"
    )

# --------------------------------------------------------

elif menu == "Progress Videos":

    st.header("Progress Videos")

    video_week = st.selectbox(
        "Video Submission Week",
        [1, 5, 10]
    )

    uploaded_video = st.file_uploader(
        "Upload your video",
        type=["mp4", "mov", "avi"]
    )

    if uploaded_video:
        st.video(uploaded_video)

    if st.button("Submit Video"):
        st.success(
            f"Week {video_week} video submitted."
        )

# --------------------------------------------------------

elif menu == "Final Reflection":

    st.header("Final Reflection")

    st.write(
        "Please write 150–250 words."
    )

    learning = st.text_area(
        "1. What I learned during this programme"
    )

    challenges = st.text_area(
        "2. Challenges I faced and how I overcame them"
    )

    improvement = st.text_area(
        "3. How my skills improved"
    )

    future = st.text_area(
        "4. How I will continue this sport"
    )

    if st.button("Submit Reflection"):
        st.success("Reflection submitted.")

# --------------------------------------------------------

elif menu == "Teacher Feedback":

    st.header("Teacher Feedback")

    week1 = st.checkbox("Week 1 Video Completed")
    week5 = st.checkbox("Week 5 Video Completed")
    week10 = st.checkbox("Week 10 Video Completed")

    feedback = st.text_area(
        "Teacher's Encouragement / Feedback"
    )

    completed = st.checkbox(
        "Student has completed the programme"
    )

    if st.button("Save Feedback"):
        st.success("Feedback saved.")

# --------------------------------------------------------

elif menu == "Certificate":

    st.header("Certificate of Completion")

    name = st.text_input(
        "Student Name"
    )

    sport = st.text_input(
        "Sport"
    )

    st.markdown("---")

    st.markdown("# 🏅")

    st.markdown("## GRIT for LIFE")

    st.markdown("### Certificate of Completion")

    st.markdown(
        "'Show your grit, claim your kit.'"
    )

    st.markdown(
        f"### This certificate is presented to"
    )

    st.markdown(
        f"# {name}"
    )

    st.markdown(
        "for successfully completing the programme."
    )

    st.markdown(
        f"Sport: **{sport}**"
    )

    st.markdown("")

    st.markdown(
        "**MR ERNEST VAITHILINGAM**"
    )

    st.markdown(
        "HOD PE"
    )
