import hashlib

try:
    import requests
except ModuleNotFoundError:
    input("### pip install requests ###")
    raise


def lookup_pwned_api(pwd):
    sha1pwd = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    url = "https://api.pwnedpasswords.com/range/" + head
    req = requests.get(url)
    hashes = (line.split(":") for line in req.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail), 0)
    return sha1pwd, count


def main():
    while True:
        sha1pwd, count = lookup_pwned_api(
            input("Password you want checked:\n"))
        if count == 0:
            print("Your password has not been leaked!\n")
        else:
            print("Change password now! its been leaked ", count, "times\n")
        print(sha1pwd, count)
        if input("Test another one y/n\n").lower() == "y":
            continue
        else:
            break


if __name__ == "__main__":
    main()
