# test_runner.py
from get_calls import get_data_from_endpoint_1, get_data_from_endpoint_2
from post_calls import post_data_to_endpoint_1, post_data_to_endpoint_2
from utils import generate_html_report

def run_tests():
    results = []

    # Run GET tests
    for func in [get_data_from_endpoint_1, get_data_from_endpoint_2]:
        result = func()
        response = result["response"]
        results.append({
            "name": result["name"],
            "status_code": response.status_code,
            "response": response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
        })

    # Run POST tests
    for func, payload in [(post_data_to_endpoint_1, {"key1": "value1"}), (post_data_to_endpoint_2, {"key2": "value2"})]:
        result = func(payload)
        response = result["response"]
        results.append({
            "name": result["name"],
            "status_code": response.status_code,
            "response": response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
        })

    # Generate HTML report
    report_file = generate_html_report(results)
    print(f"Report generated: {report_file}")

if __name__ == "__main__":
    run_tests()
