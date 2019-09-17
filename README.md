## Dot navigate


### Description

On complex dictionaries is very hard to get any value, so this library can help to this, but how? Easy with dot navigatation on list and dictionaries keys.


#### Important: This library only works on python 3


Some examples:

```python
from dot_navigate import DotNavigate

# Get value of foo key
fancy_dict = {
    'bar': {
        'baz': {
            'foo': "Fancy Value"
        }
    }
}

navigate = DotNavigate(fancy_dict)
foo_value = navigate.get('bar.baz.foo')
print(foo_value)

# Get value from list and dictionary
fancy_list = ['some', 'value', {
    'foo': [1,2,3]
}]

navigate = DotNavigate(fancy_list)
foo_value = navigate.get('2.foo.0')

print(foo_value)
```

See examples with more complexity on example.py file

<div align="center">
Made with ❤️ by [Sairoko](https://cbenavides.mx)
</div>
