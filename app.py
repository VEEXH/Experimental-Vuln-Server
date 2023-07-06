from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

scan_in_progress = False
scan_complete = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    global scan_in_progress, scan_complete
    url = request.form['url']
    scan_in_progress = True
    # Replace the following line of code with the actual function call for your vulnerability scanner
    # vulnerability_scanner.run_scan(url)
    scan_in_progress = False
    scan_complete = True
    return "Scan completed and report generated."

@app.route('/scan_status')
def scan_status():
    global scan_complete
    if scan_complete:
        scan_complete = False  # Reset the status for future scans
        return jsonify(status='complete')
    else:
        return jsonify(status='in_progress')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

