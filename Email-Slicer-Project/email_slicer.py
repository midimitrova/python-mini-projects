def get_email():
    print('Welcome to email slicer program!')

    email_input = input('Please, enter your email here: ').strip()

    user_name, domain = email_input.split('@')
    domain, extension = domain.split('.')

    print(f'User Name: {user_name}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension}')
    print()


try:
    while True:
        get_email()
except EOFError as e:
    print(e)
