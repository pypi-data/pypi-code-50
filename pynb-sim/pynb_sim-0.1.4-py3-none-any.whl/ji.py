"""
    Jupyter Interface:: This class contains the core methods to interface with the
    Jupyter notebook.
"""
import os, sys
from IPython.core.display import display, HTML


def widget():
    display(HTML("""
    <script src="https://kit.fontawesome.com/aceb3af2d4.js" crossorigin="anonymous"></script>
    <script>
        cellDiv = $("div.cell.code_cell:contains('import pynbsim')");
        cellDiv.addClass('widget_cell');
        inputDiv = cellDiv.find('div.input');
        console.log("Initializing pynbsim widget in div:", cellDiv);
        labelShown = 'Hide widget init'; labelHidden = 'Show widget init';
        if(!cellDiv.attr('loaded')) {
            inputDiv.hide();
            inputHidden = true;
            function toggleInput() {
            if(inputHidden) {
                inputDiv.show();
                $("#toggleInput").find('span').html(labelShown);
            } else {
                inputDiv.hide();
                $("#toggleInput").find('span').html(labelHidden);
            }
            inputHidden = !inputHidden;
            }
            $("<div id='toggleInput'></div>")
                .css('position', 'relative')
                .css('top', '-4px')
                .css('left', '-4px')
                .css('cursor', 'pointer')
                .click(toggleInput)
                .insertBefore(cellDiv)
                .append(
                    $("<span>" + labelHidden + "</span>").css('color', '#999').css('font-style', 'italic')
                ).append(
                    $("<div style='float: right'><i class='fas fa-rocket'></i> Powered by <a href='https://github.com/Helveg/pynb-sim' target='_blank'>pynbsim</a></div>")
                )

            cellDiv.attr('loaded', true);
        }
    </script>
    """))
    with open(os.path.join(os.path.dirname(__file__), "index.html")) as f:
        display(HTML(f.read()))

def progress_text():
    pass
