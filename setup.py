from setuptools import find_packages, setup
<<<<<<< HEAD

package_name = 'sun_drawer_4'
=======
from glob import glob
import os

package_name = 'ros2_py_template'
>>>>>>> 605dc6b60db023bf22ae5e3a7a90baf78b7b9c93

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
<<<<<<< HEAD
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajr',
    maintainer_email='martinordasfarkas2004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
entry_points={
    'console_scripts': [
        'draw_sun_3 = sun_drawer_4.draw_sun_4:main',
    ],
},

=======
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='todo@todo.com',
    description='TODO: Package description',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'control_vehicle = ros2_py_template.control_vehicle:main',
        ],
    },
>>>>>>> 605dc6b60db023bf22ae5e3a7a90baf78b7b9c93
)
