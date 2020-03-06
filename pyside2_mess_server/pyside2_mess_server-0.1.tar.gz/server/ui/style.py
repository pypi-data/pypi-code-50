def search_box_style():
    return """
    QGroupBox{
    background-color:#9bc9ff;
    font:15pt Times Bold;
    color:white;
    border:2px solid gray;
    border-radius:15px;
    }
    """


def search_button_style():
    return """
    QPushButton{
    background-color: #fcc324;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    border-color:beige;
    font:12px;
    padding:6px;
    min-width:6em;
    }
    """


def user_top_frame():
    return """
           QFrame{
           font:20pt Times Bold;
           background-color:white;
           }
           """


def user_bottom_frame():
    return """
        QFrame{
        font:15pt Times Bold;
        background-color:#fcc324
        }
        """
