import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
from pydub import AudioSegment
import random

st.title('Welcome to AI Music Player')

# @st.cache_data
def run():
   
    option = st.selectbox(
'Enter Your Mood',
 ('Happy', 'Sad', 'Angry','Random'))
    if option == 'Happy':
        mp3_files = ["1.mp3", "2.mp3", "3.mp3","4.mp3","5.mp3","6.mp3","7.mp3","8.mp3","9.mp3","10.mp3"]

# Generate a random number
        random_number = random.randint(1, 10)

# Select the corresponding MP3 file
        selected_mp3 = mp3_files[random_number - 1]

        st.title("MP3 Player")
        
        a=selected_mp3
        audio_file = a

        st.audio(audio_file, format='audio/mp3')
    if option =='Sad':
        mp3_files = ["11.mp3", "12.mp3", "13.mp3","14.mp3","15.mp3","16.mp3","17.mp3","18.mp3","19.mp3","20.mp3"]

# Generate a random number
        random_number = random.randint(1, 10)

# Select the corresponding MP3 file
        selected_mp3 = mp3_files[random_number - 1]

        st.title("MP3 Player")
        
        a=selected_mp3
        audio_file = a

        st.audio(audio_file, format='audio/mp3')
    if option =='Angry':
        mp3_files = ["26.mp3", "27.mp3", "28.mp3","29.mp3","30.mp3","31.mp3","32.mp3","33.mp3","34.mp3","35.mp3"]

# Generate a random number
        random_number = random.randint(1, 10)

# Select the corresponding MP3 file
        selected_mp3 = mp3_files[random_number - 1]

        st.title("MP3 Player")
        
        a=selected_mp3
        audio_file = a

        st.audio(audio_file, format='audio/mp3')
    if option =='Random':
        mp3_files = ["21.mp3", "22.mp3", "23.mp3","24.mp3","25.mp3"]

# Generate a random number
        random_number = random.randint(1, 5)

# Select the corresponding MP3 file
        selected_mp3 = mp3_files[random_number - 1]

        st.title("MP3 Player")
        
        a=selected_mp3
        audio_file = a

        st.audio(audio_file, format='audio/mp3')




    st.write('You selected:', option)
    bio = BytesIO()
    bio.write(audio_file)
    bio.seek(0)
    st.download_button('Download Audio File', audio_file, file_download=audio_file.read())

run()
