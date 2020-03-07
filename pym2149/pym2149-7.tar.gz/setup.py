import setuptools

def long_description():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
        name = 'pym2149',
        version = '7',
        description = 'YM2149 emulator supporting YM files, OSC, MIDI to JACK, PortAudio, WAV',
        long_description = long_description(),
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/combatopera/pym2149',
        author = 'Andrzej Cichocki',
        packages = setuptools.find_packages(),
        py_modules = ['bpmtool', 'lc2txt', 'ym2portaudio', 'lc2wav', 'dosound2jack', 'midi2wav', 'ym2wav', 'dosound2wav', 'ym2txt', 'dosound2txt', 'ym2jack', 'midi2jack', 'dsd2wav', 'lc2jack'],
        install_requires = ['aridity', 'diapyr', 'lagoon', 'Lurlene', 'mynblep', 'outjack', 'Pillow', 'PyAudio', 'pyrbo', 'splut', 'timelyOSC'],
        package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
        scripts = [],
        entry_points = {'console_scripts': ['bpmtool=bpmtool:main_bpmtool', 'dosound2jack=dosound2jack:main_dosound2jack', 'dosound2txt=dosound2txt:main_dosound2txt', 'dosound2wav=dosound2wav:main_dosound2wav', 'dsd2wav=dsd2wav:main_dsd2wav', 'lc2jack=lc2jack:main_lc2jack', 'lc2txt=lc2txt:main_lc2txt', 'lc2wav=lc2wav:main_lc2wav', 'midi2jack=midi2jack:main_midi2jack', 'midi2wav=midi2wav:main_midi2wav', 'ym2jack=ym2jack:main_ym2jack', 'ym2portaudio=ym2portaudio:main_ym2portaudio', 'ym2txt=ym2txt:main_ym2txt', 'ym2wav=ym2wav:main_ym2wav', 'mkdsd=ymtests.mkdsd:main_mkdsd']})
