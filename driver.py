from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


def calculateTotalMonthlyPayment(loanAmount, interestRate, loanTerm):
    totalMonthlyPayment = loanAmount * (1+interestRate)/12
    return totalMonthlyPayment

@app.route("/", methods = ["POST", "GET"])
def home():
    return render_template("index.html")
#     if request.method == "POST":
#         u_name = request.form["username"]
#         p_name = request.form["playlistName"]
#         p_description = request.form["playlistDescription"]
#         num_songs = request.form["numSongsToAdd"]
#         numSongs = int(num_songs)
#         print(numSongs)
#         timeRange = request.form["timeRange"]
#         print(timeRange)
#         if authenticate(u_name) == True:
#             createAPlaylist(u_name, p_name, p_description, numSongs, timeRange)
            
#         return (redirect(url_for("success")))
#     else:
#         return render_template("index.html")


# @app.route("/success")
# def success():
#     return render_template("success.html")

@app.route("/expenseTracker", methods = ["POST", "GET"])
def expenseTracker():
    totalNeedExpense = 0
    totalWantExpense = 10

    if request.method == "POST":
        if request.form["necessity"] == "Want":
            totalWantExpense += int(request.form["price"])

        elif request.form["necessity"] == "Need":
            totalNeedExpense += int(request.form["price"])

        print(totalWantExpense)
        print(totalNeedExpense)

        return render_template("expenseTracker.html")
    
    elif request.method == "GET":
        return render_template("expenseTracker.html")

@app.route("/studentLoanCalculator", methods = ["POST", "GET"])
def studentLoanCalculator():
    if request.method == "POST":
        loan_amount = int(request.form["loanAmount"])
        interest_rate = float(request.form["interestRate"])
        loan_term = int(request.form["loanTerm"])
        print(loan_amount)
        print(interest_rate)
        print(loan_term)

        totalMonthlyPayment = calculateTotalMonthlyPayment(loan_amount, interest_rate, loan_term)
        
        return render_template("studentLoanCalculator.html", totalMonthlyPayment = totalMonthlyPayment, studentDebt = loan_amount)
    
    elif request.method == "GET":
        return render_template("studentLoanCalculator.html")

if __name__ == "__main__":
    app.run(debug = True)

