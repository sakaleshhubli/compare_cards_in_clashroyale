from flask import Flask, render_template, request
import urllib.request
import json

app = Flask(__name__)

import urllib.request
import json

def get_cards():
    with open("mykey.txt") as f:
        mykey = f.read().strip()

    url = "https://api.clashroyale.com/v1/cards"
    headers = {
        "Authorization": f"Bearer {mykey}"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data["items"]
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        print(e.read().decode())  # This helps you debug further
        return []


@app.route("/", methods=["GET", "POST"])
def index():
    cards = get_cards()
    selected_cards = []
    if request.method == "POST":
        selected_ids = request.form.getlist("cards")
        selected_cards = [card for card in cards if card["id"] in map(int, selected_ids)]
    return render_template("index.html", cards=cards, selected=selected_cards)

if __name__ == "__main__":
    app.run(debug=True)
