import os
import certifi
import shutil

certifi_path = certifi.where()
dst = "/Applications/Python 3.10.2/Install Certificates.command"

with open(dst, "w") as f:
    f.write("#!/bin/bash\n")
    f.write(f"export SSL_CERT_FILE={certifi_path}\n")
    f.write(f"echo \"SSL_CERT_FILE={certifi_path}\"")

os.chmod(dst, 0o755)
print(f"Install Certificates.command created at {dst}")
