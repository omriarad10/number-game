
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

number = random.randint(1, 100)
attempts = 0
won = False
message = "Guess a number between 1 and 100!"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Guess The Number</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            background: linear-gradient(135deg, #141e30, #243b55);
            color: white;
            font-family: Arial;
            text-align: center;
            padding: 80px 15px;
        }

        .game {
            background: #26354d;
            max-width: 350px;
            margin: auto;
            padding: 35px 20px;
            border-radius: 20px;
            box-shadow: 0 0 25px #111;
        }

        h1 {
            color: #a78bfa;
        }

        input {
            padding: 12px;
            width: 150px;
            font-size: 20px;
            border-radius: 10px;
            border: none;
            text-align: center;
        }

        button {
            padding: 12px 25px;
            margin-top: 15px;
            background: #8b5cf6;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #6d28d9;
        }

        h2 {
            margin-top: 30px;
        }
    </style>
</head>

<body>
    <div class="game">
        <h1>🎯 Guess The Number</h1>

        <p>I'm thinking of a number between 1-100</p>

        <form method="POST">
            <input type="number" name="guess"
                min="1" max="100" required
                placeholder="Your guess"
                {% if won %}disabled{% endif %}>

            <br>

            <button type="submit" {% if won %}disabled{% endif %}>
                GUESS
            </button>
        </form>

        <h2>{{ message }}</h2>
        <p>Attempts: {{ attempts }}</p>

        <form method="POST">
            <button name="reset">🔄 New Game</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global number, attempts, won, message

    if request.method == "POST":

        if "reset" in request.form:
            number = random.randint(1, 100)
            attempts = 0
            won = False
            message = "New game! Guess a number!"

        elif not won:
            guess = int(request.form["guess"])
            attempts += 1

            if guess > number:
                message = "Too HIGH! Try again!"

            elif guess < number:
                message = "Too LOW! Try again!"

            else:
                message = f"You WON! You guessed it in {attempts} tries!"
                won = True

    return render_template_string(
        HTML,
        message=message,
        attempts=attempts,
        won=won
    )


if __name__ == "__main__":
    app.run()
