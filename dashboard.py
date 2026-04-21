"""
Dashboard Analytics Module
Generates charts and analytics for the dashboard
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from datetime import datetime

# Use non-interactive backend for server
matplotlib.use('Agg')


def prepare_data(csv_file):
    """
    Load and prepare data from CSV file
    
    Args:
        csv_file (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Prepared dataframe
    """
    try:
        df = pd.read_csv(csv_file)
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None


def generate_job_category_chart(csv_file, output_path):
    """
    Generate job category distribution chart
    
    Args:
        csv_file (str): Path to CSV file
        output_path (str): Path to save the chart
        
    Returns:
        bool: True if successful
    """
    try:
        df = prepare_data(csv_file)
        if df is None or 'Category' not in df.columns:
            return False
        
        # Count categories
        category_counts = df['Category'].value_counts()
        
        # Create figure
        plt.figure(figsize=(10, 6))
        colors = list(plt.cm.Purples(np.linspace(0.4, 0.9, len(category_counts))))
        
        plt.bar(category_counts.index, category_counts.values, color=colors)
        plt.title('Job Category Distribution', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save figure
        plt.savefig(output_path, dpi=100, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return True
    except Exception as e:
        print(f"Error generating category chart: {e}")
        return False


def generate_top_skills_chart(csv_file, output_path):
    """
    Generate top skills chart
    
    Args:
        csv_file (str): Path to CSV file
        output_path (str): Path to save the chart
        
    Returns:
        bool: True if successful
    """
    try:
        df = prepare_data(csv_file)
        if df is None or 'Skills' not in df.columns:
            return False
        
        # Extract and count skills
        all_skills = []
        for skills_str in df['Skills'].dropna():
            # Assuming skills are comma-separated
            skills = [s.strip() for s in str(skills_str).split(',')]
            all_skills.extend(skills)
        
        skill_counts = Counter(all_skills)
        top_skills = dict(skill_counts.most_common(10))
        
        # Create figure
        plt.figure(figsize=(10, 6))
        colors = list(plt.cm.Purples(np.linspace(0.4, 0.9, len(top_skills))))
        
        plt.barh(list(top_skills.keys()), list(top_skills.values()), color=colors)
        plt.title('Top 10 Required Skills', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Frequency', fontsize=12)
        plt.gca().invert_yaxis()
        plt.tight_layout()
        
        # Save figure
        plt.savefig(output_path, dpi=100, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return True
    except Exception as e:
        print(f"Error generating skills chart: {e}")
        return False


def get_dataset_statistics(csv_file):
    """
    Get statistics from dataset
    
    Args:
        csv_file (str): Path to CSV file
        
    Returns:
        dict: Statistics
    """
    try:
        df = prepare_data(csv_file)
        if df is None:
            return {}
        
        # Build unique skills count from the dataset
        all_skills = []
        if 'Skills' in df.columns:
            for skills_str in df['Skills'].dropna():
                skills = [s.strip() for s in str(skills_str).split(',')]
                all_skills.extend(skills)

        stats = {
            'total_records': len(df),
            'columns': list(df.columns),
            'categories': df['Category'].value_counts().to_dict() if 'Category' in df.columns else {},
            'missing_values': df.isnull().sum().to_dict(),
            'unique_skills_count': len(set([skill for skill in all_skills if skill]))
        }
        
        return stats
    except Exception as e:
        print(f"Error getting statistics: {e}")
        return {}


def get_recent_analyses(csv_file, limit=5):
    """
    Build a recent analyses list for display
    """
    try:
        df = prepare_data(csv_file)
        if df is None:
            return []
        
        if 'Name' not in df.columns or 'Category' not in df.columns:
            return []
        
        recent = []
        date_str = datetime.now().strftime('%m/%d/%Y')
        for _, row in df.head(limit).iterrows():
            file_name = f"{str(row['Name']).replace(' ', '_')}.pdf"
            recent.append({
                'file_name': file_name,
                'predicted_job': str(row['Category']),
                'date': date_str,
                'details_url': '#'
            })
        
        return recent
    except Exception as e:
        print(f"Error getting recent analyses: {e}")
        return []


def ensure_charts_exist(static_dir, csv_file):
    """
    Ensure all required charts exist
    
    Args:
        static_dir (str): Path to static directory
        csv_file (str): Path to CSV file
    """
    # Create static directory if doesn't exist
    os.makedirs(static_dir, exist_ok=True)
    
    category_chart = os.path.join(static_dir, 'category_chart.png')
    skills_chart = os.path.join(static_dir, 'skills_chart.png')
    
    # Generate charts if they don't exist
    if not os.path.exists(category_chart):
        generate_job_category_chart(csv_file, category_chart)
    
    if not os.path.exists(skills_chart):
        generate_top_skills_chart(csv_file, skills_chart)
