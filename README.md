# Selenium Automation Script README

This README document describes the Selenium automation script used for interacting with a specific web application. (e-csdd)

## Description

The script automates the following web interactions:
1. Navigating to a page by clicking a link.
2. Selecting options from a series of dropdowns and forms.
3. Inputting text into text fields.
4. Clicking buttons and checkboxes.

## Requirements

To run this script, you need:

- Python 3.6 or higher.
- Selenium WebDriver.
- ChromeDriver matching your version of Google Chrome.

## Setup

1. Ensure Python is installed on your machine.
2. Install Selenium by running `pip install selenium`.
3. Download the correct version of ChromeDriver for your version of Google Chrome.
4. Google Chrome must be running with remote debugging enabled on port 9222.

## Running the Script

Before running the script, start Google Chrome with the following command:

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Path\To\A\New\Folder"
Replace `"C:\Path\To\A\New\Folder"` with a path to a folder where Chrome should save user data for this session.

## Notes

- The script includes a `human_like_delay` function that introduces random pauses to simulate human interaction and avoid being detected as a bot.
- Specific IDs and text within the script must correspond to elements on the web page you're interacting with.
- The script currently waits for up to 10 minutes for elements to become clickable. Adjust the wait time in the script according to your network speed and page load times.
- Running this script against a website you do not own or have permission to automate against may violate the website's terms of service.
