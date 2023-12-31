from openai import OpenAI
from dotenv import load_dotenv
import os
from ImageToText import TextReader
import cv2 as cv

load_dotenv()
class GPT4:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))
    def predict(self, text):
        prompt = f"What type of document is the following classified as\n\n{text}"
        response = self.client.chat.completions.create(
            model='gpt-4',
            messages=[{'role':'user','content':prompt}]
            )
        return  response.choices[0].message.content

