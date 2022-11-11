# Plantuml server on CGI

## Deploy

Put plantuml-server.html to www direcotry.

Put plantuml-server.py to cgi-bin directory.

Visit plantuml-server.html.

## src

### plantuml-server.py

Call by CGI server and return a svg image string.

### plantuml-server.html

Post plantuml code to plantuml-server.py and display svg image.