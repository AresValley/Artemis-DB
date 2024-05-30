import shutil
import os
from generic_utils import checksum_sha256

shutil.make_archive('sigID', 'tar', 'sigID')

print("SHA256:\t{}".format(checksum_sha256('sigID.tar')))
print("BYTES:\t{}".format(os.path.getsize('sigID.tar')))
