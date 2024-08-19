# Passwor-manager

The Password Manager allows you to securely save and view your passwords. The passwords are encrypted using the `Fernet` symmetric encryption from the `cryptography` library, ensuring that your data is kept safe.

## **Features**

- **Password Encryption**: All stored passwords are encrypted using a secret key.
- **Password Viewing**: View stored passwords in their decrypted form.
- **Password Addition**: Add new passwords to the password file.

  Security

	•	Encryption Key: The encryption key (key.key) must be securely stored. If the key is lost, all encrypted passwords will be irretrievable.
	•	Password File: The Password.txt file stores the encrypted passwords. This file should be kept in a secure location.

Contributing

Contributions are welcome! If you’d like to add new features or improve the existing ones, feel free to fork the repository and submit a pull request.

Steps to Contribute:

	1.	Fork the Project
	2.	Create your Feature Branch (git checkout -b feature/NewFeature)
	3.	Commit your Changes (git commit -m 'Add new feature')
	4.	Push to the Branch (git push origin feature/NewFeature)
	5.	Open a Pull Request
