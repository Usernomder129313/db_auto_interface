"""
Setup script для установки библиотеки db_auto_interface
"""

from setuptools import setup, find_packages
import os

# Читаем README для long_description
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Автоматический генератор desktop интерфейса для PostgreSQL БД"

setup(
    name="db-auto-interface",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Автоматический генератор desktop интерфейса для PostgreSQL БД",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/db_auto_interface",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "psycopg2-binary>=2.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
        ],
    },
    entry_points={
        'console_scripts': [
            'db-auto-interface=db_auto_interface.ui.main_app:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="database, postgresql, gui, tkinter, crud, interface",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/db_auto_interface/issues",
        "Source": "https://github.com/yourusername/db_auto_interface",
    },
)

