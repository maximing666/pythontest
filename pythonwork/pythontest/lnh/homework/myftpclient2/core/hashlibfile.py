import hashlib

class hashlibfile:
    """
    加盐验证文件的md5值
    """
    def __init__(self, file):
        self.file = r'' + file

    def hash(self):
        md5 = hashlib.md5(bytes('MyFtp', encoding='utf-8'))
        with open(self.file, mode='rb') as f:
            md5.update(f.read())
        return md5.hexdigest()
