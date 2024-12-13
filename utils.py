# utils.py
from datetime import datetime

def generate_html_report(results):
    """Generates an HTML report for API test results."""
    report = """
    <html>
    <head>
        <title>API Test Report</title>
    </head>
    <body>
        <h1>API Test Report</h1>
        <table border="1">
            <tr>
                <th>API NAME</th>
                <th>API STATUS</th>
                <th>API CODE</th>
                <th>DATA RESPONSE</th>
            </tr>
    """
    for result in results:
        status = "PASS" if 200 <= result["status_code"] < 300 else "FAIL"
        report += f"""
        <tr>
            <td>{result['name']}</td>
            <td>{status}</td>
            <td>{result['status_code']}</td>
            <td>{result['response']}</td>
        </tr>
        """
    report += """
        </table>
    </body>
    </html>
    """
    file_name = f"reports/api_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(file_name, "w") as f:
        f.write(report)
    return file_name
