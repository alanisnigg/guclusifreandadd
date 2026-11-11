
import random
import string

def generate_username(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    username_length = int(input("Kullanıcı adı uzunluğunu giriniz: "))
    password_length = int(input("Şifre uzunluğunu giriniz: "))

    if username_length <= 0 or password_length <= 0:
        print("Uzunluk 0'dan büyük olmalıdır!")
        return

    username = generate_username(username_length)
    password = generate_password(password_length)

    print(f"\nÜretilen kullanıcı adı: {username}")
    print(f"Üretilen şifre: {password}")


main()
