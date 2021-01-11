def singleton(func):
    """
    单例模式
    :param func:
    :return:
    """
    _instance = {}

    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)
        return _instance[func]

    return wrapper