import pytesseract
import cv2
import json
from google.cloud import texttospeech

# with open('braided-horizon-380818-a343e93b3e20.json') as f:
#     data = json.load(f)

# print(data)

##intialize a connection to google cloud texttospeech client using json key
client = texttospeech.TextToSpeechClient.from_service_account_json('braided-horizon-380818-a343e93b3e20.json')

synthesis_input = texttospeech.SynthesisInput(text="Checking if this working correct so far")

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
