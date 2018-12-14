from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    inputEmail = request.form.get('inputEmail')
    if "@" in inputEmail:
        return render_template("email_error.html")
    else:
        return render_template("net_error.html")

"""@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)"""