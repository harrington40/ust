import re
class PassWordChecker:
    def check_password_validity(passwords):
        valid_passwords = []

        # Split the input sequence of passwords
        password_list = passwords.split(',')

        for password in password_list:
            # Check the criteria using regular expressions
            if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$', password):
                valid_passwords.append(password)

        # Print the valid passwords separated by a comma
        print(','.join(valid_passwords))