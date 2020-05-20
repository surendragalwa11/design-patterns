import pytest
from patterns.singleton import singleton_one

class TestPatterns:
    def test_singleton(self):
        s = singleton_one.Singleton
        s1 = s.getInstance()
        s2 = s.getInstance()
        assert s1 == s2