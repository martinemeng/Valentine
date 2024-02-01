import tkinter as tk

root = tk.Tk()
root.title("Python GUI")

# Set up the main frame
frame = tk.Frame(root, bg="#F8C8DC", height=600, width=800)
frame.pack_propagate(False)
frame.pack()

# Position the "No" button
no_button = tk.Button(frame, text="No", bg="#FFB6C1", fg="white", padx=15, pady=32, font=("Nunito", 16), bd=0, cursor="hand2")
no_button.place(relx=0.2, rely=0.5, anchor="center")

# Position the "Yes" button
yes_button = tk.Button(frame, text="Yes", bg="#FFB6C1", fg="white", padx=15, pady=32, font=("Nunito", 16), bd=0, cursor="hand2")
yes_button.place(relx=0.8, rely=0.5, anchor="center")

# Display header text
header_text = tk.Label(frame, text="Your Header Text", font=("Nunito", 50, "bold"), bg="#F8C8DC", fg="white")
header_text.place(relx=0.5, rely=0.1, anchor="center")

# Display text
text_label = tk.Label(frame, text="Your Text", font=("Nunito", 25, "bold"), bg="#F8C8DC", fg="white")
text_label.place(relx=0.5, rely=0.3, anchor="center")

# Set up buttons container
buttons_container = tk.Frame(frame, bg="#F8C8DC")
buttons_container.place(relx=0.5, rely=0.7, anchor="center")

# Set up "GIF" container
gif_container = tk.Frame(frame, bg="#F8C8DC")
gif_container.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()