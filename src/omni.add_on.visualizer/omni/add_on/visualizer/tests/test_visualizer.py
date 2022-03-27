import omni.kit.test

class TestExtension(omni.kit.test.AsyncTestCaseFailOnLogError):
    async def setUp(self) -> None:
        pass

    async def tearDown(self) -> None:
        pass

    async def test_extension(self):
        pass