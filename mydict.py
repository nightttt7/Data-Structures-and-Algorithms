# 生成dict的实例Dict,增加属性访问和设置


class Dict(dict):

    # super,增加而非修改
    def __init__(self, **kw):
        super().__init__(**kw)

    # 获取属性
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    # 设置属性
    def __setattr__(self, key, value):
        self[key] = value
