import tkinter as tk
import subprocess

def start_attendance():
    root.withdraw()   # 👈 GUI hide karega
    subprocess.run(["python", "facedetectio.py"])
    root.deiconify()  # 👈 GUI wapas laayega

# Main window
root = tk.Tk()
root.title("Aditya's Face Attendance System")
root.geometry("500x400")
root.configure(bg="#0f172a")  # dark background

# Title
title = tk.Label(
    root,
    text="👋 Welcome to Aditya's App",
    font=("Helvetica", 18, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=20)

# Description
desc = tk.Label(
    root,
    text="Smart Face Recognition Attendance System\nPowered by AI",
    font=("Arial", 12),
    bg="#0f172a",
    fg="white",
    justify="center"
)
desc.pack(pady=10)

# Button
start_btn = tk.Button(
    root,
    text="🎥 Start Attendance",
    font=("Arial", 12, "bold"),
    bg="#22c55e",
    fg="black",
    padx=20,
    pady=10,
    command=start_attendance
)
start_btn.pack(pady=30)

# Footer
footer = tk.Label(
    root,
    text="Developed by Aditya & Rahul",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=10)

guide = tk.Label(
    root,
    text="Guided by: Assistant Professor Maajid Bashir",
    font=("Arial", 10, "italic"),
    bg="#0f172a",
    fg="#facc15"
)
guide.pack(side="bottom")

root.mainloop()