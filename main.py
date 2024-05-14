import eel
import os
from take_query import take_query


# Main function to initiate the assistant
if __name__ == '__main__':
    try:
        eel.init("web")

        os.system('start msedge.exe --app="http://localhost:8000/index.html"')

        eel.start('index.html', mode=None, host='localhost', block=True)

    except Exception as e:
        eel.close_window()
        exit()
