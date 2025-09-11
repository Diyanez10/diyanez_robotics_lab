from setuptools import find_packages, setup

package_name = 'robot_controller_sept_3_dk'

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
    maintainer='admin-7',
    maintainer_email='pp8514@srmist.edu.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "Test_node = robot_controller_sept_3_dk.my_first_node:main"
        ],
    },
)
