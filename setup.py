import setuptools

setuptools.setup(
    name="kvm_switcher",
    version="0.0.1",
    author="Kristian Nymann Jakobsen",
    author_email="kristian@nymann.dev",
    description="Hibernates inactive monitor, and wakes up active one post kvm-switch button toggle.",
    url="https://github.com/nymann/kvm-switcher",
    packages=setuptools.find_packages(),
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "sentry_sdk"
    ],
    extras_require={
        'lint': [
            "pylint",
            "coverage"
        ]
    },
    entry_points={
        'console_scripts': [
            'kvm_switch=kvm_switcher.console_scripts.__main__:main',
        ]
    },
)
