# NiShangE2ETest
This is the end to end testing repository for the main website of Ni Shang. 

## Set Up
If you don't have python on your machine, visit https://www.python.org/downloads/.

We recommend using venv for your development: https://docs.python.org/3/library/venv.html

After activating your virtual environment, run the following command to install dependencies needed: 

```bash
pip install -r requirements.txt
```

To Update the dependency list:
```bash
pip freeze > requirements.txt
```

If you don't have a chromium browser on your machine, run the following command to install:
```bash
playwright install
```

And, yes, this project uses Playwright with Python: https://playwright.dev/python/