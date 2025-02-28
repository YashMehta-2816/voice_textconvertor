import tkinter as tk
from tkinter import *
from tkinter import messagebox
import speech_recognition as S
from gtts import gTTS
import playsound
import os

def voice_to_text(lang):
    sr = S.Recognizer()
    with S.Microphone() as M:
        try:
            print("Listening...")
            audio=sr.listen(M)
            if lang=="hindi":
                query = sr.recognize_google(audio, language="hi-IN")
                messagebox.showinfo("You Said (Hindi):", query)
            elif lang == "english":
                query = sr.recognize_google(audio, language="en-IN")
                messagebox.showinfo("You Said (English):", query)
            elif lang == "tamil":
                query = sr.recognize_google(audio, language="ta-IN")
                messagebox.showinfo("You Said (Tamil):", query)
        except S.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I couldn't understand.")
        except S.RequestError:
            messagebox.showerror("Error", "Service unavailable.")

def text_to_voice(lang, text):
    if not text.strip():
        messagebox.showerror("Error", "No text provided.")
        return
    try:
        if lang=="hindi":
            tts=gTTS(text=text, lang="hi")
        elif lang=="english":
            tts=gTTS(text=text, lang="en")
        elif lang=="tamil":
            tts= gTTS(text=text,lang="ta")
        else:
            messagebox.showerror("Error", "Invalid language.")
            return
        
        file = "output.mp3"
        tts.save(file)
        playsound.playsound(file)
        os.remove(file)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_voice_to_text_gui():
    window = tk.Toplevel()
    window.title("Voice to Text")
    window.geometry("700x250")

    tk.Label(window, text="Select Language:", font=("Arial", 14)).pack(pady=10)
    languages = [("Hindi", "hindi"), ("English", "english"), ("Tamil", "tamil")]

    for text, lang in languages:
        tk.Button(window, text=text, font=("Arial", 12),
                  command=lambda l=lang: voice_to_text(l)).pack(pady=5)

def create_text_to_voice_gui():
    window = tk.Toplevel()
    window.title("Text to Voice")
    window.geometry("900x450")
    tk.Label(window, text="Enter Text:", font=("Arial", 14)).pack(pady=5)
    text_entry = tk.Text(window, height=5, width=40, font=("Arial", 12))
    text_entry.pack(pady=10)

    tk.Label(window, text="Select Language:", font=("Arial", 14)).pack(pady=10)
    languages = [("Hindi", "hindi"), ("English", "english"), ("Tamil", "tamil")]

    for text, lang in languages:
        tk.Button(window, text=text, font=("Arial", 12),
                  command=lambda l=lang: text_to_voice(l, text_entry.get("1.0", "end").strip())).pack(pady=5)



root = tk.Tk()
root.title("Voice and Text Conversion")
root.geometry("900x450")
root.configure(bg="#305065")
Top_frame=Frame(root,bg="white",width=900,height=160)
Top_frame.place(x=0,y=0)

tk.Label(root, text="Choose Functionality", font=("Arial", 16)).pack(pady=80)

tk.Button(root, text="Voice to Text", font=("Arial", 14), command=create_voice_to_text_gui).pack(pady=25)
tk.Button(root, text="Text to Voice", font=("Arial", 14), command=create_text_to_voice_gui).pack(pady=25)

root.mainloop()
