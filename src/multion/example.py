from multion.client import MultiOn
from dotenv import load_dotenv
import os

load_dotenv()

multion_api_key = os.getenv('MULTION_API_KEY')

client = MultiOn(
    api_key=multion_api_key
)

retrieve_response = client.retrieve(
    cmd="Get all posts on Hackernews with title, creator, time created, points as a number, number of comments as a number, and the post URL.",
    url="https://news.ycombinator.com/",
    fields=["title", "creator", "time", "points", "comments", "url"],
    local=True
)

data = retrieve_response.data
print(data)
