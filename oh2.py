import subprocess
import json
from datetime import datetime

def check_opening_hours(opening_hours_str, timestamp=datetime.now()):
    # Convert datetime to timestamp if necessary
    if isinstance(timestamp, datetime):
        timestamp = int(timestamp.timestamp() * 1000)  # Convert to milliseconds

    # Prepare the command
    cmd = ['node', 'opening_hours_check.js', opening_hours_str, str(timestamp)]

    # Execute the JavaScript script
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Parse JSON output
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        raise Exception(f"Error calling opening_hours_check.js: {result.stderr}")

# Example usage
opening_hours_str = 'Mo-We 14:00-24:00; Th 14:00-01:00; Fr 14:00-02:00; Sa 09:00-02:00; Su 14:00-22:00'
timestamp = datetime.now()  # Current time
result = check_opening_hours(opening_hours_str, timestamp)
print(result)
