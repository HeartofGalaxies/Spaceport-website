from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

@app.route('/spaceport/translated', methods=['GET'])
def translategb():
    return render_template("translated.html")

@app.route('/spaceport/subscribe', methods=['POST'])
def subscribe():
    emailName = request.form.get('emailName')
    if "@" in emailName:
        return render_template("email_error.html")
    elif emailName == 'SpacePort-FTL-72908':
        return render_template("authorization_error.html")
    elif emailName == '':
        return render_template("empty_field.html")
    elif "+" in emailName:
        return render_template("teleport_error.html")
    else:
        return render_template("net_error.html")

@app.route('/spaceport/tsubscribe', methods=['POST'])
def tsubscribe():
    emailNamet = request.form.get('emailNamet')
    if "@" in emailNamet:
        return render_template("email_error_t.html")
    elif emailNamet == 'SpacePort-FTL-72908':
        return render_template("authorization_error_t.html")
    elif emailNamet == '':
        return render_template("empty_field_t.html")
    elif "+" in emailNamet:
        return render_template("teleport_error_t.html")
    else:
        return render_template("net_error_t.html")

@app.route('/portal', methods=['GET'])
def portalsite():
    return render_template("portal_home.html")