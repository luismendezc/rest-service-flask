from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
rest_ip = "rest-service"
rest_port = "2000"


@app.route('/', methods=["GET"])
def index():
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/students".format(rest_ip, rest_port)

    r = requests.get(url=url, headers=header)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    students = r.json()

    return render_template("index.html", **students)


@app.route('/add', methods=["POST"])
def add_student():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    mat_nr = request.form["mat_nr"]

    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "mat_nr": mat_nr

    }
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/students".format(rest_ip, rest_port)

    r = requests.post(json=payload, headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    return redirect("/")


@app.route('/delete', methods=["POST"])
def delete_student():
    id = request.form["id"]

    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/students/{}".format(rest_ip, rest_port, id)

    r = requests.delete(headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    return redirect("/")


@app.route('/update', methods=["POST"])
def update_student():
    id = request.form["id"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    mat_nr = request.form["mat_nr"]

    payload = {
        "id": id
    }
    if first_name != "":
        payload["first_name"] = first_name
    if last_name != "":
        payload["last_name"] = last_name
    if mat_nr != "":
        payload["mat_nr"] = mat_nr

    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/students/{}".format(rest_ip, rest_port, id)

    r = requests.put(json=payload, headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    return redirect("/")


if __name__ == '__main__':
    app.run(port=30000, host="0.0.0.0")
