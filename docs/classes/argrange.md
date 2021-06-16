<!-- ## ArgRange -->

<details>
<summary>
ArgRange
</summary>

Class

*module `argtype`*

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


    def __init__(self, *args):
        # super(ArgRange, self).__init__()
        self.range = range(*args)
        self.info = 'between {} and {}'
        self.args = args



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


    def example(self, n=1):
        values = list(self.range)
        return random.choices(values, k=n)



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
        return self.info.format(*self.args)



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:07:07.525884

<details>
<summary>View source</summary>

```python

class ArgRange:
    """ArgRange"""

    def __init__(self, *args):
        # super(ArgRange, self).__init__()
        self.range = range(*args)
        self.info = 'between {} and {}'
        self.args = args

    def text(self):
        return self.info.format(*self.args)

    def example(self, n=1):
        values = list(self.range)
        return random.choices(values, k=n)


```
</details>

</details>
