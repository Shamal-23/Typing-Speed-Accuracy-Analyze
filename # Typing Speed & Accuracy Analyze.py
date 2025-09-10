# Typing Speed & Accuracy Analyze
import tkinter as tk
import random
from time import time

# Custom practice lines
practice_lines = [
    "Coding improves problem solving ability.",
    "Stay consistent to achieve your goals.",
    "Python makes automation simple and powerful.",
    "Learning new skills keeps your mind active."
]

# New function names
def verify_text():
    user_input = text_box.get()
    if user_input == current_line[0]:
        total_time = round(time() - start_time[0], 2)
        words = len(current_line[0].split())
        speed = round(words / total_time * 60, 2)
        output.config(text=f"{total_time} sec | {speed} WPM", fg="green")
    else:
        output.config(text=" Wrong typing, try again!", fg="red")

def new_challenge():
    current_line[0] = random.choice(practice_lines)
    display.config(text=current_line[0])
    text_box.delete(0, tk.END)
    output.config(text="")
    start_time[0] = time()

#  Main Window
app = tk.Tk()
app.title("Typing Speed Challenge")
app.geometry("650x320")
app.config(bg="#f0f8ff")

#  Start with random line
current_line = [random.choice(practice_lines)]
start_time = [time()]

#  Sentence Display
display = tk.Label(app, text=current_line[0], font=("Calibri", 15), wraplength=550, bg="#f0f8ff")
display.pack(pady=20)

#  Input box
text_box = tk.Entry(app, width=60, font=("Calibri", 12))
text_box.pack(pady=10)
text_box.bind("<Return>", lambda e: verify_text())

# Buttons
tk.Button(app, text="Check", command=verify_text, width=14, bg="#87cefa").pack(pady=5)
tk.Button(app, text="Next Line", command=new_challenge, width=14, bg="#d3d3d3").pack(pady=5)

#  Result Label
output = tk.Label(app, text="", font=("Arial", 13), bg="#f0f8ff")
output.pack(pady=20)



app.mainloop()
