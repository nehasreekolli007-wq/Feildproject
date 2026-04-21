"""
AI Resume Screening and Job Recommendation System
Main Flask Application
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import pdfplumber
import os
from datetime import datetime
import traceback

# Import custom modules
from skill_extractor import extract_skills, get_skill_category
from model import predict_job_role, get_role_description, get_learning_paths
from dashboard import ensure_charts_exist, get_dataset_statistics, get_recent_analyses

# Flask configuration
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'pdf'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static', exist_ok=True)


def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF file
    
    Args:
        pdf_path (str): Path to PDF file
        
    Returns:
        str: Extracted text
    """
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return None


def get_job_opportunities():
    """Get list of job opportunity platforms"""
    return [
        {
            'name': 'LinkedIn',
            'description': 'Find jobs from top companies',
            'url': 'https://www.linkedin.com/jobs/',
            'icon': '💼'
        },
        {
            'name': 'Indeed',
            'description': 'World\'s largest job site',
            'url': 'https://www.indeed.com/',
            'icon': '🔍'
        },
        {
            'name': 'Glassdoor',
            'description': 'Company reviews and salaries',
            'url': 'https://www.glassdoor.com/Job/index.htm',
            'icon': '⭐'
        },
        {
            'name': 'AngelList',
            'description': 'Startup jobs and investor connections',
            'url': 'https://wellfound.com/jobs',
            'icon': '🚀'
        }
    ]


@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_resume():
    """Handle resume upload and processing"""
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check if file is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files are allowed'}), 400
        
        # Save file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
        filename = timestamp + filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from PDF
        resume_text = extract_text_from_pdf(filepath)
        
        if resume_text is None or len(resume_text.strip()) == 0:
            return jsonify({'error': 'Could not extract text from PDF'}), 400
        
        # Extract skills
        skills = extract_skills(resume_text)
        skill_categories = get_skill_category(skills)
        
        # Predict job role
        prediction = predict_job_role(skills)
        role_description = get_role_description(prediction['role'])
        
        # Get learning resources
        learning_resources = get_learning_paths(prediction['role'])
        
        # Get job opportunities
        job_opportunities = get_job_opportunities()
        
        # Prepare response
        response = {
            'success': True,
            'skills': skills,
            'skill_categories': skill_categories,
            'prediction': prediction,
            'role_description': role_description,
            'learning_resources': learning_resources,
            'job_opportunities': job_opportunities,
            'resume_text_preview': resume_text[:500] + '...' if len(resume_text) > 500 else resume_text
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error in upload_resume: {e}")
        print(traceback.format_exc())
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/dashboard')
def dashboard():
    """Dashboard page route"""
    try:
        # Ensure charts exist
        csv_file = 'dataset/resume_dataset.csv'
        ensure_charts_exist('static', csv_file)
        
        # Get dataset statistics and recent analyses
        stats = get_dataset_statistics(csv_file)
        recent_analyses = get_recent_analyses(csv_file)
        
        return render_template('dashboard.html', stats=stats, recent_analyses=recent_analyses)
    
    except Exception as e:
        print(f"Error in dashboard: {e}")
        return render_template('dashboard.html', stats={}, recent_analyses=[])


@app.route('/api/dataset-stats')
def get_stats():
    """API endpoint to get dataset statistics"""
    try:
        csv_file = 'dataset/resume_dataset.csv'
        stats = get_dataset_statistics(csv_file)
        return jsonify(stats)
    except Exception as e:
        print(f"Error getting stats: {e}")
        return jsonify({'error': str(e)}), 500


@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 16MB'}), 413


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return redirect(url_for('index'))


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("="*50)
    print("AI Resume Screening System Starting...")
    print("="*50)
    print("Visit: http://localhost:5000")
    print("="*50)
    
    # Use environment variable for port, default to 5000
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(debug=debug, host='0.0.0.0', port=port)
