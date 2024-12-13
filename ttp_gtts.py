from gtts import gTTS
import streamlit as st

st.title('Convert Text to Speech')
ttp = st.text_input("Enter your text: ", value="", max_chars=None, type="default", placeholder = None)

if st.button("Convert to Speech"):  
    text_to_speech = gTTS(ttp,lang='hi',tld='com')
    text_to_speech.save('text_to_speech_gtts.wav')
    sound_file = 'text_to_speech_gtts.wav'
    # Display the result
    st.audio(sound_file, autoplay= False)