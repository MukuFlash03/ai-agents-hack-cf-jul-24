from multion.client import MultiOn
from dotenv import load_dotenv
import os
from extensionClicker import click_extension_button, cursor_positions, managePopups

load_dotenv()

multion_api_key = os.getenv('MULTION_API_KEY')

client = MultiOn(
    api_key=multion_api_key,
)

def createJobApplySession(job_url="https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"):
    create_response = client.sessions.create(
        url=job_url,
        local=True
    )
    click_extension_button(cursor_positions['chrome']['greenhouse']["maximize_window"][0], cursor_positions['chrome']['greenhouse']["maximize_window"][1])
    return create_response.session_id

def applyToJob(session_id, job_url="https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"):
    job_form_response = client.browse(
        url=job_url,
        cmd="""
                Click the submit button at the bottom of the form.
            """,
        local=True,
        session_id=session_id
    )

def closeWindowAfterSubmit(session_id):
    job_submit_response = client.browse(
        cmd="""
                On successful submission you see this message: 'Thank you for applying. Your application has been received. If there is a fit, someone will be getting back to you.
                At this point, close the browser tab.
            """,
        session_id=session_id
    )

    print(job_submit_response.message)

def closeSession(session_id):
    client.sessions.close(
        session_id=session_id
)
    
from concurrent.futures import ThreadPoolExecutor

def applyAllJobs(job_url):
    session_id = createJobApplySession(job_url['url'])
    managePopups(job_url['board'])
    applyToJob(session_id, job_url['url'])
