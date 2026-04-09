# Python System Health Tool

The purpose of this project was to create a Python-based command-line interface that system administrators can use to obtain information about a computer's hardware and verify network connectivity. This tool automatically collects vital system metrics and provides reports that are both human- and machine-readable.

## Features
1. `System Information`: Shows the hostname, operating system, and IP address of the computer
2. `Resource Usage`: Shows how much CPU is being used in real time, how much memory has been used, and how much disk space remains.
3. `Internet Connectivity`: Pings Google DNS(`8.8.8.8`) to check internet status; sees if it is a Windows computer or a Linux/Mac computer calling -n and -c flags, respectively.
4. `Get Uptime`: Calculates and formats by days and hours how long the system has been up and running since the last boot.
5. `Report`: Grants you the ability to write output to the terminal or save the results as either a `.txt` or a `.json` file

## Installation
Clone
- `git clone https://github.com/juan-rami/python-system-health-check.git`
- `cd python-system-health-check`

Virtual Environment:
- `python -m venv venv`
- `source .venv/bin/activate`

Dependencies:
- `pip install -r requirements.txt`

## Usage
- In your terminal: `python system_health_check.py`
- Saving a text report: `python system_health_check.py --output my_report.txt`
- Saving a JSON report: `python system_health_check.py --output data.json --format json`

## Requirements
- Python 3x
- `psutil` libary
