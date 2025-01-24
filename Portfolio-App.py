import streamlit as st

# Set the title of the web app
st.set_page_config(page_title="Shreyas Shekhar's Portfolio", page_icon="🌟")

# Custom CSS for styling and moving the image downwards
st.markdown("""
    <style>
        .main {
            background-color: #f7f7f7;
        }
        .profile-pic-container {
            margin-top: 70px; /* Moves the image 70px downwards */
            display: flex;
            justify-content: center;
        }
        .profile-pic-container {
            margin-top: 70px; /* Moves the image 70px downwards */
            display: flex;
            justify-content: center;
        }

        }
        .section-header {
            font-size: 2.5em;
            color: #4B8BBE;
            margin-top: 20px;
            border-bottom: 2px solid #4B8BBE;
        }
        .subheader {
            font-size: 1.5em;
            color: white;
        }
        .card {
            padding: 15px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .link {
            color: #1E90FF;
        }
        ol {
            margin-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section with Profile Picture
col1, col2 = st.columns([2, 4])  # Adjust column width ratio for better alignment
with col1:
    st.markdown(
        '<div class="profile-pic-container">', unsafe_allow_html=True
    )
    st.image("/Users/sameekshashekhar/Desktop/Personal-Portfolio/shreyas_9882.jpg", width=200)  # Provide the correct path to the image
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.title("Shreyas Shekhar")
    st.write("""
        I am Shreyas Shekhar, a final-year B.Tech student pursuing Electronics and Communication Engineering (ECE) at PES University. 
        I have a strong foundation in software development, data analysis, and AI/ML technologies. Proficient in Python, Java, and JavaScript, 
        I also excel in frameworks like React.js and Django, with hands-on expertise in TensorFlow, OpenCV, and Scikit-learn for machine learning applications. 
        My certifications in Python for Data Science and AI and Google Data Analytics reflect my commitment to continuous learning. 
        My interests lie in Data Science, Data Analytics, and Software Development roles.
    """)

# Contact Information Section
with st.expander("Contact Information"):
    st.markdown("<div class='section-header'>Contact Information</div>", unsafe_allow_html=True)
    st.markdown("""
    1. 📞 +91-9148862724  
    2. 📧 [shreyasshekhar98@gmail.com](mailto:shreyasshekhar98@gmail.com)  
    3. [LinkedIn Profile](https://linkedin.com/in/shreyas-shekhar-6b050930a)  
    4. [GitHub Profile](https://github.com/Shreyas9882)  
    """)

# Education Section
with st.expander("Education"):
    st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
    st.markdown("""
    1. **PES University**  
       - Bachelor of Technology in Electronics and Communication Engineering  
       - October 2021 to July 2025 | CGPA: 6.35  
       - Relevant Coursework: Computer Networks, Computer Architecture, RISC-V Architecture, Digital Image Processing, Database Management, Data Structures & Algorithms  

    2. **Deeksha PU College**  
       - 12th Grade Science (PCMC)  
       - May 2019 to June 2021 | Percentage: 85%  

    3. **Carmel School**  
       - 10th Grade ISCE  
       - June 2018 to March 2019 | Percentage: 85%  
    """)

# Skills Section
with st.expander("Skills"):
    st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
    skills = {
        "1. Languages": ["Python", "Java", "HTML", "CSS", "JavaScript"],
        "2. Software Development": ["React", "TailwindCSS", "Django", "Streamlit", "REST API", "OOPs", "DSA"],
        "3. Data Analysis": ["NumPy", "Pandas", "Seaborn", "Matplotlib", "Excel", "PowerBI"],
        "4. AI/ML": ["TensorFlow", "Scikit-learn", "OpenCV"],
        "5. Tools": ["VS Code", "Jupyter Notebook", "PyCharm", "Github", "MATLAB", "Arduino"],
        "6. Databases": ["MySQL", "MongoDB"],
        "7. Soft Skills": ["Analytical Thinking", "Problem Solving", "Communication Skills", "Learning Agility",
                           "Business Acumen"]
    }

    for category, items in skills.items():
        st.markdown(f"<div class='subheader'>{category}</div>", unsafe_allow_html=True)
        st.write(", ".join(items))

# Projects Section
with st.expander("Projects"):
    st.markdown("<div class='section-header'>Projects</div>", unsafe_allow_html=True)

    projects = [
        {
            "description": """
                ### 1. Smart Neck Band — IoT, Machine Learning  
                Developed an IoT-enabled device that monitors cervical spine posture using machine learning algorithms. It provides real-time posture correction alerts to prevent spondylitis. The system collects data from sensors, analyzes it with ML models, and notifies the user of improper posture, promoting better neck health and posture awarenes.  
                **Technologies**: IoT, Machine Learning, Python  
                [GitHub: Smart Neck Band](https://github.com/Shreyas9882/Smart-Neck-Band)
            """
        },
        {
            "description": """
                ### 2. Customer Churn Prediction System  
                Developed binary classification models for customer churn prediction using Keras with hyperparameter tuning. Achieved 75.62% validation accuracy accross multiple models through data pre-processing and feature engineering. Visualized results and provided insights to improve customer retention strategies.  
                **Technologies**: Python, Keras, TensorFlow, Scikit-learn  
                [GitHub: Customer Churn Prediction](https://github.com/Shreyas9882/Customer_Churn_Prediction)
            """
        },
        {
            "description": """
                ### 3. Age and Gender Prediction  
                This Age-and-Gender-Prediction system uses pre-trained deep learning models for face detection, age, and gender prediction. It processes images or live video feeds, detects faces, and predicts age and gender. Results are displayed with bounding boxes and labels, supporting both photo upload and real-time webcam modes.  
                **Technologies**: OpenCV, Python, Deep Learning  
                [GitHub: Age and Gender Prediction](https://github.com/Shreyas9882/Age-and-Gender-detectio-using-OpenCV)
            """
        },
        {
            "description": """
                ### 4. Image-Object Classification  
                This project uses MobileNetV2, a pre-trained deep learning model, to classify objects in images with high accuracy. Users can upload images, and the model predicts the most likely object with its confidence score, enabling efficient object recognition  
                **Technologies**: TensorFlow, MobileNetV2  
                [GitHub: Image-Object Classification](https://github.com/Shreyas9882/Image-Oject-Classification)
            """
        },
        {
            "description": """
                ### 5. Music Genre Classification  
                The Music Genre Classification System uses deep learning to classify music tracks into 10 genres. It preprocesses audio into Mel spectrograms and predicts the genre using a pre-trained CNN model. Built with TensorFlow and Streamlit, the app allows users to upload audio files and view predicted genres in real-time, offering an interactive interface  
                **Technologies**: TensorFlow, Streamlit  
                [GitHub: Music Genre Classification](https://github.com/Shreyas9882/Music-Genre-Classification-Using-Deep-Learning)
            """
        }
    ]

    for project in projects:
        st.markdown(project["description"])

# Certifications Section
with st.expander("Certifications"):
    st.markdown("<div class='section-header'>Certifications</div>", unsafe_allow_html=True)
    st.markdown("""
    1. Python for Data Science, AI and Development (Coursera) - November 2024  
    2. Google Data Analytics Professional Certificate (Coursera) - December 2024  
    """)

# Extracurricular Activities Section
with st.expander("Extracurricular Activities"):
    st.markdown("<div class='section-header'>Extracurricular Activities</div>", unsafe_allow_html=True)
    st.markdown("""
    1. **Volunteer, Aatmatrisha**  
       Assisted with stage setup and decorations for the PES University's cultural fest Aatmatrisha.  

    2. **Organiser, Kannada Club**  
       Organized and coordinated Kannada events, promoting Kannada language and culture.  
    """)
