def main():
    while True:
        user_password: str = input('Enter a Password (or type "exit" to quit): ').strip()
        
        # Exit condition
        if user_password.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Check for empty input
        if not user_password:
            print("You must enter a password.")
            continue
        
        # Check the password
        check_password(user_password)


def check_password(password: str):
    with open('passwords.txt', 'r')as file:
        common_passwords: list[str] =file.read().splitlines()
        
        
    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: Is Not Uniuqe & is the (#{i}) most common password!')
            return
        
    print(f'{password}: Is Uniuqe')
        

    
if  __name__ == '__main__':
    main()