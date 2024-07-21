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
        url="https://www.google.com",
        local=True
    )
    # click_extension_button(cursor_positions['chrome']["maximize_window"][0], cursor_positions['chrome']["maximize_window"][1])
    return create_response.session_id

def scrapeJobs():
    session_id = createLinkedInSession()