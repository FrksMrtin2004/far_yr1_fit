from setuptools import find_packages, setup

package_name = 'sun_drawer_5'

setup(
    name='sun_drawer_5',
    version='0.0.1',
    packages=['sun_drawer_5'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajr',
    maintainer_email='martinordasfarkas2004@gmail.com',
    description='Egy csomag, amely a "turtle" könyvtár segítségével rajzolja meg a napot',
    license='MIT',  # Cseréld ki a megfelelő licencre
    extras_require={  # `tests_require` helyett `extras_require` használata
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'draw_sun_4 = sun_drawer_5.draw_sun_4:main',
        ],
    },
)
