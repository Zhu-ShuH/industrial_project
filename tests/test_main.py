"""main 模块单元测试。"""

from src.main import main


def test_main_runs():
    """测试 main 函数能够正常执行。"""
    assert main() is None


def test_main_return_type():
    """测试 main 返回值类型。"""
    result = main()
    assert result is None


def test_main_repeatable():
    """测试 main 可以重复运行。"""
    assert main() == main()
