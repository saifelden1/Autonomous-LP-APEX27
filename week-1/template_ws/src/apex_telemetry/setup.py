from setuptools import find_packages, setup

package_name = 'apex_telemetry'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name] if False else []),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='APEX Autonomous Systems',
    maintainer_email='apex@team.org',
    description='APEX Autonomous Systems - Week 1 Telemetry & Safety Watchdog',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'telemetry_publisher = apex_telemetry.telemetry_publisher:main',
            'safety_watchdog = apex_telemetry.safety_watchdog:main',
        ],
    },
)
