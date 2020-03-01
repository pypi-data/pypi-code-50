import sys, os
winclip_PATH = os.path.abspath(os.path.dirname(__file__))
try:
    os.environ['PATH'] = ';'.join((winclip_PATH, os.environ['PATH']))
    sys.path.append(winclip_PATH)
except Exception:
    print("Couldn't add winclip to sys.path...\nImageToString path : " +winclip_PATH)

