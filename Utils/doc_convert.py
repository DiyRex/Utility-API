# Only work in linux environment

import os
import subprocess

def convert(file_path):
    try:
        path, filename = os.path.split(file_path)
        file_name = os.path.splitext(os.path.basename(file_path))
        filename = filename + ".pdf"
        cmd = f"unoconv -f pdf {file_path}"
        print(cmd)
        subprocess.call(cmd, shell=True)
        print(f"{file_path} Converted to PDF Sucessfully")
        return os.path.join(path, filename)
    except:
        return "System Error !"

