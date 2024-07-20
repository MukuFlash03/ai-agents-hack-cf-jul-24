'''

{
    "request":"/voyager/api/jobs/jobPostings/3974986581?
                decorationId\u003Dcom.linkedin.voyager.deco.jobs.web.shared.WebLightJobPosting-23\u0026",
    "status":200,"body":"bpr-guid-3872833",
    "method":"GET",
    "headers":{"x-li-uuid":"AAYdnkhxpPtMtO4LXSQULA\u003D\u003D"}
}



{
  "request":"/voyager/api/graphql?includeWebMetadata\u003Dtrue\u0026variables\u003D
            (
                start:0,
                query:(
                    flagshipSearchIntent:SEARCH_MY_ITEMS_LEARNING,
                    queryParameters:List(
                        (
                            key:learningContentState,
                            value:List(SAVED,IN_PROGRESS,HISTORY)
                        )
                    )
                )
            )\u0026
            queryId\u003DvoyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2",
  "status":200,
  "body":"bpr-guid-3994208",
  "method":"GET",
  "headers":{"x-li-uuid":"AAYdnsavhBRV5TMSA+B7Eg\u003D\u003D"}
}



{
    "request":"/voyager/api/graphql?includeWebMetadata\u003Dtrue\u0026variables\u003D
            (
                start:0,
                query:
                (
                    flagshipSearchIntent:SEARCH_MY_ITEMS_SAVED_POSTS,
                    queryParameters:List
                    (
                        (
                            key:savedPostType,
                            value:List(ALL)
                        )
                    )
                )
            )\u0026
            queryId\u003DvoyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2",
    "status":200,
    "body":"bpr-guid-3994211",
    "method":"GET",
    "headers":{"x-li-uuid":"AAYdnsavhBRV5TMSA+B7Eg\u003D\u003D"}
}



{
    "request":"/voyager/api/graphql?includeWebMetadata\u003Dtrue\u0026variables\u003D
            (
                start:0,
                query:
                (
                    flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,
                    queryParameters:List
                    (
                        (
                            key:cardType,
                            value:List(SAVED,APPLIED,ARCHIVED,IN_PROGRESS)
                        )
                    )
                )
            )\u0026
            queryId\u003DvoyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2",
    "status":200,
    "body":"bpr-guid-3994215",
    "method":"GET",
    "headers":{"x-li-uuid":"AAYdnsavhBRV5TMSA+B7Eg\u003D\u003D"}
}


https://www.linkedin.com/voyager/api/graphql?
    variables=(
        start:0,
        query:(
            flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,
            queryParameters:List((key:cardType,value:List(SAVED)))
        )
    )&
    queryId=voyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2

'''

import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Define the API endpoint
url = "https://www.linkedin.com/voyager/api/graphql"

# Define the query parameters
params = {
    "variables": "(start:0,query:(flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,queryParameters:List((key:cardType,value:List(SAVED)))))",
    "queryId": "voyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2"
}

# Define headers
headers = {
    "Accept": "application/vnd.linkedin.normalized+json+2.1",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.8",
    "Cookie": "bcookie=\"v=2&f2469b4e-b71b-46c3-82bf-a3b87cec6394\"; bscookie=\"v=1&2024071718143438ac4be1-2e42-44fa-85ef-75527b78c67bAQE5aJGRHYEhBMVaZMCFbDQDMyIqoUNF\"; li_at=AQEDAVDhIHED53GuAAABkMorIWMAAAGQ7jelY1YAfq52L-uFgE95AHokZ2YOj4EMYRxbkq2dalCy644O7ua5KpmFtcCRpXhlVl1FsobisYnqoCaRtUzMQPyusnJx_S4rQaMUwuud-YMhtT_zBzFTyem3; JSESSIONID=ajax:6095855818373291426",
    "Csrf-Token": os.getenv('JSESSIONID').strip('"'),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Li-Lang": "en_US",
    "X-Li-Page-Instance": "urn:li:page:d_flagship3_myitems_savedjobs;btteXlA4QQi+UOXj1Rfc/g==",
    "X-Restli-Protocol-Version": "2.0.0"
}

# Make the GET request
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Response data:", data)
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Response content:", response.text)