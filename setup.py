from setuptools import setup, find_packages

setup(
    name="Predictive Demand Forecasting",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib==3.4.0",
        "scikit-learn==0.24.1",
        "pandas==1.2.1",
        "numpy==1.20.1",
        "tensorflow==2.5.0",
        "keras==2.4.3",
        # Add any additional dependencies here
    ],
    entry_points={
        "console_scripts": [
            "your_script_name = your_package_name.your_module_name:main",
        ],
    },
    author="Vivek Vala",
    author_email="valavivek2019@gmail.com",
    description="Develop AI models for precise inventory predictions based on historical data, optimizing warehouse distribution to meet dynamic demand across different regions and time periods.",
    url="https://github.com/valavivekkumarj/Datatrone",
)
