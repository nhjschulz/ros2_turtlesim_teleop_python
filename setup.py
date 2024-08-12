from setuptools import find_packages, setup

package_name = 'ros2_turtlesim_teleop_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='norbert',
    maintainer_email='github@schulznorbert.de',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pythonop_turtle = ros2_turtlesim_teleop_python.pythonop_turtle:main'
        ],
    },
)
