import subprocess
import time
import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ALLURE_RESULTS_DIR = "./allure-results"
ALLURE_REPORT_DIR = "./allure-report"

# Ensure directories exist
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)
os.makedirs(ALLURE_REPORT_DIR, exist_ok=True)

def clean_allure_results_dir():
    """Clean the Allure results directory."""
    if os.path.exists(ALLURE_RESULTS_DIR):
        shutil.rmtree(ALLURE_RESULTS_DIR)
    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)
    logger.info(f"Cleaned Allure results directory: {ALLURE_RESULTS_DIR}")

def run_tests():
    """Run pytest to execute tests with @pytest.mark.test marker."""
    logger.info(f"Running tests with @pytest.mark.test marker... Results will be stored in: {ALLURE_RESULTS_DIR}")
    result = subprocess.run(['pytest', '-v', '-s', f'--alluredir={ALLURE_RESULTS_DIR}', '-m', 'test'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        logger.info("Tests ran successfully.")
    else:
        logger.error(f"Tests failed: {result.stderr.decode()}")
    return result.returncode

def generate_allure_report():
    """Generate Allure report from custom-allure-results directory."""
    logger.info(f"Generating Allure report... Results will be read from: {ALLURE_RESULTS_DIR}, Report will be generated in: {ALLURE_REPORT_DIR}")
    result = subprocess.run(['allure', 'generate', ALLURE_RESULTS_DIR, '--clean', '-o', ALLURE_REPORT_DIR], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        logger.info("Allure report generated successfully.")
    else:
        logger.error(f"Failed to generate Allure report: {result.stderr.decode()}")

def serve_allure_report():
    """Serve Allure report from custom-allure-report directory."""
    logger.info(f"Serving Allure report temporarily... Results will be served from: {ALLURE_REPORT_DIR}")
    try:
        server_process = subprocess.Popen(['allure', 'serve', ALLURE_RESULTS_DIR], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)  # Adjust delay as needed to ensure the server starts properly
        logger.info("Allure report server started.")
        server_process.terminate()
        logger.info("Allure report server stopped.")
    except Exception as e:
        logger.error(f"Failed to serve Allure report: {e}")

if __name__ == "__main__":
    clean_allure_results_dir()
    if run_tests() == 0:  # Check if tests ran successfully
        generate_allure_report()
        serve_allure_report()
    else:
        generate_allure_report()
        serve_allure_report()
