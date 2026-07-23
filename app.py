from flask import Flask, render_template, request

app = Flask(__name__)

# Very simple, hard-coded exchange rates
RATES = {
    "USD": {"GBP": 0.79, "EUR": 0.92},
    "GBP": {"USD": 1.27, "EUR": 1.16},
    "EUR": {"USD": 1.09, "GBP": 0.86}
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        amount = request.form.get("amount")
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")

        # Check for empty input
        if amount is None or amount.strip() == "":
            error = "Please enter a currency amount."

        else:
            try:
                # Convert entered amount to float
                amount = float(amount)

                # If same currency selected, return original amount
                if from_currency == to_currency:
                    result = amount
                else:
                    rate = RATES[from_currency][to_currency]
                    result = round(amount * rate, 2)

            except ValueError:
                error = "Please enter a numeric amount."

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)