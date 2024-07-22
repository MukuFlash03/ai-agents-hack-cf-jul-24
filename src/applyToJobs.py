from multion.client import MultiOn
from dotenv import load_dotenv
import os
from extensionClicker import click_extension_button, cursor_positions, managePopups

load_dotenv()

multion_api_key = os.getenv('MULTION_API_KEY')
agentops_api_key = os.getenv('AGENTOPS_API_KEY')

client = MultiOn(
    api_key=multion_api_key,
    agentops_api_key=agentops_api_key,
)

def createJobApplySession(job_url="https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"):
    create_response = client.sessions.create(
        url=job_url,
        local=True
    )
    click_extension_button(cursor_positions['chrome']['greenhouse']["maximize_window"][0], cursor_positions['chrome']['greenhouse']["maximize_window"][1])
    return create_response.session_id

def visitJobApplication(session_id, job_url):
    visit_job_board = client.browse(
        cmd="""
            Click on the Apply button which should be present on the left hand side and you should land on a job application form page. 
            Now don't do anything on the job page, the next function will handle it.
        """,
        url=job_url,
        local=True,
        session_id=session_id
    )
    print(visit_job_board.message)

# def applyToJob(session_id):
#     job_form_response = client.browse(
#         # url=job_url,
#         cmd="""
#                 Wait for the 5 seconds for the form to be filled up.
#                 Click the submit button at the bottom of the form.
#             """,
#         local=True,
#         session_id=session_id
#     )
#     print(job_form_response.message)

def applyToJob(session_id, job_url="https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"):
    job_form_response = client.browse(
        url=job_url,
        cmd=""".
                Click the submit button at the bottom of the form.
                The button will look blue in color and might say submit application.
            """,
        local=True,
        session_id=session_id
    )
    print(job_form_response.message)

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

def applyAllJobs(job_url):
    session_id = createJobApplySession(job_url['url'])
    # visitJobApplication(session_id, job_url['url'])
    managePopups(job_url['board'])
    # applyToJob(session_id)
    applyToJob(session_id, job_url['url'])
