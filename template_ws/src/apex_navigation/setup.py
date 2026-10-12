import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'apex_navigation'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name] if False else []),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='APEX Autonomous Systems',
    maintainer_email='apex@team.org',
    description='APEX Autonomous Systems - Pure Pursuit Capstone Navigation',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_publisher = apex_navigation.path_publisher:main',
            'pure_pursuit_controller = apex_navigation.pure_pursuit_controller:main',
        ],
    },
)
