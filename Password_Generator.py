import random    
import string
import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_database():
        """
        Create the SQLite database and the passwords table if they do not exist.
        """
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

def save_password(name, password):
        """
        Save the password to the SQLite database.
        
        Parameters:
        name (str): The name of the password.
        password (str): The generated password.
        """
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passwords (name, password) VALUES (?, ?)', (name, password))
        conn.commit()
        conn.close()

def retrieve_passwords():
        """
        Retrieve all saved passwords from the SQLite database.
        
        Returns:
        list: A list of tuples containing the name and password.
        """
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, password FROM passwords')
        passwords = cursor.fetchall()
        conn.close()
        return passwords

def display_passwords():
        """
        Display the saved passwords in a new window.
        """
        passwords = retrieve_passwords()
        display_window = tk.Toplevel(root)
        display_window.title("Saved Passwords")
        display_window.geometry("600x400")
        font_style = ("Times New Roman", 18)

        listbox = tk.Listbox(display_window, font=font_style, width=50, height=20)
        listbox.pack(pady=10)

        for name, password in passwords:
            listbox.insert(tk.END, f"Name: {name} - Password: {password}")

def generate_password(length=10, use_upper=True, use_lower=True, use_digits=True, use_special=True):
        """
        Generate a random password based on user preferences.
        
        Parameters:
        length (int): The length of the password to be generated. Default is 10.
        use_upper (bool): Whether to include uppercase letters. Default is True.
        use_lower (bool): Whether to include lowercase letters. Default is True.
        use_digits (bool): Whether to include digits. Default is True.
        use_special (bool): Whether to include special characters. Default is True.
        
        Returns:
        str: A randomly generated password.
        """
        characters = ''
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            raise ValueError("No character types selected")
        
        password = ''.join(random.choice(characters) for i in range(length))
        return password

def generate_password_ui():
        """
        Generate a password based on the user-specified length and preferences from the UI.
        """
        try:
            length = int(entry_length.get())
            use_upper = var_upper.get()
            use_lower = var_lower.get()
            use_digits = var_digits.get()
            use_special = var_special.get()
            
            password = generate_password(length, use_upper, use_lower, use_digits, use_special)
            messagebox.showinfo("Generated Password", f"Generated password: {password}")
            
            if messagebox.askyesno("Save Password", "Do you want to save this password?"):
                save_password_ui(password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

def save_password_ui(password):
        """
        Prompt the user to enter a name for the password and save it to the database.
        """
        save_window = tk.Toplevel(root)
        save_window.title("Save Password")
        save_window.geometry("400x200")
        font_style = ("Times New Roman", 18)

        tk.Label(save_window, text="Enter a name for the password:", font=font_style).pack(pady=10)
        entry_name = tk.Entry(save_window, font=font_style)
        entry_name.pack(pady=5)

        def save():
            name = entry_name.get()
            if name:
                save_password(name, password)
                messagebox.showinfo("Password Saved", f"Password saved as: {name}")
                save_window.destroy()
            else:
                messagebox.showerror("Invalid Input", "Password name cannot be empty")

        tk.Button(save_window, text="Save", command=save, font=font_style).pack(pady=10)

def main():
        """
        Main function to create the UI for password generation.
        """
        global root, entry_length, var_upper, var_lower, var_digits, var_special
        root = tk.Tk()
        root.title("Password Generator")
        root.geometry("600x500")

        font_style = ("Times New Roman", 18)

        tk.Label(root, text="Enter the desired length for the password:", font=font_style).pack(pady=10)
        entry_length = tk.Entry(root, font=font_style)
        entry_length.pack(pady=5)

        var_upper = tk.BooleanVar(value=True)
        var_lower = tk.BooleanVar(value=True)
        var_digits = tk.BooleanVar(value=True)
        var_special = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, font=font_style).pack(anchor='w')
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, font=font_style).pack(anchor='w')
        tk.Checkbutton(root, text="Include Digits", variable=var_digits, font=font_style).pack(anchor='w')
        tk.Checkbutton(root, text="Include Special Characters", variable=var_special, font=font_style).pack(anchor='w')

        tk.Button(root, text="Generate Password", command=generate_password_ui, font=font_style).pack(pady=10)
        tk.Button(root, text="Show Saved Passwords", command=display_passwords, font=font_style).pack(pady=10)

        root.mainloop()

if __name__ == "__main__":
        create_database()
        main()
        main()

import random    
import string
import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_database():
    """
    Create the SQLite database and the passwords table if they do not exist.
    """
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_password(name, password):
    """
    Save the password to the SQLite database.
    
    Parameters:
    name (str): The name of the password.
    password (str): The generated password.
    """
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (name, password) VALUES (?, ?)', (name, password))
    conn.commit()
    conn.close()

def retrieve_passwords():
    """
    Retrieve all saved passwords from the SQLite database.
    
    Returns:
    list: A list of tuples containing the id, name, and password.
    """
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, password FROM passwords')
    passwords = cursor.fetchall()
    conn.close()
    return passwords

def delete_password(password_id):
    """
    Delete a password from the SQLite database.
    
    Parameters:
    password_id (int): The ID of the password to be deleted.
    """
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords WHERE id = ?', (password_id,))
    conn.commit()
    conn.close()

def display_passwords():
    """
    Display the saved passwords in a new window with an option to delete them.
    """
    passwords = retrieve_passwords()
    display_window = tk.Toplevel(root)
    display_window.title("Saved Passwords")
    display_window.geometry("600x400")
    font_style = ("Times New Roman", 18)

    listbox = tk.Listbox(display_window, font=font_style, width=50, height=20)
    listbox.pack(pady=10)

    for password_id, name, password in passwords:
        listbox.insert(tk.END, f"Name: {name} - Password: {password}")
        delete_button = tk.Button(display_window, text="Delete", command=lambda id=password_id: delete_password_ui(id))
        listbox.window_create(tk.END, window=delete_button)
import tkinter as tk

def display_passwords():
    """
    Display the saved passwords in a new window with an option to delete them.
    """
    passwords = retrieve_passwords()
    display_window = tk.Toplevel(root)
    display_window.title("Saved Passwords")
    display_window.geometry("600x400")
    font_style = ("Times New Roman", 18)

    text_widget = tk.Text(display_window, font=font_style, width=50, height=20)
    text_widget.pack(pady=10)

    for password_id, name, password in passwords:
        text_widget.insert(tk.END, f"Name: {name} - Password: {password}\n")
        delete_button = tk.Button(display_window, text="Delete", command=lambda id=password_id: delete_password_ui(id))
        text_widget.window_create(tk.END, window=delete_button)
        text_widget.insert(tk.END, "\n")

    text_widget.config(state=tk.DISABLED)

def generate_password(length=10, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generate a random password based on user preferences.
    
    Parameters:
    length (int): The length of the password to be generated. Default is 10.
    use_upper (bool): Whether to include uppercase letters. Default is True.
    use_lower (bool): Whether to include lowercase letters. Default is True.
    use_digits (bool): Whether to include digits. Default is True.
    use_special (bool): Whether to include special characters. Default is True.
    
    Returns:
    str: A randomly generated password.
    """
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected")
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_password_ui():
    """
    Generate a password based on the user-specified length and preferences from the UI.
    """
    try:
        length = int(entry_length.get())
        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        messagebox.showinfo("Generated Password", f"Generated password: {password}")
        
        if messagebox.askyesno("Save Password", "Do you want to save this password?"):
            save_password_ui(password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def save_password_ui(password):
    """
    Prompt the user to enter a name for the password and save it to the database.
    """
    save_window = tk.Toplevel(root)
    save_window.title("Save Password")
    save_window.geometry("400x200")
    font_style = ("Times New Roman", 18)

    tk.Label(save_window, text="Enter a name for the password:", font=font_style).pack(pady=10)
    entry_name = tk.Entry(save_window, font=font_style)
    entry_name.pack(pady=5)

    def save():
        name = entry_name.get()
        if name:
            save_password(name, password)
            messagebox.showinfo("Password Saved", f"Password saved as: {name}")
            save_window.destroy()
        else:
            messagebox.showerror("Invalid Input", "Password name cannot be empty")

    tk.Button(save_window, text="Save", command=save, font=font_style).pack(pady=10)

def main():
    """
    Main function to create the UI for password generation.
    """
    global root, entry_length, var_upper, var_lower, var_digits, var_special
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("600x500")

    font_style = ("Times New Roman", 18)

    tk.Label(root, text="Enter the desired length for the password:", font=font_style).pack(pady=10)
    entry_length = tk.Entry(root, font=font_style)
    entry_length.pack(pady=5)

    var_upper = tk.BooleanVar(value=True)
    var_lower = tk.BooleanVar(value=True)
    var_digits = tk.BooleanVar(value=True)
    var_special = tk.BooleanVar(value=True)

    tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, font=font_style).pack(anchor='w')
    tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, font=font_style).pack(anchor='w')
    tk.Checkbutton(root, text="Include Digits", variable=var_digits, font=font_style).pack(anchor='w')
    tk.Checkbutton(root, text="Include Special Characters", variable=var_special, font=font_style).pack(anchor='w')

    tk.Button(root, text="Generate Password", command=generate_password_ui, font=font_style).pack(pady=10)
    tk.Button(root, text="Show Saved Passwords", command=display_passwords, font=font_style).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_database()
    main()