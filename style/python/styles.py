import tkinter as tk

root = tk.Tk()
root.title("GUI Apllication")

#Set up the main frame
frame = tk.Frame(root, bg = "#F8C8DC", height=600, width=800)
frame.pack_propagate(False)
frame.pack()

#Position the No-button
no_button = tk.Button(frame, text="No", bg="#FFB6C1", fg="white", padx=15, pady=32, font=("Nuito",16), bd=0, cursor="hand2")
no_button.place(relx=0.2, rely=0.5, anchor="center")

#Position the Yes-button
yes_button = tk.Button(frame, etext="Yes", bg="#FFB6C1", fg="white", padx=15, pady=32, font=("Nuito",16), bd=0, cursor="hand2")
yes_button.place(relx=0.8, rely=0.5, anchor="center")

#Display header text
header_text = tk.label(frame, text="Your Header Text", font=("Nunito",50,"bold"), bg="#F8C8DC", fg="white")
header_text.place(relx=0.5, rely=0.1, anchor="center")

#Add some space between buttons
frame.grid_rowconfigure(0,weight=1)
frame.grid_rowconfigure(2,weight=1)

#Set up the gif container
gif_container = tk.Frame(frame, bg = "#F8C8DC")
gif_container.place(relx = 0.5, rely = 0.5, anchor = "center")

root.mainloop()