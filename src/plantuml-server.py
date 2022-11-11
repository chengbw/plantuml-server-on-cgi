#!/usr/bin/python

import subprocess
import sys
import io

JAVA_PATH = r'/usr/bin/java'
PLANTUML_PATH = r'/home/demo/plantuml.jar'

def do_response():
    # get plantuml code
    fp_in = sys.stdin
    # fp.read() must return bytes
    if isinstance(fp_in, io.TextIOWrapper):
        fp_in = fp_in.buffer
    
    # exec process
    cmd = [JAVA_PATH, '-jar', PLANTUML_PATH, '-tsvg', '-pipe']
    p = subprocess.Popen(cmd, stdin=fp_in, stdout=subprocess.PIPE)

    # return response
    print("Content-Type: image/svg")   
    print()                             # blank line, end of headers
    print(p.stdout.read().decode('utf8'))



if __name__ == "__main__":
    do_response()


