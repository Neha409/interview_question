import sys
import subprocess
app = sys.argv[1]

cmd = f"systemctl status {app}.service"

output = subprocess.run(cmd, capture_output = True, text = True)

print(output.stdout.strip())