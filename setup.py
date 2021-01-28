import setuptools
import os

print('OS=',os.name);

if (os.name == 'nt'):
  print('In Windows');
  with open("README.md", "r") as fh:
     long_description = fh.read()

else:
  print('In UNIX');
  with open("README.md", "r") as fh:
     long_description = fh.read()


    
setuptools.setup(
    name="bisImgSegPkg",
    version="0.5.0",
    author="BioImageSuite Web Team (An Qu)",
    author_email="xenophon.papademetris@yale.edu",
    description="A 3D Medical Image Segmentation Package Using MONAI",
    long_description=long_description,
    license="License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    long_description_content_type="text/markdown",
    url="https://github.com/bioimagesuiteweb/imagesegm",
    packages=setuptools.find_packages(),
    install_requires= [
      'nibabel',
      'numpy',
      'monai',
      'torch',
      'pytorch-lightning',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['bisImgSeg=bisImgSeg.imageSegmentation:main']
    },
    python_requires='>=3.6',
)
