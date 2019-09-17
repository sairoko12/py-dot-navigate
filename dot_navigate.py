# -*- coding: utf-8 -*-


class DotNavigate:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get(self, dot_path, default=None, dictionary=None):
        parts_of_path = dot_path.split('.')
        dictionary = self.dictionary if dictionary is None else dictionary

        for index, key in enumerate(parts_of_path):
            if key.isnumeric() and DotNavigate.is_list(dictionary):
                try:
                    if DotNavigate.is_dict(dictionary[int(key)]) \
                            and len(parts_of_path) >= 2:
                        path = ".".join([parts_of_path[part] for part in range(
                            1, len(parts_of_path))])
                        return self.get(path, default, dictionary[int(key)])
                    else:
                        return dictionary[int(key)]
                except IndexError:
                    return default
            elif DotNavigate.is_dict(dictionary) and key in dictionary.keys():
                if DotNavigate.is_dict(dictionary[key]) \
                        or DotNavigate.is_list(dictionary[key]):
                    del parts_of_path[index]
                    if len(parts_of_path) == 0:
                        return dictionary[key]
                    else:
                        return self.get(".".join(parts_of_path),
                                        default, dictionary[key])
                else:
                    return dictionary[key]
            else:
                return default

    @staticmethod
    def is_list(value):
        return isinstance(value, (list))

    @staticmethod
    def is_dict(value):
        return isinstance(value, (dict))
