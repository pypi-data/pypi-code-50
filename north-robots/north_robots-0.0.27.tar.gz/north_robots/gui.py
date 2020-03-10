from typing import Type, Optional
import time
from threading import Thread
from multiprocessing import Process, Pipe
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout


class EstopWindowProcess:
    """
    This class manages the Qt process and message threads needed to show the EstopWindow in another process
    """

    @staticmethod
    def window_main(message_pipe):
        """ This thread manages the Qt app and window and starts a thread to listen for messages from the main process """

        # flag to control running status of message thread
        global running
        running = True

        def message_main():
            global running
            while running:
                message = message_pipe.recv()
                # quit and close everything if we get a quit message from the main process
                if message == 'quit':
                    window.close()
                    app.quit()
                    running = False

        def send_estop_clicked():
            message_pipe.send('estop_clicked')

        # create a thread to listen for messages from the main process
        message_thread = Thread(target=message_main, daemon=True)
        message_thread.start()

        # start the Qt app and show the window
        app = QApplication([])
        window = EstopWindow(onEstopClicked=send_estop_clicked)
        window.show()
        app.exec_()

        # this point will be reached if the app exits, so cleanup and send a quit message to the main process
        message_pipe.send('quit')
        running = False
        message_thread.join()

    def __init__(self, on_estop_clicked=None):
        self.on_estop_clicked = on_estop_clicked
        self.message_pipe, self.child_pipe = Pipe()
        self.message_thread = Thread(target=self.thread_main, daemon=True)
        self.window_process = Process(target=self.window_main, args=[self.child_pipe])
        self.running = False

    def thread_main(self):
        """ This thread listens for messages from the UI process """

        while self.running:
            message = self.message_pipe.recv()

            if message == 'estop_clicked':
                self.on_estop_clicked()
            elif message == 'quit':
                # send a quit message to the process to unblock it's message thread
                self.message_pipe.send('quit')
                self.running = False

    def start(self):
        """ Start the UI process and show the EstopWindow """
        self.running = True
        self.window_process.start()
        self.message_thread.start()

    def stop(self):
        """ Close the EstopWindow and stop the UI process """
        self.running = False
        # send a quit message to the process, which will also send a quit message to the message thread
        self.message_pipe.send('quit')
        self.message_thread.join()
        self.window_process.join()


class EstopWindow(QMainWindow):
    """
    Simple QMainWindow class that opens an always-on-top window with an E-Stop button
    """

    ESTOP_BUTTON_STYLE = """
        background-color: red;
        color: white;
        font-size: 35px;
        font-weight: bold;
    """

    def __init__(self, parent=None, onEstopClicked=None):
        super().__init__(parent)

        self.onEstopClicked = onEstopClicked

        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint
        )

        self.build_ui()

    def build_ui(self):
        """
        Create widgets needed for the UI
        """
        self.setWindowTitle('N9 E-Stop')
        self.estopButton = QPushButton('E-Stop')
        self.estopButton.setStyleSheet(self.ESTOP_BUTTON_STYLE)

        if self.onEstopClicked:
            self.estopButton.clicked.connect(self.onEstopClicked)

        self.setCentralWidget(self.estopButton)


if __name__ == '__main__':
    gui = EstopWindowProcess(on_estop_clicked=lambda: print('clicked'))
    gui.start()
    time.sleep(100)
    gui.stop()