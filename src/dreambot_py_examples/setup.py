from setuptools import find_packages, setup

package_name = 'dreambot_py_examples'

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
    maintainer='praful_pawar',
    maintainer_email='praful_pawar@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_parameter = dreambot_py_examples.dreambot_py_examples.simple_parameter:main',
            'simple_service = dreambot_py_examples.dreambot_py_examples.simple_service:main',
            'simple_action = dreambot_py_examples.dreambot_py_examples.simple_action:main',
            'simple_publisher = dreambot_py_examples.dreambot_py_examples.simple_publisher:main',
            'simple_subscriber = dreambot_py_examples.dreambot_py_examples.simple_subscriber:main',
            'simple_client = dreambot_py_examples.dreambot_py_examples.simple_client:main',
        ],
    },
)
