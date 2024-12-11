from browser_package.open_Browser import start_browser
from browser_package.Close_Browser import stop_browser

def test_Case():
    start_browser()
    print("Hello Running TC")
    stop_browser()

test_Case()