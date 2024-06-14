import psutil


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    if cpu_usage > CPU_THRESHOLD:
        print(f"CPU usage is high: {cpu_usage}%")

    if memory_usage > MEMORY_THRESHOLD:
        print(f"Memory usage is high: {memory_usage}%")

    if disk_usage > DISK_THRESHOLD:
        print(f"Disk usage is high: {disk_usage}%")

if __name__ == "__main__":
    check_system_health()
