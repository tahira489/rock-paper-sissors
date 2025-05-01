import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

window = tk.Tk()
window.title("Rock Paper Scissors")

try:
    rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((100, 100)))
    paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((100, 100)))
    scissors_img = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((100, 100)))
except FileNotFoundError:
    messagebox.showerror("Error", "Missing image files! Need: rock.png, paper.png, scissors.png")
    exit()

def play(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if player_choice == computer_choice:
        result = "Tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

def start_game():
    start_button.pack_forget()  
    label.pack(pady=10)  
    
    rock_btn.pack(side="left", padx=10)
    paper_btn.pack(side="left", padx=10)
    scissors_btn.pack(side="left", padx=10)

start_button = tk.Button(window, text="Start Game", command=start_game, font=("Arial", 14))
start_button.pack(pady=50)

label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))

rock_btn = tk.Button(window, image=rock_img, command=lambda: play("rock"))
paper_btn = tk.Button(window, image=paper_img, command=lambda: play("paper"))
scissors_btn = tk.Button(window, image=scissors_img, command=lambda: play("scissors"))

window.mainloop()