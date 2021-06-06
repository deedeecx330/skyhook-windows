import os

# IPFS Host
# Example:
# host = "/dns/ipfs.infura.io/tcp/5001/https"

# Temporary directory for file processing
tmpDir = "{}\\AppData\\Local\\Temp".format(os.environ["USERPROFILE"])

# Skyhook directory
skyhookDir = "{}\\AppData\\Local\\".format(os.environ["USERPROFILE"])
