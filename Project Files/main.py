import pytesseract
import cv2
import json
from google.cloud import texttospeech
# import spacy
# nlp = spacy.load('en_core_web_sm')

# with open('braided-horizon-380818-a343e93b3e20.json') as f:
#     data = json.load(f)

# print(data)

##intialize a connection to google cloud texttospeech client using json key
img = cv2.imread('test.jpeg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to remove noise
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Apply Gaussian blur to smooth the image
blur = cv2.GaussianBlur(thresh, (3, 3), 0)

# Apply Canny edge detection to extract edges
edges = cv2.Canny(blur, 100, 200)

ocrText = pytesseract.image_to_string(edges)
# doc = nlp(text2)
# words = [token.text for token in doc if token.is_alpha]

client = texttospeech.TextToSpeechClient.from_service_account_json('braided-horizon-380818-a343e93b3e20.json')

# for i in range(0,len(words)):
#     print(words[i])
synthesis_input = texttospeech.SynthesisInput(text=ocrText)

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
    print('Audio content written to file output.mp3')
