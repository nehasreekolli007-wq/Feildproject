# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.7 or higher
- Windows/Mac/Linux

### Installation

1. **Open Command Prompt/Terminal** in the project folder

2. **Create Virtual Environment**
   ```
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   
   Windows:
   ```
   venv\Scripts\activate
   ```
   
   Mac/Linux:
   ```
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```
   python app.py
   ```

6. **Open Browser**
   Visit: http://localhost:5000

## 📝 Usage

### Step 1: Upload Resume
- Click on upload area
- Select a PDF file containing your resume
- Wait for processing (takes 1-2 seconds)

### Step 2: View Results
- See extracted skills organized by category
- View predicted job role with confidence
- Browse recommended courses and videos
- Check job opportunities

### Step 3: Dashboard
- Click "Dashboard" to see analytics
- View job category distribution
- See top 10 required skills

## 🧪 Test Resume Keywords

Try these keywords in your test resume:

**For AI/ML Engineer:**
- Python, Machine Learning, Deep Learning, TensorFlow, Data Analysis

**For Web Developer:**
- HTML, CSS, JavaScript, React, Angular, Vue

**For Data Analyst:**
- SQL, Python, Tableau, Excel, Data Visualization

**For Cloud Engineer:**
- AWS, Azure, Docker, Kubernetes, Cloud

**For DevOps Engineer:**
- Docker, Kubernetes, Jenkins, CI/CD, Git, Linux

## 💡 Features

✅ Upload PDF resumes
✅ Extract skills automatically
✅ Predict job roles
✅ Get learning resources
✅ Find job opportunities
✅ View analytics dashboard
✅ Beautiful dark theme UI
✅ Responsive design
✅ No database required

## 🆘 Need Help?

1. Check README.md for detailed documentation
2. See requirements.txt for all dependencies
3. Verify all Python files are present
4. Ensure dataset/resume_dataset.csv exists

## 📁 Files Created

```
FPPROJECT/
├── app.py                  (Main Flask app)
├── model.py               (Job prediction)
├── skill_extractor.py     (Skill extraction)
├── dashboard.py           (Analytics)
├── requirements.txt       (Dependencies)
├── README.md              (Full documentation)
├── QUICKSTART.md          (This file)
├── templates/
│   ├── index.html         (Home page)
│   └── dashboard.html     (Analytics page)
├── dataset/
│   └── resume_dataset.csv (Sample data)
├── uploads/               (Uploaded files)
└── static/                (Generated charts)
```

## ⚡ What Each File Does

| File | Purpose |
|------|---------|
| app.py | Main Flask application, handles routes |
| skill_extractor.py | Extracts skills from resume text |
| model.py | Predicts job roles and learning paths |
| dashboard.py | Generates analytics charts |
| index.html | Home page with upload interface |
| dashboard.html | Analytics page with charts |

## 🎯 Project Highlights

- **Full-Stack**: Backend (Python/Flask) + Frontend (HTML/CSS/JS)
- **Real Processing**: Actually extracts text from PDFs
- **Smart Prediction**: Rule-based ML for job role prediction
- **Beautiful UI**: Dark theme with smooth animations
- **Responsive**: Works on desktop, tablet, mobile
- **No Database**: Uses CSV file for data

## 🎓 Learning Value

Perfect for:
- Final Year Projects
- Portfolio Projects
- Learning Flask
- Understanding Web Development
- Practicing Python

## ✅ Everything Works!

All code is tested and working. No errors or missing imports.

Happy Coding! 🚀
