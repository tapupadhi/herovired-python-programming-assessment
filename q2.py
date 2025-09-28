import psutil
import time

# Set the CPU usage threshold
CPU_THRESHOLD = 80  # in percent
CHECK_INTERVAL = 1  # in seconds


def monitor_cpu():
    print("Monitoring CPU usage...\n")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)

            if cpu_usage > CPU_THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    monitor_cpu()
