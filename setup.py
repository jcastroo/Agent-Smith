from setuptools import setup, find_packages

setup(
    name="agent_smith",
    version="1.0.0",
    author="João Castro",
    description="Monitorização de servidores e envio de alertas via Gmail API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jcastroo/Agent-Smith",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.1",
        "google-auth>=2.23.4",
        "google-auth-oauthlib>=0.8.0",
        "google-api-python-client>=2.94.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
        "agent_smith=agentsmith:main",
],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
