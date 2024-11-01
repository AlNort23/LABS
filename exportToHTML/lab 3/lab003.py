def get_username():
    while True:
        username = input("wats dat username: ").strip()
        if username:
            return username.upper()
        else:
            print("try again, harder")

def get_message():
    while True:
        message = input("wats dat message: ").strip()
        if message:
            return message
        else:
            print("try again, harder")

def get_group():
    while True:
        group_name = input("wat group do u want 2 join? ").strip().upper()
        if group_name:
            return group_name
        else:
            print("try harder")

username = get_username()
print(f"you've been named {username}")

group_name = get_group()
print(f"Ur in {group_name}")

message = get_message()
print(f"Ur message: {message}")