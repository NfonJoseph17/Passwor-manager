from cryptography.fernet import Fernet

### Uncomment this for the First time you open file###
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#
#
# write_key()


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("Password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User {user},| Password {fer.decrypt(passw.encode()).decode()}")


def add():
    name = input("Account name: ")
    password = input("Account password: ")

    with open("Password.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Do you want to VIEW passwords or ADD a new password? or Q to quit ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue
