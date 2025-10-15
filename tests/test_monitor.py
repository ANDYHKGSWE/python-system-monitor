from src.monitor import Monitor

def test_monitor_initialization():
  """ Test that the Monitor class can be initialized """

  monitor = Monitor()
  assert isinstance(monitor, Monitor)

def test_get_cpu_usage_returns_float():
  """Test that the get_cpu_usage() returns a float."""
  monitor = Monitor()
  cpu_usage = monitor.get_cpu_usage()
  assert isinstance(cpu_usage, float)
  assert 0.0 <= cpu_usage <= 100.0

def test_get_memory_usage_returns_dict():
  """Test if the get_memory_usage() returns a dictionary with the correct keys."""
  monitor = Monitor()
  memory_usage = monitor.get_memory_usage()
  assert isinstance(memory_usage, dict)
  expected_keys = ["percent", "used_gb", "total_gb"]
  for key in expected_keys:
    assert key in memory_usage

def test_get_disk_usage_returns_dict():
  """Test if the get_disk_usage() returns a dictionary with the correct keys."""
  monitor = Monitor()
  disk_usage = monitor.get_disk_usage()
  assert isinstance(disk_usage, dict)
  expected_keys = ["percent", "used_gb", "total_gb"]
  for key in expected_keys:
    assert key in disk_usage
