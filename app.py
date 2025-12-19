from flask import Flask, render_template, request

app = Flask(__name__)

correct_pin = "1234"
balance = 10000

@app.route("/", methods=["GET", "POST"])
def atm():
    global balance
    message = ""

    if request.method == "POST":
        pin = request.form["pin"]
        action = request.form["action"]
        amount = request.form.get("amount")

        if pin != correct_pin:
            message = "❌ Incorrect PIN"

        else:
            if action == "balance":
                message = f"💰 Balance: ₹{balance}"

            elif action == "deposit":
                balance += int(amount)
                message = f"✅ Deposited ₹{amount}"

            elif action == "withdraw":
                if int(amount) <= balance:
                    balance -= int(amount)
                    message = f"✅ Withdrawn ₹{amount}"
                else:
                    message = "❌ Insufficient Balance"

    return render_template("atm.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
