import hashlib


class Patient:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other) -> bool:
        if isinstance(other, Patient):
            return self.name == other.name
        return False

    @property
    def id(self) -> str:
        md5_hash = hashlib.md5()
        md5_hash.update(self.name.encode('utf-8'))
        return md5_hash.hexdigest()
