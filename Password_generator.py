import string
import secrets

print("Welcome to Password Generator!")

while True:
    try:
        length = int(input("Password kitne characters ka chahiye? "))
        
        if length < 6:
            print("Password kam se kam 6 characters ka hona chahiye.")
            continue
        
        characters = (
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits
            + string.punctuation
        )
        
        password = "".join(secrets.choice(characters) for _ in range(length))
        
        print("\nTumhara naya password:")
        print(password)
        break

    except ValueError:
        print("Sirf number likho, jaise 12 ya 16.")