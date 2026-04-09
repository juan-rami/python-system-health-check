import platform
import socket
import psutil
import shutil
import subprocess
import argparse
import json
from datetime import datetime

def get_system_info():
    hostname = socket.gethostname()
    os_name = platform.system()
    ip_address = socket.gethostbyname(hostname)
    return hostname, os_name, ip_address

def get_resource_usage():
    cpu_use = psutil.cpu_percent(interval = 1)
    memory = psutil.virtual_memory()
    memory_use = memory.percent
    total, used, free = shutil.disk_usage("/")
    disk_space = free // (2 ** 30)
    return cpu_use, memory_use, disk_space

def check_internet_connectivity(os_name):
    if os_name.lower() == "windows":
        piece = "-n"
    else:
        piece = "-c"

    command = ["ping", piece, "1", "8.8.8.8"]
    ping = subprocess.call(command, stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)

    if ping == 0:
        connectivity = "OK"
        result = "SUCCESS"
    else:
        connectivity = "FAILED"
        result = "FAILED"
    return connectivity, result

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = datetime.now().timestamp() - boot_time
    days = int(uptime_seconds // (24 * 3600))
    hours = int((uptime_seconds % (24 * 3600)) // 3600)
    return f"{days} days, {hours} hours"

def generate_text_report(data):
    report = (
        f"## System Health Report\n\n"
        f"Hostname: {data['hostname']}\n"
        f"Operating System: {data['operating_system']}\n"
        f"IP Address: {data['ip_address']}\n\n"
        f"CPU Usage: {data['cpu_usage_percent']}%\n"
        f"Memory Usage: {data['memory_usage_percent']}%\n"
        f"Disk Free Space: {data['disk_free_gb']} GB\n\n"
        f"Internet Connectivity: {data['internet_connectivity']}\n"
        f"Ping to 8.8.8.8: {data['ping_result']}\n\n"
        f"Uptime: {data['uptime']}\n"
    )
    return report

def generate_json_report(data):
    return json.dumps(data, indent = 4)

def save_report(information, file_path):
    try:
        with open(file_path, "w") as s:
            s.write(information)
        print(f"The report is now located in {file_path}")
    except Exception as b:
        print(f"Error saving file: {b}")

def main():
    parser = argparse.ArgumentParser(description = "System Health Check Tool")
    parser.add_argument("--output", help = "File path to save the report")
    parser.add_argument("--format", choices = ["txt", "json"], help = "Ouput format")
    argument = parser.parse_args()

    if argument.format and not argument.output:
        parser.error

    hn, osn, ipa = get_system_info()
    cpu, mem, disk = get_resource_usage()
    con, res = check_internet_connectivity(osn)
    up = get_uptime()

    data_dict = {
        "hostname": hn,
        "operating_system": osn,
        "ip_address": ipa,
        "cpu_usage_percent": cpu,
        "memory_usage_percent": mem,
        "disk_free_gb": disk,
        "internet_connectivity": con,
        "ping_result": res,
        "uptime": up
    }

    if argument.format == "json":
        report = generate_json_report(data_dict)
    else:
        report = generate_text_report(data_dict)

    if argument.output:
        save_report(report, argument.output)
    else:
        print(report)

if __name__ == "__main__":
    main()