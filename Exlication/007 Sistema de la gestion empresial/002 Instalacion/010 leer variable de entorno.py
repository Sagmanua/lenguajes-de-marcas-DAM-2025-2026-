# En el shell:
# echo 'export NOMBRE="BOHDAN"' >> ~/.bashrc
# source ~/.bashrc

import os

print(os.environ.get("NOMBRE"))
