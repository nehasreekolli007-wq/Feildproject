"""
Skill Extraction Module
Extracts skills from resume text using keyword matching
"""

# Dictionary of skills and keywords
SKILLS_KEYWORDS = {
    # Programming Languages
    'Python': ['python', 'py'],
    'Java': ['java', 'javadeveloper'],
    'JavaScript': ['javascript', 'js', 'nodejs', 'node.js'],
    'C++': ['c++', 'cpp'],
    'C#': ['c#', 'csharp'],
    'PHP': ['php'],
    'Ruby': ['ruby', 'rails'],
    'Go': ['golang', 'go'],
    'Swift': ['swift'],
    'Kotlin': ['kotlin'],
    
    # Web Development
    'HTML': ['html', 'html5'],
    'CSS': ['css', 'css3', 'sass', 'scss'],
    'React': ['react', 'reactjs'],
    'Vue': ['vue', 'vuejs'],
    'Angular': ['angular'],
    'Django': ['django'],
    'Flask': ['flask'],
    'FastAPI': ['fastapi'],
    
    # Databases
    'SQL': ['sql', 'mysql', 'postgresql'],
    'MongoDB': ['mongodb', 'mongo'],
    'Firebase': ['firebase'],
    'Redis': ['redis'],
    'Oracle': ['oracle'],
    'SQLite': ['sqlite'],
    
    # Data Science & ML
    'Machine Learning': ['machine learning', 'ml', 'supervised learning', 'unsupervised learning'],
    'Deep Learning': ['deep learning', 'neural network', 'cnn', 'rnn', 'lstm'],
    'Data Analysis': ['data analysis', 'data visualization', 'analytics'],
    'Pandas': ['pandas'],
    'NumPy': ['numpy', 'np'],
    'Scikit-learn': ['scikit-learn', 'sklearn'],
    'TensorFlow': ['tensorflow'],
    'PyTorch': ['pytorch'],
    'Keras': ['keras'],
    
    # Cloud & DevOps
    'AWS': ['aws', 'amazon web services', 'ec2', 's3'],
    'Azure': ['azure', 'microsoft azure'],
    'Google Cloud': ['google cloud', 'gcp', 'cloud platform'],
    'Docker': ['docker'],
    'Kubernetes': ['kubernetes', 'k8s'],
    'Jenkins': ['jenkins'],
    'Git': ['git', 'github', 'gitlab', 'bitbucket'],
    
    # Other Tools & Frameworks
    'REST API': ['rest api', 'restful', 'api design'],
    'GraphQL': ['graphql'],
    'Linux': ['linux', 'ubuntu'],
    'Windows': ['windows'],
    'MacOS': ['macos', 'mac'],
    'Excel': ['excel', 'vba'],
    'Tableau': ['tableau'],
    'Power BI': ['power bi', 'powerbi'],
}


def extract_skills(resume_text):
    """
    Extract skills from resume text
    
    Args:
        resume_text (str): The text content of the resume
        
    Returns:
        list: List of extracted skills
    """
    # Convert resume text to lowercase for matching
    resume_lower = resume_text.lower()
    
    # Extract skills
    extracted_skills = []
    
    for skill, keywords in SKILLS_KEYWORDS.items():
        for keyword in keywords:
            if keyword in resume_lower:
                if skill not in extracted_skills:
                    extracted_skills.append(skill)
                break  # Break inner loop once a skill is found
    
    return extracted_skills


def get_skill_category(skills):
    """
    Categorize extracted skills
    
    Args:
        skills (list): List of extracted skills
        
    Returns:
        dict: Skills organized by category
    """
    categories = {
        'Programming': [],
        'Web Development': [],
        'Database': [],
        'Data Science & ML': [],
        'Cloud & DevOps': [],
        'Tools': []
    }
    
    programming_skills = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'PHP', 'Ruby', 'Go', 'Swift', 'Kotlin']
    web_skills = ['HTML', 'CSS', 'React', 'Vue', 'Angular', 'Django', 'Flask', 'FastAPI']
    database_skills = ['SQL', 'MongoDB', 'Firebase', 'Redis', 'Oracle', 'SQLite']
    ml_skills = ['Machine Learning', 'Deep Learning', 'Data Analysis', 'Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'PyTorch', 'Keras']
    devops_skills = ['AWS', 'Azure', 'Google Cloud', 'Docker', 'Kubernetes', 'Jenkins', 'Git']
    tools = ['REST API', 'GraphQL', 'Linux', 'Windows', 'MacOS', 'Excel', 'Tableau', 'Power BI']
    
    for skill in skills:
        if skill in programming_skills:
            categories['Programming'].append(skill)
        elif skill in web_skills:
            categories['Web Development'].append(skill)
        elif skill in database_skills:
            categories['Database'].append(skill)
        elif skill in ml_skills:
            categories['Data Science & ML'].append(skill)
        elif skill in devops_skills:
            categories['Cloud & DevOps'].append(skill)
        else:
            categories['Tools'].append(skill)
    
    # Remove empty categories
    return {k: v for k, v in categories.items() if v}
