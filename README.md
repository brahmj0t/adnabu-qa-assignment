# AdNabu QA Assignment

## Tech Stack
- Python 3.x
- Selenium
- Pytest

## Setup

1. Install Python 3.x from https://python.org

2. Clone the repository:
   git clone https://github.com/brahmj0t/adnabu-qa-assignment.git

3. Install dependencies:
   pip install -r requirements.txt

## How to Run

pytest test_adnabu_store.py -v

## Generate HTML Report

pip install pytest-html
pytest test_adnabu_store.py -v --html=report.html --self-contained-html

## Test Scenario

**Search and Add to Cart**

Steps automated:
1. Navigate to the password-protected AdNabu test store
2. Enter store password to unlock access
3. Click the search icon in the navigation bar
4. Type "snowboard" in the search input
5. Wait for autocomplete dropdown to appear
6. Click on "The Complete Snowboard" from the dropdown
7. Click the "Add to Cart" button on the product page
8. Verify the cart count updates to 1

## Key Implementation Details

- No hardcoded sleeps — all waits use WebDriverWait with ExpectedConditions
- Modular functions for each action — easy to read and maintain
- Incognito mode ensures a clean cart state on every run
- Config values stored as constants at the top of the file
