import setuptools

setuptools.setup(
    name="streamlit-reveal-slides",
    version="0.0.1",
    author="",
    author_email="",
    description="reveal.js HTML presentations for streamlit",
    long_description="create and add reveal.js HTML presentations to your streamlit app",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
