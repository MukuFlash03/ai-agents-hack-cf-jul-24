# import streamlit as st
# import json
# import glob
# import os

# st.title("LinkedIn Job Scraper Dashboard")

# # Find the most recent JSON file
# json_files = glob.glob('scraped_jobs_*.json')
# latest_file = max(json_files, key=os.path.getctime)

# # Load the JSON data
# with open(latest_file, 'r', encoding='utf-8') as f:
#     jobs = json.load(f)

# # Display job information
# for job in jobs:
#     st.subheader(job['job_title'])
#     st.write(f"Company: {job['company']}")
#     st.write(f"Location: {job['location']}")
#     st.write(f"Posted Time: {job['posted_time']}")
#     st.write("---")

import streamlit as st
import json
import glob
import os
from easyApplAI import easyApplAIEntrypoint

st.set_page_config(layout="wide")
st.title("LinkedIn Job Scraper Dashboard")

if st.button("Scrape Jobs"):
    # easyApplAIEntrypoint()
    scraped_jobs = easyApplAIEntrypoint()
    
    #Display scraped jobs
    st.subheader("Scraped Jobs")
    for job in scraped_jobs:
        st.write(f"**{job['job_title']}**")
        st.write(f"Company: {job['company']}")
        st.write(f"Location: {job['location']}")
        st.write(f"Posted Time: {job['posted_time']}")
        st.write("---")


# Custom CSS to reduce font size and spacing
st.markdown("""
<style>
    .stText p {
        font-size: 14px !important;
        margin-bottom: 0px !important;
    }
    .job-card {
        border: 1px solid #ddd;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Find the most recent JSON file
json_files = glob.glob('data/scrapedJobs/scraped_jobs_*.json')
latest_file = max(json_files, key=os.path.getctime)

# Load the JSON data
with open(latest_file, 'r', encoding='utf-8') as f:
    jobs = json.load(f)

# Display job information in horizontal cards
for job in jobs:
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with st.container():
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        col1.write(f"**{job['job_title']}**")
        col2.write(f"Company: {job['company']}")
        col3.write(f"Location: {job['location']}")
        col4.write(f"Posted Time: {job['posted_time']}")
        st.markdown('</div>', unsafe_allow_html=True)

