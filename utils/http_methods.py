import requests

class Http_Methods:

    headers = {'Content-Type' : 'application\json'}
    cookie = ""

    def get(url):
        result = requests.get(url, headers=Http_Methods.headers, cookies=Http_Methods.cookie)
        return result

    def post(url, body):
        result = requests.get(url, json=body, headers=Http_Methods.headers, cookies=Http_Methods.cookie)
        return result

    def put(url, body):
        result = requests.get(url, json=body, headers=Http_Methods.headers, cookies=Http_Methods.cookie)
        return result

    def delete(url, body):
        result = requests.get(url, json=body, headers=Http_Methods.headers, cookies=Http_Methods.cookie)
        return result