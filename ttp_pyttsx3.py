import pyttsx3

text = 'text to speech demo'

audio = pyttsx3.init()
audio.setProperty('rate', 150)
audio.setProperty('volume', 0.8)

# change the voices
voice = audio.getProperty('voices')

# 0 for male and 1 for female
#audio.setProperty('voice', voice[0].id)      # for male voice   
audio.setProperty('voice', voice[1].id)       # for female voice

# text-to speech conversion
audio.say(text)

# save the audio file
#audio.save_to_file(text, 'test_male_Voice.mp3')
audio.save_to_file(text, 'test_female_Voice.mp3')

audio.runAndWait()