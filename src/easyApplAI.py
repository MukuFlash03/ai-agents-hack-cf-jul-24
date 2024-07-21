import agentops
from dotenv import load_dotenv

from scrapeLinkedinJobs import scrapeJobs
from applyToJobs import applyAllJobs
import os

agentops.init(os.getenv('AGENTOPS_API_KEY'))

job_url = "https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"

url_list = [
    { 'board': 'greenhouse', 'url': 'https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn' },
    { 'board': 'greenhouse', 'url': 'https://boards.greenhouse.io/seesaw/jobs/4386481006' },
    { 'board': 'lever', 'url': 'https://jobs.lever.co/avela/53a20cb0-ae0d-4821-a850-c31a40804312/apply?lever-source=LinkedIn' }
]

def easyApplAIEntrypoint():
    scrapeJobs()
    # scraped_jobs = scrapeJobs()
    # return scraped_jobs

    for url in url_list:
        print("Applying to: ", url['board'])
        applyAllJobs(url)


if __name__ == "__main__":
    easyApplAIEntrypoint()