from scrapeLinkedinJobs import scrapeJobs 
from applyToJobs import applyAllJobs


job_url = "https://boards.greenhouse.io/fulfil/jobs/6044634003?source=LinkedIn"

def easyApplAIEntrypoint():
    # scrapeJobs()
    scraped_jobs = scrapeJobs()
    applyAllJobs(job_url)
    return scraped_jobs

if __name__ == "__main__":
    easyApplAIEntrypoint()