from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='cashfree_sdk',
      version='0.1.1',
      description='Library to integrate cashfree APIs',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/cashfree/cashfree-sdk-python',
      download_url='https://github.com/cashfree/cashfree-sdk-python/archive/0.1.1.tar.gz',
      author='Cashfree',
      author_email='ankur@cashfree.com',
      license='MIT',
      packages=['cashfree_sdk', 
            'cashfree_sdk.payouts', 
            'cashfree_sdk.payouts.beneficiary',
            'cashfree_sdk.payouts.cashgram',
            'cashfree_sdk.payouts.transfers',
            'cashfree_sdk.payouts.validations',
            'cashfree_sdk.exceptions'],
      install_requires=['requests', 'pem', 'pycrypto'],
      python_requires='>=3.5',
      zip_safe=False)