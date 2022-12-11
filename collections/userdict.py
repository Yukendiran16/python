from collections import UserDict


class LowerDict(dict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})

print(ordinals)

print(isinstance(ordinals, dict))


class LowerDict(UserDict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})

print(ordinals)

print(isinstance(ordinals, dict))


class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        key = str(key).lower()
        self.data[key] = value

    def __getitem__(self, key):
        key = str(key).lower()
        return self.data[key]


custom_dict = CaseInsensitiveDict({'Name': 'Nik', 'Age': 33, 3: 3})
print(custom_dict['name'])


UK_TO_US = {"colour": "color", "flavour": "flavor", "behaviour": "behavior"}


class EnglishSpelledDict(UserDict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        try:
            return super().__getitem__(UK_TO_US[key])
        except KeyError:
            pass
        raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            key = UK_TO_US[key]
        except KeyError:
            pass
        super().__setitem__(key, value)


print(EnglishSpelledDict(UK_TO_US))
