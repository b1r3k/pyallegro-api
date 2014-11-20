from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyallegro-api',
      version=version,
      description="Wrapper for Allegro WebAPI on steroids",
      long_description="""\
Wrapper for Allegro WebAPI with additional features out-of-the-box""",
      classifiers=[
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Development Status :: 5 - Production/Stable',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='allegro webapi api SOAP',
      author='Lukasz Jachym',
      author_email='lukasz@cx-lab.com',
      url='https://github.com/b1r3k/pyallegro-api',
      license='MIT',
      package_dir = {'':'src'},
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      test_suite = 'tests',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'suds-jurko==0.4.1.jurko.4'
      ],
      tests_require = [
          'mock'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
