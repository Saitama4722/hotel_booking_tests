import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://restful-booker.herokuapp.com"
    )

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--api-url")
