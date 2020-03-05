from setuptools import setup, find_packages

setup(
    name='Orange_Vision',
    version="0.0.4",
    description="FRC Orange Vision API",
    long_description='API to run inference on image data coming from the camera.',
    author='Danny Dasilva',
    author_email='dannydasilva.solutions@gmail.com',
    license='Apache 2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy>=1.12.1',
        'Pillow>=4.0.0',
        'pygobject>=3.22.0',
        'protobuf>=3.0.0',
        'edgetpu',
    ],
    scripts = [
        'scripts/kill.sh',
        'scripts/autoboot.sh',
        'scripts/wifi_down.sh',
        'scripts/wifi_up.sh'
    ],
    entry_points = {
        'console_scripts': ['orange_classify=Orange_Vision.classify:main',
                            'orange_classify_server=Orange_Vision.classify_server:main',
                            'orange_detect=Orange_Vision.detect:main',
                            'orange_detect_server=Orange_Vision.detect_server:main'],
    },
    python_requires='>=3.5.3',
)
