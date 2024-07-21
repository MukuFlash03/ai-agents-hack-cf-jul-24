from multion.client import MultiOn
from dotenv import load_dotenv
import os
import json
import datetime
import time
from  extensionClicker import click_extension_button, cursor_positions

load_dotenv()

multion_api_key = os.getenv('MULTION_API_KEY')

client = MultiOn(
    api_key=multion_api_key,
)

def createLinkedInSession():
    create_response = client.sessions.create(
        # url="https://linkedin.com",
        # url="https://www.linkedin.com/my-items/saved-jobs/",
        url="https://www.google.com",
        # url="https://www.amazon.com/",
        local=True
    )
    # click_extension_button(cursor_positions['chrome']["maximize_window"][0], cursor_positions['chrome']["maximize_window"][1])
    return create_response.session_id

def retrieveSavedJobs():
    scraped_jobs = []
    # has_more = True
    # page = 1

    retrieve_response = client.retrieve(
            url="https://www.linkedin.com/my-items/saved-jobs/",
            # cmd="""
            #     You should be on the Saved jobs page now.
            #     Now, there should a list of jobs listed below the 'Saved jobs' heading.
            #     Once you are there, do not click anywhere else on any jobs.
            #     There might always be a 'Next' button at the bottom of the list of jobs.
            #     Do not click the other job categories at the top of the page that are besides the 'Saved jobs' heading.
            #     The maximum number of jobs per page is 10.
            #     The jobs might be spread across multiple pages and will be paginated by the URL using the query parameter 'start'.
            #     The 'start' query parameter is the starting index of the jobs list on the current page.
            #     The indexing is zero based and continues from one plus the index of the last job on the previous page.
            #     If you don't see the  'Next' button at the bottom of the list of jobs, then you have reached the last page and you can stop this current retrieve operation.
            #     Each job has these fields visible: Job title, Company, Location, Posted date.
            #     There might also be a 'Actively recruiting' text with a check mark icon next to it, but you can ignore it.
            #     I want you to scrape the job title, company, location, and posted time for each job.
            #     Do not click on the title of the job on the saved jobs list.
            #     Do not click on any other button under the 'My Jobs' heading.
            #     Only go to the next page if you see a Next button towards the bottom right of the jobs list.
            #     If you don't see the  'Next' button at the bottom of the list of jobs, then you have reached the last page and you can stop this current retrieve operation.
            #     Then, I want you to click the 'Next' button to go to the next page, until you reach the last page.
            #     Only scrape the requested data for all the jobs listed on the current page.
            #     """,
            # cmd="""
            #     On the LinkedIn Saved jobs page:
            #     1. Scrape job title, company, location, and posted time for each job (max 10 per page).
            #     2. Ignore 'Actively recruiting' status.
            #     3. Don't click on job titles or other categories.
            # """,
            cmd="Get list of jobs on the Saved jobs page.",
            # cmd="Get following details for each list of jobs on the Saved jobs page - job title, company, location, and posted time.",
            fields=["job_title", "company", "location", "posted_time"],
            scroll_to_bottom=True,
            local=False,
            render_js=True
        )
    
    data = retrieve_response.data
    print(data)
    
    # scraped_jobs.extend(retrieve_response.data)
    # print(f"Scraped page {page} with {len(retrieve_response.data)} jobs")
    # page += 1
    # step_response = client.sessions.step(
    #     session_id=session_id,
    #     cmd="Click the 'Next' button to go to the next page."
    # )
    
    session_id = retrieve_response.session_id

    return (session_id, scraped_jobs)

# Write the scraped jobs to a JSON file
def storeJobsToJson(scraped_jobs):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'scraped_jobs_{timestamp}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(scraped_jobs, f, ensure_ascii=False, indent=4)
    print(f"Job data has been written to data/scrapedJobs/scraped_jobs_{timestamp}.json")

def closeSession(session_id):
    client.sessions.close(
        session_id=session_id
)
    
def resetHighlightedJob():
    click_extension_button(cursor_positions['chrome']["empty_space"][0], cursor_positions['chrome']["empty_space"][1])
    time.sleep(1.5)

def testSearch(session_id):
    retrieve_response = client.retrieve(
        session_id=session_id,
        cmd="""
            Do a search for mobile phones to buy from Amazon.
            You'll have to go to search bar and type out the query 'mobile phones to buy' and press enter.
        """,
        scroll_to_bottom=True,
    )

def testWindow():
    test_response = client.retrieve(
        url="https://www.google.com",
        cmd="""
                Don't do anything, just continue and exit this function.
            """,
        local=True
    )
    return test_response.session_id 


def scrapeJobs():
    session_id = createLinkedInSession()
    # resetHighlightedJob()
    # testSearch(session_id)

    # click_extension_button(cursor_positions['chrome']["maximize_window"][0], cursor_positions['chrome']["maximize_window"][1])
    # session_id, scraped_jobs = retrieveSavedJobs()
    # print(scraped_jobs)
    # storeJobsToJson(scraped_jobs)
    # closeSession(session_id)
    # return scraped_jobs
    # testWindow()



##############################################################################################


# status = "CONTINUE"

# while status == "CONTINUE":
#     step_response = client.sessions.step(
#         session_id=session_id,
#         cmd="""
#             Click on the 'Jobs' tab in the main navigation bar options present at the top of the page to the right of the search bar.
#             The navigation bar options are: Home, My Network, Jobs, Messages, Notifications, and Profile.
#             I want you to click on the 'Jobs' tab only.
#             Then once the Jobs page opens, focus on the left hand sidebar.
#             Below the 'Jobs Update' heading, you should see some menu options: My jobs, Preferences, Interview prep, Job seeker guidance.
#             I want you to click on the 'My jobs' option.
#             Then once the My jobs page opens, focus on the center of the page where the saved jobs are listed.
#             Under the 'My Jobs' heading, you should see these headings: Saved, In Progress, Applied, Archived.
#             To confirm you are on the Saved jobs page, click on the 'Saved jobs' tab.
#         """
#     )
#     status = step_response.status

# scraped_jobs = []
# has_more = True
# page = 1

# while has_more:
#     retrieve_response = client.retrieve(
#         session_id=session_id,
#         cmd="""
#             So, you should be on the Saved jobs page now.
#             Now, there should a list of jobs listed below the 'Saved jobs' heading.
#             The jobs will be spread across multiple pages and will be paginated by the URL using the query parameter 'start'.
#             The 'start' query parameter is the starting index of the jobs list on the current page.
#             The indexing is zero based and continues from one plus the index of the last job on the previous page.
#             The maximum number of jobs per page is 10.
#             Each job has these fields visible: Job title, Company, Location, Posted date.
#             There might also be a 'Actively recruiting' text with a check mark icon next to it, but you can ignore it.
#             I want you to scrape the job title, company, location, and posted time for each job.
#             Then, I want you to click the 'Next' button to go to the next page.
#             Then, I want you to scrape the job title, company, location, and posted time for each job on the next page.
#             Keep doing this until you reach the last page.
#             Do not click on the title of the job on the saved jobs list.
#             Only scrape the requested data for all the jobs listed on the current page and click next until you reach the last page.
#             If you don't see the  'Next' button at the bottom of the list of jobs, then you have reached the last page.
#             You can stop this current retrieve operation.
#             """,
#         fields=["job_title", "company", "location", "posted_time"],
#         scroll_to_bottom=True,
#         # render_js=True
#     )
#     scraped_jobs.extend(retrieve_response.data)
#     print(f"Scraped page {page} with {len(retrieve_response.data)} jobs")
#     page += 1
#     step_response = client.sessions.step(
#         session_id=session_id,
#         cmd="Click the 'Next' button to go to the next page."
#     )
#     has_more = "last page" not in step_response.message
