import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="http://test.com",
    )

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--api-url")