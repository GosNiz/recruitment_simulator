from audio_recorder_streamlit import audio_recorder
import streamlit as st

def record_audio():
    # Record audio
    audio_data = audio_recorder(pause_threshold=3.0, sample_rate=48_000, icon_size="2x")
    if audio_data:
        st.audio(audio_data, format="audio/wav")
    return audio_data

# Record audio
audio_data = record_audio()
