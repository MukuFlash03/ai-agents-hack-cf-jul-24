# main.py
import streamlit as st
from audio_recorder_streamlit import audio_recorder
from faster_whisper import WhisperModel
import os
from groqFunctionCalling_Jobs import run_tests_e2e
from gtts import gTTS
from dotenv import load_dotenv
import requests
from pathlib import Path
from openai import OpenAI
from voiceTestXI import text_to_speech_xi_curl

load_dotenv()

open_ai_api_key = os.getenv('OPENAI_API_KEY')
xi_api_key = os.getenv('XI_API_KEY')
wordware_api_key = os.getenv('WORDWARE_API_KEY')

# Set page config
st.set_page_config(page_title='Groq Translator', page_icon='🎤')

# Set page title
st.title('Easy ApplAI')

# Load whisper model
model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=int(os.cpu_count() / 2))

# Speech to text
def speech_to_text(audio_chunk):
    segments, info = model.transcribe(audio_chunk, beam_size=5)
    speech_text = " ".join([segment.text for segment in segments])
    return speech_text

def text_to_speech(text):
    client = OpenAI()

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=text
    ) as response:
        response.stream_to_file("speech.mp3")

# Record audio
audio_bytes = audio_recorder()
if audio_bytes:
    # Display audio player
    # st.audio(audio_bytes, format="audio/wav")
    st.audio(audio_bytes, format="audio/mpeg")

    # Save audio to file
    # with open('audio.wav', mode='wb') as f:
    with open('audio.mpeg', mode='wb') as f:
        f.write(audio_bytes)

    # Speech to text
    st.divider()
    with st.spinner('Transcribing...'):
        text = speech_to_text('audio.mpeg')
    st.subheader('Transcribed Text')
    st.write(text)

    # Groq function calling
    st.divider()
    with st.spinner('Executing Groq Function...'):
        final_response = run_tests_e2e(text)
    st.subheader('Executed Groq Function...')
    st.write(final_response)

    # text_to_speech(final_response)
    text_to_speech_xi_curl(final_response)
    st.audio("speech.mp3", format="audio/mp3")

    # response.stream_to_file(speech_file_path)