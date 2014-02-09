from setuptools import setup, find_packages
import image_ui

setup(name='twentytab-image-ui',
      version=image_ui.__version__,
      description='A django app that implements an admin to have thumbnails with colorbox.js',
      author='20tab S.r.l.',
      author_email='info@20tab.com',
      url='https://github.com/20tab/twentytab-image-ui',
      license='MIT License',
      install_requires=[
          'Django >=1.6',
          'Pillow >=2.3',
          'django-appconf >=0.6',
          'django_imagekit >=3',
      ],
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
      }
)
