import psutil

from typing import Dict, Any

class Monitor:
  """ Class for monitoring system resources such as CPU, memory, and disk usage """

# Method in the class Monitor for getting CPU usage in float
  def get_cpu_usage(self) -> float:
    """ Get the actual CPU usage in percent """

    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent


# Method in the class Monitor for getting memory information and will return a dictionary with the following keys: percent, used_gb, total_gb
  def get_memory_usage(self) -> Dict[str, Any]:
    """ Get the actual memory usage in percent """

    memory = psutil.virtual_memory()

    used_gb = round(memory.used / (1024**3), 1)
    total_gb = round(memory.total / (1024**3), 1)

    return {
      "percent": memory.percent,
      "used_gb": used_gb,
      "total_gb": total_gb,
    }


# Method in the class Monitor for getting disk usage and looking for the root of the filesystem

  def get_disk_usage(self) -> Dict[str, Any]:
    """ Get the actual disk usage for the root directory """

    disk = psutil.disk_usage("/")
    used_gb = round(disk.used / (1024**3), 1)
    total_gb = round(disk.total / (1024**3), 1)

    return {
      "percent": disk.percent,
      "used_gb": used_gb,
      "total_gb": total_gb,
    }

  def get_system_status(self) -> Dict[str,Any]:
    """ Get complete system status. """
    return {
      "cpu": self.get_cpu_usage(),
      "memory": self.get_memory_usage(),
      "disk": self.get_disk_usage(),
    }


