import customtkinter as ctk
import smtplib
from tkinter import messagebox

root = ctk.CTk()

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("green")

# Main Window

root.geometry("600x300")
root.title("Send Emails")
root.configure(bg="black")
root.configure(highlightbackground="black")

# Frames

Frame = ctk.CTkFrame(master=root)
Frame.pack(padx=10, pady=10, fill="both", expand=True)

# Buttons


# Sender Email id

entry1st = ctk.CTkEntry(master=Frame, font=("Arial", 17), width=210, height=30,placeholder_text="Email Id")
entry1st.place(x=20, y=20)

# Sender Email id password


entry2nd = ctk.CTkEntry(master=Frame, font=("Arial", 17), width=210, height=30, placeholder_text="Password")
entry2nd.place(x=300, y=20)

# Sender Email id


entry3rd = ctk.CTkEntry(master=Frame, font=("Arial", 17), width=210, height=30, placeholder_text="Sender Email Id")
entry3rd.place(x=20, y=80)
# Receiver Email id


entry4th = ctk.CTkEntry(master=Frame, font=("Arial", 17), width=210, height=30, placeholder_text="Receiver Email Id")
entry4th.place(x=300, y=80)
# Your message that you need to send


message = ctk.CTkTextbox(master=Frame, font=("Arial", 17), width=300, height=70)
message.place(x=130, y=160)





def on_closing():
	if messagebox.askyesno(title="Calculator", message="Are you sure you want to quit?"):
		root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

msglabel = ctk.CTkLabel(master=Frame, text="Your message", font=("", 16), height=50)
msglabel.place(x=20, y=170)


# preparing for smtp
def send():
	email = entry1st.get()
	pswd = entry2nd.get()
	receiver_mail_01 = entry3rd.get()
	receiver_mail_02 = entry4th.get()
	msg = message.get("1.0", ctk.END)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(email, pswd)
	s.sendmail(receiver_mail_01, receiver_mail_02, msg)
	s.quit()


buttons = ctk.CTkButton(master=Frame, text="send", font=("Arial", 12), width=120, height=30, command=send)
buttons.place(x=215, y=250)

root.mainloop()
