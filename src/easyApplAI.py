import agentops
from dotenv import load_dotenv
import os


from scrapeLinkedinJobs import scrapeJobs
from applyToJobs import applyAllJobs

agentops.init(os.getenv('AGENTOPS_API_KEY'))

job_url = "https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"

url_list_dict = [
    { 'board': 'greenhouse', 'url': 'https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn' },
    { 'board': 'greenhouse', 'url': 'https://boards.greenhouse.io/seesaw/jobs/4386481006' },
    # { 'board': 'lever', 'url': 'https://jobs.lever.co/avela/53a20cb0-ae0d-4821-a850-c31a40804312/apply?lever-source=LinkedIn' }
]

def url_list_to_listDict(url_list):
    url_list_dict = []
    for url in url_list:
        url_list_dict.append({'board': 'greenhouse', 'url': url})
    return url_list_dict

def easyApplAIEntrypoint():
    # url_list = scrapeJobs()
    # url_list_dict = url_list_to_listDict(url_list)

    for url in url_list_dict:
        print("Applying to: ", url['board'])
        applyAllJobs(url)

    return True


if __name__ == "__main__":
    easyApplAIEntrypoint()