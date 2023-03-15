# Webapp Vulnerability Scanner

This webserver hosts a web application that allows users to input a URL and scan it for potential webapp vulnerabilities. It outlines the discovered vulnerabilities and generates a comprehensive report.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Limitations](#limitations)

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required dependencies using the following command:

    ```
    pip install -r requirements.txt
    ```

3. Download and set up your vulnerability scanning script (e.g., OWASP ZAP, etc.) and ensure it is compatible with the web application.

4. Replace the import statement and function call in the `vulnerability_scanner.py` file with the appropriate imports and function calls for your vulnerability scanning script.

## Usage

1. Start the Flask webserver using the following command:

    ```
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Input a URL in the text box and click the 'Scan' button.

4. The web application will display the vulnerability report once the scan is complete.

## Features

- Simple web interface for entering a URL to scan.
- Asynchronous scanning using AJAX for a non-blocking user experience.
- Comprehensive vulnerability report outlining discovered issues.
- Option to save the generated report as a Markdown file on the server.

## Limitations

- This webserver and application are designed for demonstration purposes and may not be suitable for production environments without proper access control, authentication, and error handling.
- The vulnerability scanning functionality depends on the integration of a separate vulnerability scanning script, which must be set up and configured separately.
- The performance and accuracy of the vulnerability scanning are dependent on the chosen vulnerability scanning tool.
