# Selenium Test Automation with Allure Reporting

## This project demonstrates automated testing using Selenium WebDriver and reporting with Allure Framework.

### Features:
- Executes tests written with pytest framework.
- Leverages Selenium WebDriver to interact with web applications.
- Generates Allure reports with custom report directories for better organization.
- Includes basic logging functionalities.
- Automates the entire Allure reporting process, including cleaning up previous results, running tests, generating reports, and serving them temporarily.

### Prerequisites:
- Python 3.x
- pip (Python package manager)
- Selenium WebDriver (install using pip install selenium)
- Allure Framework (install using pip install allure-python)
- Web browser (Chrome, Firefox, etc.) with appropriate WebDriver (download from https://chromedriver.chromium.org/ or similar for other browsers)

### Installation:
- Clone this repository or download the code.
- Open a terminal and navigate to the project directory.
- Install required dependencies using pip install -r requirements.txt (assuming you have a requirements.txt file listing dependencies).

### Directory Structure:
```
your_project_name/
├── allure-results/  # Stores test execution results captured by Selenium
├── allure-report/    # Generated Allure reports are placed here
├── test_*.py        # Your automated test cases (written with pytest)  (Moved from tests/)
├── generate_allure_report.py  # Script for generating Allure reports
└── README.md         # This file (instructions and usage)
```

### Execution:
#### Run your test suite and generate the Allure report using:

#### Bash
```
python3 generate_allure_report.py
```

### Accessing the Allure Report:
#### There are two main ways to access the generated Allure report:

#### 1. Using VS Code Live Server Extension (Simple Approach):

- Install the "Live Server" extension by Microsoft (ms-vscode.vscode-live-server) from the VS Code Extensions view (Extensions tab or Ctrl+Shift+X or Cmd+Shift+X on macOS).

- Navigate to the allure-report directory in VS Code after generating the report.

- Right-click on the index.html file (the main report file) and select "Open with Live Server".

#### This will launch a temporary server and open the report in your default web browser, typically at http://localhost:5500.

### 2. Using the Allure Support Extension (Advanced Features):

- Install the "Allure Support" extension by qameta (qameta.allure-vscode) from the VS Code Extensions view.

- Refer to the Allure Support extension documentation for specific functionalities related to generating, serving, and managing Allure reports within VS Code.

#### Note: The temporary serving duration for the automatically generated report depends on the sleep time defined in the serve_allure_report() function within generate_allure_report.py. You might want to adjust this based on your needs.

### Customizing Allure Reports (Optional):
- Modify the allure_utils.py file (or create one) to define custom report generation configurations (e.g., report title, environment details).
- Update the generate_allure_report.py script to use your custom configurations (if applicable).
