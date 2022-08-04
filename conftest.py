import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        a = os.path.abspath(__file__)
        b = os.path.dirname(a)
        config_file = os.path.join(b, request.config.getoption("--target"))
        with open(config_file) as h:
            target = json.load(h)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
