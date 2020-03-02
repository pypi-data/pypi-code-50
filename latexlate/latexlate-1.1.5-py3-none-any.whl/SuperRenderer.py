from latexlate import StandartFilters
try:
    from wolframclient.evaluation import WolframLanguageSession
    from wolframclient.language import wlexpr
except ImportError as i:
    WOLFRAM_ENABLED = False

from os import environ

DEFAULT_KERNEL = '/usr/local/Wolfram/Mathematica/11.3/Executables/wolfram'
WOLFRAM_ENABLED = True


class SuperRenderer:
    def __init__(self):
        global WOLFRAM_ENABLED
        if WOLFRAM_ENABLED:
            try:
                kernel = environ['MATHEMATICA_KERNEL']
            except KeyError as k:
                kernel = DEFAULT_KERNEL
            try:
                self.session = WolframLanguageSession(kernel)
            except Exception as e:
                WOLFRAM_ENABLED = False

        self.filters = StandartFilters.filters

    def add_block(self):
        return '%%%%%%%%%%%'

    def add_plot(self, path_to_image,
                 scale_options='scale=1.', caption_text='', label=''):
        text = r'''
\begin{figure}
    \label{{label}}
    \includegraphics[{keyvals}]{{imagefile}}
    \caption{{text}}
\end{figure}
        '''.format(label=label,
                   keyvals=scale_options,
                   imagefile=path_to_image,
                   text=caption_text,
                   figure='{figure}')
        return text

    def to_str(self, value):
        if isinstance(value, float):
            return StandartFilters.preccision(value, 4)
        return str(value)


    def handle_wolram(self, value):
        if not WOLFRAM_ENABLED:
            return 'WOLFRAM IS NOT ENABLED'
        value = self.session.evaluate(wlexpr(value))
        if value is not None:
            return str(value)

        return ''

    def evaluate_wolfram(self, value):
        if not WOLFRAM_ENABLED:
            return ''
        return self.session.evaluate(wlexpr(value))

    def cleanup(self):
        if WOLFRAM_ENABLED:
            self.session.terminate()
