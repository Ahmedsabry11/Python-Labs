"""
    virtual environment:
            goal:
                - separate each project's required libraries
                - avoid conflicts between projects

            how to use:
                creation:
                    python -m venv .venv

                activation:
                    Linux / Mac:
                        source ./.venv/bin/activate
                    Windows:
                        .\.venv\Scripts\activate

                deactivation:
                    deactivate
    
    packages:
        - use pip → downloads by default from PyPI (Python Package Index)

        # how to install a package:
            pip install {package_name}
            pip install requests

        # how to know the installed packages:
            pip freeze

        # requirements.txt:
            - a text file listing all your installed dependencies
            - helps recreate the same environment
            - command:
                pip freeze > requirements.txt

    Poetry: https://python-poetry.org/
    
    pipenv: https://pipenv.pypa.io/en/latest/   
"""