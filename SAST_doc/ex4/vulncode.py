from flask import Flask, request, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    toaccount = request.form['toaccount']

    # Vulnerability: No CSRF protection, allowing potential CSRF attacks
    # An attacker could create a malicious page with a form that auto-submits funds

    # Transfer funds logic here...

    return f"Transfer of {amount} to {toaccount} successful!"

if _name_ == '_main_':
    app.run(debug=True)
