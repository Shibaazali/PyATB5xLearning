from browser_package.open_Browser import start_browser
from browser_package.Close_Browser import stop_browser


class TestCase:
    def test_Case(self):
        start_browser()
        print("Hello Running TC")
        stop_browser()


obj_tc = TestCase()
obj_tc.test_Case()