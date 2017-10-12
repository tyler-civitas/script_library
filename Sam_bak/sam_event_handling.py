import car

# KEYSTROKE POSSIBLE VALUES
# 'up', 'down', 'right', 'left', 'space'

# SERVER INSTRUCTIONS
# Navigate to folder (explain)
# python event_server.py 8090 ** OR ** python3 event_server.py 8090
# second web browser to 192.168.1.6:8090

def key_event(keystroke):
    key = keystroke.decode('utf-8')
    print(key.split('=')[1])
    return(key.split('=')[1])