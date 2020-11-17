"""
    link == https://towardsdatascience.com/extracting-speech-from-video-using-python-f0ec7e312d38
    the above is the link to the tutorial of extractive audio & text from video 
"""
import speech_recognition as sr
import moviepy.editor as mp

# converting video to audio 
clip = mp.VideoFileClip(r"video.mp4")

clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()

audio = sr.AudioFile("converted.wav")

with audio as source:
    audio_file = r.record(source)

result = r.recognize_google(audio_file)

# exporting the result to a file.txt 
with open('recognized.txt',mode ='w') as file:
    file.write("Recognized Speech: ")
    file.write("\n")
    file.write(result)
    print("ready!")

