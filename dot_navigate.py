from dataclasses import dataclass, field


@dataclass
class DotNavigate(object):
    dictionary: dict
    cache: dict = field(default_factory=dict, init=False)

    def get(self, dot_path, default=None):
        if dot_path in self.cache:
            return self.cache[dot_path]

        current_value = self.dictionary
        keys = iter(dot_path.split('.'))

        try:
            for key in keys:
                key = int(key) if key.isdigit() else key
                current_value = current_value[key]

            self.cache[dot_path] = current_value
        except (KeyError, IndexError, TypeError):
            return default

        return current_value
