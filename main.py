import psutil
import time

print("Mäter CPU-använding...")

for i in range (5):
  cpu = psutil.cpu_percent(interval=1)
  print(f"CPU usage: {cpu}%")