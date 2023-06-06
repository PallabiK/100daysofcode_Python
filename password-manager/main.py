from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)

    password = []
    password += [choice(letters) for _ in range(randint(8, 10))]
    password += [choice(numbers) for _ in range(randint(2, 4))]
    password += [choice(symbols) for _ in range(randint(2, 4))]
    # for i in range(0, nr_letters):
    #     password.append(random.choice(letters))
    # for j in range(0, nr_symbols):
    #     password.append(random.choice(symbols))
    # for k in range(0, nr_numbers):
    #     password.append(random.choice(numbers))

    shuffle(password)

    shuffled_password = ''.join(password)
    password_entry.insert(0, shuffled_password)
    pyperclip.copy(shuffled_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message= "Please don't leave any field empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details you have entered: \n"
        #                                                       f"Email: {email} \nPassword: {password} "
        #                                                       f"\nIs it okay to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No Data File Found.\nEnter Some Data First.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website} details", message=f"Email: {email}\nPassword:{password} ")
        else:
            messagebox.showinfo(title="Oops!", message=f"No Data About {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#website field
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

#Search Button
search_button = Button(text="Search", width=12, command=search_password)
search_button.grid(column=2, row=1)

#Email/Username field:
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "password_manager@gmail.com")

#Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

#add
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()
