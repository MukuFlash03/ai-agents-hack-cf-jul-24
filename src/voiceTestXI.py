import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

wordware_api_key = os.getenv('WORDWARE_API_KEY')

def text_to_speech_xi(text):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/cgSgspJ2msm6clMCkdW9"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": xi_api_key
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open('speech_xi.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def download_file(url, ):
    local_filename="speech.mp3"

    # Send a GET request to the URL
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # This will raise an exception for HTTP errors
        
        # Open a local file with write-binary mode
        with open(local_filename, 'wb') as f:
            # Iterate over the response data in chunks
            for chunk in r.iter_content(chunk_size=8192): 
                # Write each chunk to the file
                f.write(chunk)
    
    return local_filename

def extract_output_url(response_text):
    for line in response_text.split('\n'):
        if line.strip():
            try:
                chunk = json.loads(line)
                if 'value' in chunk and 'output' in chunk['value']:
                    return chunk['value']['output']
            except json.JSONDecodeError:
                continue
    return None

def text_to_speech_xi_curl(text):
    url = "https://app.wordware.ai/api/released-app/c8169d79-229d-43ce-9935-0d66b23c6ed9/run"
    headers = {
        "Authorization": f"Bearer {wordware_api_key}"
    }
    data = {
        "inputs": {
            "content": text,
            "voice id": "cgSgspJ2msm6clMCkdW9"
        },
        "version": "^1.0"
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        output_url = extract_output_url(response.text)
        if output_url:
            print("Output URL:", output_url)
            
            # Download the file
            try:
                local_file = download_file(output_url)
                print(f"File downloaded successfully: {local_file}")
            except requests.RequestException as e:
                print(f"Error downloading file: {e}")
        else:
            print("Output URL not found in response")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    sample_text = """
        Born and raised in the charming south, 
        I can add a touch of sweet southern hospitality 
        to your audiobooks and podcasts
    """

    text_to_speech_xi_curl(sample_text)