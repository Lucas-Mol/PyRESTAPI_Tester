# PyRESTAPI_Tester
## Intro
PyRESTAPI_Tester is a simple project to test that all endpoints of all services you have access to and must control are online and responding 'OK'.

It's using Python as script language and reading a JSON containing the list of all wished endpoints.
## Overview
![Testing...](https://github.com/Lucas-Mol/PyRESTAPI_Tester/assets/93149981/0bff9dcb-9846-4a03-8bab-8e5353e5ba42)

**Description:** The test running successfully <br/><br/>

![JSON example](https://github.com/Lucas-Mol/PyRESTAPI_Tester/assets/93149981/2a2a6687-8453-4fe9-aae6-34ac147af545)

**Description:** The JSON file with example of templates (Explication on <a href='README.md#how-to-run-it'>'How to run it?'<a/>) <br/><br/>

## How to run it?
It must be installed:
- Python 3 +

Libs used:
- Requests
- PyTest

So, if you don't have them installed yet, just run: `pip install requests` and `pip install pytest`


Write the wished endpoints on <a href='endpoints.json'>endpoints.json<a/> file:
_(It's already filled with some templates that can be used)_
   - If endpoint has no auth: just write the url
   - If endpoint has login auth: write the url, username and password
   - If endpoint has JWT token auth: write the url and jwtoken

**Note:** You can add any endpoint as you want

**And finally**, run command: `pytest -v` on project's directory

## Tech Stack

- Python 3
- Request lib
- PyTest lib
