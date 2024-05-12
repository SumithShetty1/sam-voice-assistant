import threading
import time
import eel
from sam_functions.listen import listen

eel.init("web")


@eel.expose
def display_response(element_id):
    while True:
        try:
            response_file = "web/response.txt"
            input_file = "web/input.txt"

            with open(input_file, "r") as f:
                input_data = f.read().strip()

            with open(response_file, "r") as f:
                response_data = f.read().strip()

            js_script = f"document.getElementById('{element_id}').innerText='Input: {input_data}\nResponse: {response_data}';"
            eel.js(js_script)()
        except Exception as e:
            print(f"Sam: An error occurred: {e}")
        time.sleep(1)


def ui():
    eel.start('index.html', size=(800, 600))


def sam():
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=ui)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


sam()

# Error Support

# import eel
# \Lib\site-packages\eel\__init__.py", line 16, in <module>
# import bottle.ext.websocket as wbs
# ModuleNotFoundError: No module named 'bottle.ext.websocket'

# If you ever get the above error then
# Fortunately, bottle-websocket can be used and should work the same.
# I got mine working using Python 3.12.
# You just have to change an import in __init__.py in the eel module.

# Find this import line:

# import bottle.ext.websocket as wbs

# and replace it with the one below:

# import bottle_websocket as wbs
