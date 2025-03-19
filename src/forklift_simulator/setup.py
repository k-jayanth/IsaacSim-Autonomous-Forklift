import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'forklift_simulator'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join("share", package_name, "launch/"), glob("./launch/*")),
        (os.path.join("share", package_name, "meshes/"), glob("./meshes/**/*")), 
       (os.path.join("share", package_name, "meshes/materials/"), glob("./meshes/materials/*")),
        (os.path.join("share", package_name, "urdf/"), glob("./urdf/*")),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Minho Lee',
    maintainer_email='mino@inha.edu',
    maintainer='Jayanth Kandregula',
    maintainer_email='jayanthkandregula@gmail.com',
    description='The autonomous forklift simulation package',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
