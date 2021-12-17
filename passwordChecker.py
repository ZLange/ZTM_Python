
username = input('What is your username?')
password = input('What is your password?')

password_length = len(password)
hidden_password = '*' * password_length # replace password symbols with *


print(f'{username}, your password is {hidden_password} and it is {password_length} simbols long')