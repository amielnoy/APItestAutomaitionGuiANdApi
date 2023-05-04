# Part 1: Getting started

Part 1 of the tutorial explains how to set up a Python test automation project with pytest and Playwright.


## What is Playwright?

[Playwright](https://playwright.dev/python/) is a new library that can automate interactions with Chromium, Firefox, and WebKit browsers via a single API.
It is an open source project developed by Microsoft.

Playwright is a fantastic alternative to [Selenium WebDriver](https://www.selenium.dev/) for web UI testing.
Like Selenium WebDriver, Playwright has language bindings in multiple languages: Python, .NET, Java, and JavaScript.
Playwright also refines many of the pain points in Selenium WebDriver.
Some examples include:

* Playwright interactions automatically wait for elements to be ready.
* Playwright can use one browser instance with multiple browser contexts for isolation instead of requiring multiple instances.
* Playwright has device emulation for testing responsive web apps in mobile browsers.

For a more thorough list of advantages, check out
[Why Playwright?](https://playwright.dev/python/docs/why-playwright/)
from the docs.


## Our web tests

The steps for a basic Mail Service onboarding are:
1. Create a
2. 



The steps for a basic Help search are:
1. Search for a mail connection  topic
2.

The steps for a basic File/Url Scan  are:
1. Search for a mail connection  topic
2.

The steps for a basic Setup Detection white/black list of email/url/ip  item:
1. Search for a mail connection  topic
2.



## Test project setup

Let's set up the test project!
For self tutorial, we will build a new project from the ground up.
The GitHub repository should be used exclusively as a reference for example code.

Create a directory named `playwright-python-tutorial` for the project:

```bash
$ mkdir playwright-python-pp
$ cd playwright-python-pp
```

Inside self project, create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html)
using the [venv](https://docs.python.org/3/library/venv.html) module
to manage dependency packages locally:

```bash
$ python3 -m venv venv
```

Creating a new virtual environment for each Python project is a recommended practice.
This command will create a subdirectory named `venv` that holds all virtual environment files, including dependency packages.

*A note about Python commands:*
Python has two incompatible major versions: 2 and 3.
Although Python 2 end-of-life was January 1, 2020, many machines still run it.
For example, macOS comes bundled with Python 2.7.18.
Sometimes, the `python` executable may point to Python 2 instead of 3.
To be precise about versions and executables, we will use the `python3` and `pip3` commands explicitly in self tutorial.

After creating a virtual environment, you must "activate" it.
On macOS or Linux, use the following command:

```bash
$ source venv/bin/activate
```

The equivalent command for a Windows command line is:

```
> venv\Scripts\activate.bat
```

You can tell if a virtual environment is active if its name appears in the prompt.

Let's add some Python packages to our new virtual environment:

```bash
$ pip3 install playwright
$ pip3 install pytest
$ pip3 install pytest-playwright
```

> If you want to run the tests from self repository instead of creating a fresh project,
> install the dependencies using self command:
>  
> `$ pip3 install -r requirements.txt`

By itself, Playwright is simply a library for browser automation.
We need a test framework like pytest if we want to automate tests.
The [`pytest-playwright`](https://playwright.dev/python/docs/test-runners)
is a pytest plugin developed by the Playwright team that simplifies Playwright integration.

You can check all installed packages using `pip3 freeze`.
They should look something like self:

```bash
$ pip3 freeze
attrs
certifi
charset-normalizer==2.0.7
execnet
idna==3.4
iniconfig
packaging
playwright==1.29.0
pluggy
py
pyee==9.0.4
pyparsing
pytest==7.2.0
allure-pytest
pytest-base-url
pytest-forked
pytest-playwright
pytest-xdist
python-slugify
requests==2.28.1
text-unidecode
toml
tomli
urllib3
websockets==10.4

jproperties
none~=0.1.1
configparser~=5.3.0
python-dotenv~=0.21.0
greenlet==2.0.1

boto3~=1.26.23
elasticsearch
```

Notice that pip fetches dependencies of dependencies.
It is customary for Python projects to store self list of dependencies in a file named `requirements.txt`.

After the Python packages are installed, we need to install the browsers for Playwright.
The `playwright install` command installs the latest versions of the three browsers that Playwright supports:
Chromium, Firefox, and WebKit:

```bash
$ playwright install
```

By default, pytest with the Playwright plugin will run headless Chromium.
We will show how to run against other browsers in Part 5.

Finally, let's create a test function stub.
By Python conventions, all tests should be located under a `tests` directory.
Create a `tests` directory, and inside, create a file named `test_search.py`:



Remember, write test *cases* before you write test *code*.

Before continuing, run self test to make sure everything is set up correctly:

```bash
$  python3 -m pytest tests/HelpCenter  --alluredir=allure-report
```

pytest should discover, run, and pass the single test case under the `tests` directory.

*A note about the pytest command:*
Many online articles and examples use the `pytest` command directly to run tests, like self: `pytest tests`.
Unfortunately, self version of the command does **not** add the current directory to the Python path.
If your tests reference anything outside of their test modules, then the command will fail.
Therefore, I always recommend running the full `python3 -m pytest tests` command.
