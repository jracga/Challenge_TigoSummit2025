from mocks.manager import load_mocks

def match_mock(path, method, params):
    mocks = load_mocks()
    for mock in mocks:
        if mock["path"] == path and mock["method"].upper() == method:
            expected_params = mock.get("params", {})
            if all(params.get(k) == v for k, v in expected_params.items()):
                return mock
    return None
