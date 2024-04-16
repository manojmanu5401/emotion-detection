1. Clone the repo & open it in VS code
2. Create a virtual environment in your project directory (Python version greater than 3.10 should be fine)
    1. python -m venv env
3. Activate the virtual env
    1. On Linux, Unix or MacOS, using the terminal or bash shell:
        source /path/to/env/bin/activate
        e.g. source env/bin/activate

    2. On Unix or MacOS, using the csh shell:
        source /path/to/env/bin/activate.csh
    
    3. On Unix or MacOS, using the fish shell:
        source /path/to/env/bin/activate.fish

    4. On Windows using the Command Prompt:
        path\to\env\Scripts\activate.bat

    5. On Windows using PowerShell:
        path\to\env\Scripts\Activate.ps1

4. install the packages in the requirements.txt
    1. pip install -r /path/to/requirements.txt

5. Run the application
    1. python app.py