<!-- ## ArgType -->

<details>
<summary>
ArgType
</summary>

Class

*module `build-docs`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions
        self.info = '{} {} {}'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>an</code></h2></summary> -->
<summary>
an
</summary>
<!-- ### `an` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def an(self, a):
        return 'an' if a[0] in 'aeiou' else 'a'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>example</code></h2></summary> -->
<summary>
example
</summary>
<!-- ### `example` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def example(self, *args, **kwargs):
        return self.conditions[0].example(*args, **kwargs)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>text</code></h2></summary> -->
<summary>
text
</summary>
<!-- ### `text` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def text(self):
        condition_string = ', '.join(c.text() for c in self.conditions)
        p = self.primitive.__name__
        return self.info.format(self.an(p), p, condition_string)



```

</details>

#### References

- [ArgType.an](#an)

</details>


Docs built at 2021-06-16 05:07:07.532840

<details>
<summary>View source</summary>

```python

class ArgType:
    """
    Defines a 'type' that can be used for validating and/or converting function arguments, generating examples, type hinting, etc. It is intended to emulate some of the features of Python's `typing` module, albeit with a more general scope.
    """

    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions
        self.info = '{} {} {}'

    def an(self, a):
        return 'an' if a[0] in 'aeiou' else 'a'

    def text(self):
        condition_string = ', '.join(c.text() for c in self.conditions)
        p = self.primitive.__name__
        return self.info.format(self.an(p), p, condition_string)

    def example(self, *args, **kwargs):
        return self.conditions[0].example(*args, **kwargs)


```
</details>

</details>
