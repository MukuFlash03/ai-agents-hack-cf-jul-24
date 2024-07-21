from multion.client import MultiOn
from dotenv import load_dotenv
import os
import time
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
    return create_response.session_id

def applyToJob(job_url="https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"):
    job_form_response = client.browse(
        # cmd="""
        #         Can you please apply for the job by filling out the form?
        #         Use any test data you want to just fill out the form.
        #         For the Resume field, 
        #         Once done, click the submit button at the bottom.
        #     """,
        # cmd="""
        #         Can you please apply for the job by filling out the form?
        #         Once done, click the submit button at the bottom.
        #     """,
        # cmd="""
        #         Can you please apply for the job?
        #         Don't worry about filling out the form, it will be filled out automatically.
        #         Just scroll down to the bottom of the form and click the submit button. 
        #     """,
        url=job_url,
        cmd="""
                Click the submit button at the bottom of the form.
            """,
        local=True,
    )

    return job_form_response.session_id

    # click_extension_button(cursor_positions['chrome']['simplify_button_cross_onsubmit'][0], cursor_positions['chrome']['simplify_button_cross_onsubmit'][1])


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
    # session_id = createJobApplySession(job_url)
    managePopups()
    session_id = applyToJob()
    closeWindowAfterSubmit(session_id)