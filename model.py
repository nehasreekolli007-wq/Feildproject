"""
Job Role Prediction Model
Uses rule-based logic and simple ML to predict job roles based on extracted skills
"""


def predict_job_role(skills):
    """
    Predict job role based on extracted skills
    
    Args:
        skills (list): List of extracted skills from resume
        
    Returns:
        dict: Dictionary containing job role and confidence
    """
    
    # Convert skills to lowercase for matching
    skills_lower = [skill.lower() for skill in skills]
    skills_joined = ' '.join(skills_lower)
    
    # Define role patterns
    ai_ml_keywords = ['machine learning', 'deep learning', 'tensorflow', 'pytorch', 'keras', 'sklearn', 'scikit-learn', 'data analysis', 'numpy', 'pandas']
    web_dev_keywords = ['html', 'css', 'javascript', 'react', 'angular', 'vue', 'nodejs', 'django', 'flask', 'fastapi']
    data_analyst_keywords = ['sql', 'data analysis', 'tableau', 'power bi', 'excel', 'python', 'pandas']
    cloud_engineer_keywords = ['aws', 'azure', 'google cloud', 'docker', 'kubernetes', 'jenkins', 'linux']
    devops_keywords = ['docker', 'kubernetes', 'jenkins', 'git', 'aws', 'linux', 'ci/cd']
    
    # Initialize scores
    role_scores = {
        'AI/ML Engineer': 0,
        'Web Developer': 0,
        'Data Analyst': 0,
        'Cloud Engineer': 0,
        'DevOps Engineer': 0,
        'Software Engineer': 0
    }
    
    # Calculate scores based on keyword matching
    for keyword in ai_ml_keywords:
        if keyword in skills_joined:
            role_scores['AI/ML Engineer'] += 2
    
    for keyword in web_dev_keywords:
        if keyword in skills_joined:
            role_scores['Web Developer'] += 2
    
    for keyword in data_analyst_keywords:
        if keyword in skills_joined:
            role_scores['Data Analyst'] += 2
    
    for keyword in cloud_engineer_keywords:
        if keyword in skills_joined:
            role_scores['Cloud Engineer'] += 2
    
    for keyword in devops_keywords:
        if keyword in skills_joined:
            role_scores['DevOps Engineer'] += 2
    
    # General software engineer bonus if has any programming language
    programming_languages = ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'go', 'swift']
    for lang in programming_languages:
        if lang in skills_joined:
            role_scores['Software Engineer'] += 1
    
    # Get the highest scored role
    max_score = max(role_scores.values())
    
    if max_score == 0:
        # Default if no keywords matched
        predicted_role = 'Software Engineer'
        confidence = 0.5
    else:
        predicted_role = max(role_scores, key=role_scores.get)
        confidence = min(1.0, max_score / 10.0)  # Normalize to 0-1 range
    
    return {
        'role': predicted_role,
        'confidence': round(confidence, 2),
        'scores': role_scores
    }


def get_role_description(role):
    """
    Get description for a predicted role
    
    Args:
        role (str): Job role name
        
    Returns:
        str: Description of the role
    """
    
    descriptions = {
        'AI/ML Engineer': 'Works with machine learning models, deep learning, and AI systems. Requires strong knowledge of Python, TensorFlow, and data analysis.',
        'Web Developer': 'Develops web applications using HTML, CSS, JavaScript, and modern frameworks. Full-stack development expertise is valued.',
        'Data Analyst': 'Analyzes data using SQL, Python, and visualization tools. Creates insights from datasets and builds reports.',
        'Cloud Engineer': 'Works with cloud platforms like AWS, Azure, and Google Cloud. Manages infrastructure and deployment.',
        'DevOps Engineer': 'Manages CI/CD pipelines, containerization, and infrastructure automation using Docker, Kubernetes, and Jenkins.',
        'Software Engineer': 'General software development role. Works across various platforms and technologies.'
    }
    
    return descriptions.get(role, 'A general development role.')


def get_learning_paths(role):
    """
    Get recommended learning resources for a role
    
    Args:
        role (str): Job role name
        
    Returns:
        dict: Recommended courses and learning resources
    """
    
    learning_paths = {
        'AI/ML Engineer': {
            'courses': [
                {
                    'title': 'Machine Learning Specialization',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/specializations/machine-learning-introduction'
                },
                {
                    'title': 'Deep Learning Specialization',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/specializations/deep-learning'
                },
                {
                    'title': 'Complete ML & Data Science Bootcamp',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/complete-machine-learning-and-data-science-bootcamp/'
                }
            ],
            'videos': [
                {
                    'title': 'Machine Learning Full Course',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=9f6BA4_QKKY'
                },
                {
                    'title': 'TensorFlow Tutorial',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=tpCFfeUEGs8'
                }
            ]
        },
        'Web Developer': {
            'courses': [
                {
                    'title': 'The Complete Web Development Bootcamp',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/the-complete-web-development-bootcamp/'
                },
                {
                    'title': 'Responsive Web Design',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/courses?query=responsive%20web%20design'
                },
                {
                    'title': 'React - The Complete Guide',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/react-the-complete-guide-incl-redux/'
                }
            ],
            'videos': [
                {
                    'title': 'Web Development Tutorial',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=k7T0sy8g4xw'
                },
                {
                    'title': 'React JS Course',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=w7ejDZ8SWv8'
                }
            ]
        },
        'Data Analyst': {
            'courses': [
                {
                    'title': 'Data Analysis with Python',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/courses?query=data%20analysis%20python'
                },
                {
                    'title': 'SQL and Database Design',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/sql-and-database-design-a-practical-guide/'
                },
                {
                    'title': 'Tableau Desktop Specialist Certification',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/tableau-certification/'
                }
            ],
            'videos': [
                {
                    'title': 'SQL Tutorial for Beginners',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=HXV3zeQKqGY'
                },
                {
                    'title': 'Tableau Tutorial',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=aHaOIvR00So'
                }
            ]
        },
        'Cloud Engineer': {
            'courses': [
                {
                    'title': 'AWS Fundamentals',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/courses?query=aws%20fundamentals'
                },
                {
                    'title': 'Ultimate AWS Certified Solutions Architect',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/aws-certified-solutions-architect-associate/'
                },
                {
                    'title': 'Google Cloud Platform Essentials',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/courses?query=google%20cloud%20platform'
                }
            ],
            'videos': [
                {
                    'title': 'AWS Tutorial for Beginners',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=SOTamCx_eCM'
                },
                {
                    'title': 'Kubernetes Tutorial',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=X48VuDVv0Z0'
                }
            ]
        },
        'DevOps Engineer': {
            'courses': [
                {
                    'title': 'Docker & Kubernetes: Complete Guide',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/'
                },
                {
                    'title': 'DevOps Specialization',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/courses?query=devops'
                },
                {
                    'title': 'CI/CD with Jenkins',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/jenkins-course-devops/'
                }
            ],
            'videos': [
                {
                    'title': 'Docker Tutorial',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=fqMOX6JJhGo'
                },
                {
                    'title': 'DevOps Full Course',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/watch?v=OPwU3UVYuxE'
                }
            ]
        },
        'Software Engineer': {
            'courses': [
                {
                    'title': 'Software Engineering Specialization',
                    'platform': 'Coursera',
                    'url': 'https://www.coursera.org/specializations/software-engineering'
                },
                {
                    'title': 'Complete Software Development Bootcamp',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/complete-software-development-bootcamp/'
                },
                {
                    'title': 'Data Structures and Algorithms',
                    'platform': 'Udemy',
                    'url': 'https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/'
                }
            ],
            'videos': [
                {
                    'title': 'Programming Languages Tutorial',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/results?search_query=programming+tutorial'
                },
                {
                    'title': 'Software Development Best Practices',
                    'platform': 'YouTube',
                    'url': 'https://www.youtube.com/results?search_query=software+development+tutorial'
                }
            ]
        }
    }
    
    return learning_paths.get(role, {
        'courses': [],
        'videos': []
    })
