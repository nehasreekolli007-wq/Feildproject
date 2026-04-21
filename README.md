# AI Resume Screening and Job Recommendation System

A complete Final Year Project built with Python and Flask that extracts skills from resumes, predicts job roles, and recommends learning resources and job opportunities.

## 📋 Features

### Core Functionality
- **PDF Resume Upload**: Upload resumes in PDF format
- **Skill Extraction**: Automatically extract skills using keyword matching
- **Job Role Prediction**: Predict job roles based on extracted skills
- **Skills Categorization**: Organize skills into categories (Programming, Web Dev, Database, ML, Cloud, etc.)

### Job Role Predictions
The system predicts the following roles:
- AI/ML Engineer
- Web Developer
- Data Analyst
- Cloud Engineer
- DevOps Engineer
- Software Engineer

### Learning Resources
Dynamically generated learning resources for each predicted role:
- **Coursera Courses**
- **Udemy Courses**
- **YouTube Video Tutorials**

### Job Opportunities
Direct links to popular job platforms:
- LinkedIn
- Indeed
- Glassdoor
- AngelList

### Dashboard Analytics
- Job category distribution chart
- Top 10 required skills chart
- Dataset statistics
- Resume data visualization

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: pandas, scikit-learn
- **PDF Extraction**: pdfplumber
- **Charting**: matplotlib
- **File Handling**: Werkzeug

## 📁 Project Structure

```
project/
│
├── app.py                    # Main Flask application
├── model.py                  # Job role prediction logic
├── skill_extractor.py        # Skill extraction module
├── dashboard.py              # Dashboard analytics
├── requirements.txt          # Python dependencies
│
├── dataset/
│   └── resume_dataset.csv    # Sample resume dataset
│
├── templates/
│   ├── index.html            # Home page with resume upload
│   └── dashboard.html        # Analytics dashboard
│
├── static/
│   ├── category_chart.png    # Generated chart (auto-created)
│   └── skills_chart.png      # Generated chart (auto-created)
│
└── uploads/                  # Uploaded resume files
```

## 🚀 Installation & Setup

### Step 1: Clone/Download the Project
Navigate to the project directory:
```bash
cd FPPROJECT
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 📖 Running the Application

### Start the Flask Server
```bash
python app.py
```

You should see output like:
```
==================================================
AI Resume Screening System Starting...
==================================================
Visit: http://localhost:5000
==================================================
```

### Access the Application
Open your browser and go to: **http://localhost:5000**

## 💻 Usage Guide

### 📤 Upload Resume
1. Go to the home page
2. Click on the upload area or choose file
3. Select a PDF resume (Max 16MB)
4. Wait for processing

### 📊 View Results
After uploading, you'll see:
- **Extracted Skills**: All detected skills organized by category
- **Job Role Prediction**: Predicted role with confidence score
- **Learning Resources**: Recommended courses and videos
- **Job Opportunities**: Links to popular job platforms

### 📈 Check Dashboard
1. Click on "Dashboard" link in navigation
2. View statistics from the resume dataset
3. See job category distribution chart
4. View top 10 required skills chart

## 🔧 Customization

### Add More Skills
Edit `skill_extractor.py` and add to `SKILLS_KEYWORDS` dictionary:
```python
SKILLS_KEYWORDS = {
    'YourSkill': ['keyword1', 'keyword2'],
    ...
}
```

### Modify Job Roles
Edit `model.py` and update role keywords in `predict_job_role()` function

### Update Learning Resources
Edit `model.py` in the `get_learning_paths()` function to add/remove courses

### Add Dataset
Replace or update `dataset/resume_dataset.csv` with your own data

## 📊 Dataset Format

The `resume_dataset.csv` should have the following columns:
- `Name`: Employee/Resume name
- `Category`: Job category
- `Skills`: Comma-separated skills
- `Experience`: Years of experience

Example:
```
Name,Category,Skills,Experience
John Smith,AI/ML Engineer,"Python, Machine Learning, TensorFlow",5
```

## 🎨 UI Features

### Dark Theme
- Beautiful purple gradient background
- Professional card-based layout
- Smooth animations and transitions

### Responsive Design
- Works perfectly on desktop, tablet, and mobile
- Flexible grid layouts
- Touch-friendly buttons

### Interactive Elements
- Drag-and-drop file upload
- Real-time feedback messages
- Loading spinners
- Smooth scrolling

## 🔍 Skill Keywords Supported

The system recognizes keywords in these categories:

### Programming Languages
Python, Java, JavaScript, C++, C#, PHP, Ruby, Go, Swift, Kotlin

### Web Development
HTML, CSS, React, Vue, Angular, Django, Flask, FastAPI

### Databases
SQL, MongoDB, Firebase, Redis, Oracle, SQLite

### Data Science & ML
Machine Learning, Deep Learning, TensorFlow, PyTorch, Keras, Pandas, NumPy, Scikit-learn

### Cloud & DevOps
AWS, Azure, Google Cloud, Docker, Kubernetes, Jenkins, Git

### Tools & Others
REST API, GraphQL, Linux, Excel, Tableau, Power BI

## ⚠️ Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "Cannot extract text from PDF"
**Solution**: 
- Ensure PDF is not corrupted
- Try a different PDF file
- Make sure PDF has text (not just scanned images)

### Issue: Charts not showing on dashboard
**Solution**:
- Check if dataset/resume_dataset.csv exists
- Ensure CSV has 'Category' and 'Skills' columns
- Restart the Flask server

### Issue: Port 5000 already in use
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

Then visit: http://localhost:5001

## 📝 Sample Resume for Testing

Create a test PDF or use a resume containing these keywords:
- `Python`, `Machine Learning`, `Deep Learning` → AI/ML Engineer
- `HTML`, `CSS`, `JavaScript`, `React` → Web Developer
- `SQL`, `Data Analysis`, `Python` → Data Analyst
- `AWS`, `Docker`, `Kubernetes` → Cloud Engineer
- `Jenkins`, `Docker`, `Linux` → DevOps Engineer

## 📚 Learning Outcomes

This project demonstrates:
✅ Full-stack web application development
✅ PDF text extraction and processing
✅ Natural Language Processing (keyword matching)
✅ Machine learning predictive models
✅ Data visualization with charts
✅ Responsive UI/UX design
✅ REST API development
✅ Database integration
✅ File handling and security

## 🎯 Future Enhancements

- [ ] Add database for storing upload history
- [ ] Implement advanced ML models (NLP, neural networks)
- [ ] Add user authentication
- [ ] Export reports as PDF
- [ ] Real job listing API integration
- [ ] Resume scoring system
- [ ] Email notifications
- [ ] Admin panel

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Technical Support

For issues or questions:
1. Check the Troubleshooting section
2. Review error messages in the browser console
3. Check Flask server logs in terminal

## ✨ Notes

- Uploads are stored in the `uploads/` folder
- Charts are cached in the `static/` folder
- All file paths are configured correctly in the code
- The system uses keyword matching (rule-based) not ML for skill extraction
- Maximum upload file size is 16MB

## 🎓 For Students

This project is suitable for:
- Final Year Projects (Bachelor's/Master's)
- Portfolio demonstration
- Interview preparation
- Learning Flask and web development
- Understanding AI/ML pipelines

## 🚀 Deploy to Production

### Using Gunicorn (Production Server)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Heroku
1. Create a `Procfile`: `web: gunicorn app:app`
2. Push to Heroku
3. Visit your Heroku app URL

---

**Happy Learning! 🎉**

If you find this project helpful, please give it a ⭐ and share it with others!
