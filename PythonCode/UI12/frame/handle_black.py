def handle_black_list(func):
    def wrapper(*args, **kwargs):
        from PythonCode.UI12.frame.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
            # 捕获黑名单中的元素
        except Exception as e:
            # 如果计数器超过最大查找次数，抛出异常；否则更新计数器
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            # 遍历黑名单，在页面上去找有没有这些元素
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单之后，再次查找原来的元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper