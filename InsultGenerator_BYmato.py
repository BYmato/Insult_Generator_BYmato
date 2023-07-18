from tkinter import *
import requests

# Language dictionary

language_dictionary = {
    "English": "en",
    "Turkish": "tr",
    "Czech": "cs",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

# Compliment function / Countdown

countdown = 5

def hug_button():
    hug_response = requests.get("https://complimentr.com/api")
    hug_response.raise_for_status()
    hug_data = hug_response.json()
    insult_label.config(text=hug_data['compliment'].capitalize())

# Insult Generator Function

def insult_generator():
    user_language = drop_down_lang.get()
    if user_language in language_dictionary:
        user_language = language_dictionary[user_language]
    my_paremeters = {
        "lang": user_language,
        "type": "json"
    }
    response = requests.get("https://evilinsult.com/generate_insult.php", params=my_paremeters)
    response.raise_for_status()
    data = response.json()
    insult_label.config(text=data['insult'].capitalize())

    # HUG Function
    global countdown
    countdown -= 1
    if countdown == 0:
        hug_button.pack(pady=10)

# Windows

window = Tk()
window.minsize(400, 400)
window.resizable(False, False)
window.title("Hello, take a Insult")
window.config(bg="#85eac0")
window.iconbitmap("icn.ico")

# Roller

drop_down_lang = StringVar(window)
drop_down_lang.set("Pick a language")
drop_down_lang_options =OptionMenu(window, drop_down_lang, "English", "Turkish", "Spanish", "French", "German", "Czech")
drop_down_lang_options.config(bg="#a7405c", fg="#85eac0", font=("Helvetica", 10, "bold"),)
drop_down_lang_options.pack(pady=10)

# Insult Button

insult_button = Button(text="Give it to me!", bg="#a7405c", fg="#85eac0", font=("Helvetica", 14), padx=15,
                       command=insult_generator)
insult_button.pack(pady=15)

# Label

insult_label = Label(wraplength=250, bg="#85eac0", fg="#a7405c", font=("Helvetica", 18, "bold"))
insult_label.pack(pady=20)

# Hug Button

hug_button = Button(text="I need a hug!", bg="#a7405c", fg="#85eac0", font=("Helvetica", 14), padx=15,
                       command=hug_button)

# Main Loop

window.mainloop()



