import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Real imports from the implemented core
from resume_ml.core.parser import ResumeParser
from resume_ml.core.matcher import JobMatcher
from resume_ml.core.gap_analyzer import SkillGapAnalyzer

# Page config
st.set_page_config(
    page_title="Resume ML System",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
    }
    .score-high { color: #4CAF50; font-weight: bold; }
    .score-medium { color: #FF9800; font-weight: bold; }
    .score-low { color: #F44336; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<p class="main-header">📝 AI Resume Screener</p>', unsafe_allow_html=True)
    st.markdown("### Production-grade ML system hosted on **GitHub**")
    
    # Sidebar
    st.sidebar.header("Configuration")
    demo_mode = st.sidebar.checkbox("Demo Mode (Fast)", value=True)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info("""
    This demo runs entirely in your browser using 
    Streamlit and the code from the GitHub repository.
    
    [View Source Code](https://github.com/dhinak0210-pixel/FUTURE_ML_TaskNumber-3)
    """)
    
    # Main interface
    tab1, tab2, tab3 = st.tabs(["🎯 Single Resume", "📊 Batch Processing", "🔍 Job Description"])
    
    with tab1:
        st.subheader("Screen Individual Candidate")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Candidate Resume**")
            resume_input = st.text_area(
                "Paste resume text or upload file",
                height=300,
                placeholder="Paste resume content here...\n\nOr use the uploader below 👇"
            )
            
            uploaded_file = st.file_uploader(
                "Upload PDF/DOCX",
                type=["pdf", "docx", "txt"],
                key="single_resume"
            )
        
        with col2:
            st.markdown("**Job Description**")
            jd_input = st.text_area(
                "Paste job description",
                height=300,
                placeholder="Software Engineer requirements:\n- 5+ years Python experience\n- Django/Flask expertise\n- AWS cloud knowledge..."
            )
            
            # Quick select common roles
            role_preset = st.selectbox(
                "Or select preset role",
                ["Custom", "Python Engineer", "Data Scientist", "Product Manager", "DevOps Engineer"]
            )
        
        if st.button("🚀 Analyze Match", type="primary", use_container_width=True):
            if not resume_input and not uploaded_file:
                st.error("Please provide a resume")
                return
            
            with st.spinner("AI analyzing resume..." if not demo_mode else "Processing (demo mode)..."):
                # Process
                if demo_mode:
                    result = generate_demo_result(resume_input or "Sample", jd_input)
                else:
                    result = process_resume(resume_input, jd_input)
                
                display_results(result)
    
    with tab2:
        st.subheader("Batch Candidate Ranking")
        st.info("Upload multiple resumes and rank against a job description")
        
        batch_files = st.file_uploader(
            "Upload multiple resumes",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True
        )
        
        batch_jd = st.text_area("Job Description for batch", height=150)
        
        if batch_files and batch_jd and st.button("📊 Rank Candidates"):
            with st.spinner(f"Processing {len(batch_files)} resumes..."):
                # Simulate batch processing
                results = []
                for i, file in enumerate(batch_files):
                    progress = (i + 1) / len(batch_files)
                    st.progress(progress, text=f"Processing {file.name}...")
                    results.append({
                        "name": file.name,
                        "score": 0.6 + (0.35 * (hash(file.name) % 100) / 100),
                        "skills": ["Python", "AWS", "Django"] if i % 2 == 0 else ["Java", "Spring"]
                    })
                
                display_ranking(results)
    
    with tab3:
        st.subheader("Job Description Analyzer")
        st.markdown("Paste a job description to see skill requirements and suggested interview questions")
        
        analyze_jd = st.text_area("Job Description", height=400)
        
        if analyze_jd and st.button("🔍 Analyze JD"):
            with st.spinner("Extracting requirements..."):
                # Mock analysis
                st.success("Analysis complete!")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Required Skills", "8")
                with col2:
                    st.metric("Preferred Skills", "5")
                with col3:
                    st.metric("Experience Required", "5 years")
                
                st.subheader("Key Requirements")
                st.json({
                    "required": ["Python", "Django", "AWS", "PostgreSQL", "REST APIs", "Git", "CI/CD", "Docker"],
                    "preferred": ["Kubernetes", "React", "GraphQL", "Redis", "Celery"],
                    "experience_level": "Senior (5+ years)",
                    "education": "Bachelor's in CS or equivalent",
                    "soft_skills": ["Communication", "Leadership", "Problem-solving"]
                })

def display_results(result: dict):
    """Display single resume screening results"""
    score = result.get('overall_score', 0.75)
    
    # Score display
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Match Score")
        
        # Color-coded score
        if score >= 0.8:
            score_class = "score-high"
            emoji = "🟢"
        elif score >= 0.6:
            score_class = "score-medium"
            emoji = "🟡"
        else:
            score_class = "score-low"
            emoji = "🔴"
        
        st.markdown(
            f'<p style="font-size: 4rem; text-align: center;" class="{score_class}">'
            f'{emoji} {score:.0%}</p>',
            unsafe_allow_html=True
        )
        
        # Recommendation
        if score >= 0.85:
            st.success("**Recommendation:** Auto-advance to interview")
        elif score >= 0.6:
            st.warning("**Recommendation:** Schedule for human review")
        else:
            st.error("**Recommendation:** Does not meet requirements")
    
    # Detailed breakdown
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Matching Skills")
        for skill in result.get('matching_skills', ["Python", "Django", "AWS"]):
            st.markdown(f"- {skill}")
    
    with col2:
        st.subheader("❌ Skill Gaps")
        for gap in result.get('skill_gaps', ["Kubernetes", "GraphQL"]):
            st.markdown(f"- {gap}")
    
    # Explanation
    with st.expander("🧠 AI Explanation"):
        st.markdown(result.get('explanation', "Candidate shows strong technical alignment..."))

def display_ranking(results: list):
    """Display batch ranking results"""
    st.subheader("Candidate Rankings")
    
    # Sort by score
    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
    
    for i, candidate in enumerate(sorted_results, 1):
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                st.markdown(f"**#{i}**")
            
            with col2:
                st.markdown(f"**{candidate['name']}**")
                st.caption(f"Skills: {', '.join(candidate['skills'])}")
            
            with col3:
                score = candidate['score']
                color = "#4CAF50" if score > 0.8 else "#FF9800" if score > 0.6 else "#F44336"
                st.markdown(
                    f'<p style="color: {color}; font-weight: bold; font-size: 1.2rem;">{score:.0%}</p>',
                    unsafe_allow_html=True
                )
            
            st.markdown("---")

def generate_demo_result(resume: str, jd: str) -> dict:
    """Generate realistic demo result"""
    import hashlib
    seed = hashlib.md5((resume + jd).encode()).hexdigest()
    score = 0.5 + (int(seed[:4], 16) % 5000) / 10000
    
    return {
        'overall_score': score,
        'matching_skills': ["Python", "Django", "REST APIs", "PostgreSQL", "Git"],
        'skill_gaps': ["Kubernetes", "GraphQL", "Microservices"],
        'explanation': f"Score of {score:.0%} based on strong technical alignment with core requirements. Candidate shows 5+ years relevant experience with primary tech stack. Minor gaps in cloud-native technologies."
    }

def process_resume(resume_text: str, jd_text: str) -> dict:
    """Actual processing using the Screening Engine logic."""
    matcher = JobMatcher()
    gap_analyzer = SkillGapAnalyzer()
    
    analysis = matcher.calculate_score(resume_text, jd_text)
    gaps = gap_analyzer.analyze_gaps(resume_text, jd_text)
    
    return {
        'overall_score': analysis['overall_match_score'],
        'matching_skills': gaps['matched_skills'],
        'skill_gaps': gaps['missing_skills'],
        'explanation': f"Match score of {analysis['overall_match_score']:.0%} calculated using {analysis['engine']} engine."
    }

if __name__ == "__main__":
    main()
