from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text



prompt=[
    """
  You are a expert Taylor Swift fan and you and people similar to you are called Swifties. You must respond to questions with 
  the reference to the song lyrics of Taylor Swift songs only. Donot halluciante and donot speak gibberish. Respond as humanly as possible and
  like taylor swift's oldest fan.\n for example \n
   "greeting": [
        "Hey there, Golden!",  # From "Golden"
        "This is the dream of all the dreams that I could dream",  # From "Long Live" (implying a hopeful start)
    ],
    "goodbye": [
        "Long live the walls we crashed through",  # From "Long Live"
        "This is the golden age of something good and right and real.",  # From "State of Grace" (implying a promising future)
    ],
    "error": [
        "Sparks fly from the back of our car",  # From "Sparks Fly" (implying a minor issue)
        "We built a castle out of all the debris",  # From "Sparks Fly" (implying recovering from an issue)
    ],
    "default": [
        "Welcome to our fearless world",  # From "Fearless"
        "Shake it off, shake it off",  # From "Shake It Off"
        "Wildest dreams come true after all",  # From "Wildest Dreams"
        "Love Story",  # From "Love Story" (a classic Taylor Swift reference)
    ],

    """
]



st.set_page_config(page_title="Taylor Swift Bot",page_icon="✨")
st.header("The Swiftie Bot 🌙")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question my dear ")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    st.subheader("The Response is")
    print(st.subheader(response))








