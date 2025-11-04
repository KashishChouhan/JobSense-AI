JobSense AI -

AI-powered Job Role Recommendation Based on Skills

Smart Career Assistant using NLP + Machine Learning + Django

 Overview:
 
This is an AI-powered web application that recommends the best job roles to a user based on their skills. It identifies matching job opportunities, highlights skill gaps, and even provides learning resources to help users become job-ready.

How It Works:

1️⃣	User enters skills (e.g., “Python, SQL, Power BI”),

2️⃣	NLP cleans and normalizes the skills,

3️⃣	Skills are converted into numeric embeddings using all-MiniLM-L6-v2,

4️⃣	Each job description is also embedded,

5️⃣	Cosine Similarity calculates how closely they match,

6️⃣	Jobs are ranked by match score (%),

7️⃣	Missing skills are shown + learning resources provided,

8️⃣	Jobs are grouped into AI-based clusters (optional feature)

Tech Stack

Frontend        -	HTML, CSS, Bootstrap

Backend         -  Django (Python)

NLP/AI          -	SentenceTransformer (BERT Model), NumPy, Scikit-learn

Database        -  SQLite / MySQL (configurable)

Authentication  -	Django Auth (Login, Signup, Logout)

Version Control	- Git & GitHub

Installation & Setup:
# 1. Clone the repository
git clone https://github.com/KashishChouhan/AI-Powered-Job-Recommendation---Skill-Gap-Analysis-System/pull/new/master
cd job-recommender

# 2. Create Virtual Environment
python -m venv venv
venv/Scripts/activate  # (Windows)
source venv/bin/activate  # (Mac/Linux)

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create Superuser (Admin)
python manage.py createsuperuser

# 6. Run Server
python manage.py runserver

Future Enhancements:

🔹 Resume Upload & Automatic Skill Extraction

🔹 Real-time Jobs using LinkedIn/Indeed APIs

🔹 Email Alerts for Best Matches

🔹 User Dashboard to Track Progress

🔹 AI Resume Improvement Suggestions

Contributions are welcome! Feel free to fork this repo, create a pull request, or raise an issue.

Author
Kashish Chouhan
📧 Email: kashishchouhan1212@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/kashish-chouhan-39603b29b/

