import os
import sys

import winrm

pwsh_command = sys.argv[1]

server_name = os.environ["WIN_SERVER"]
username = os.environ["WIN_UN"]
password = os.environ["WIN_PW"]

print(f"http://{server_name}:5985/wsman")

session = winrm.Session(
    f"http://{server_name}:5985/wsman", auth=(username, password), transport="ntlm"
)

result = session.run_ps(pwsh_command)

print("STDOUT:", result.std_out.decode("utf-8"))
print("STDERR:", result.std_err.decode("utf-8"))

if result.status_code != 0:
    raise Exception(f"Command failed with status code {result.status_code}")
