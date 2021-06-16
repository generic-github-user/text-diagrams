<!-- ## Path -->

<details>
<summary>
Path
</summary>

Class

*module `build-docs`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__bytes__</code></h2></summary> -->
<summary>
__bytes__
</summary>
<!-- ### `__bytes__` -->
Method

Return the bytes representation of the path.  This is only


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __bytes__(self):
        """Return the bytes representation of the path.  This is only
        recommended to use under Unix."""
        return os.fsencode(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__enter__</code></h2></summary> -->
<summary>
__enter__
</summary>
<!-- ### `__enter__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __enter__(self):
        return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__eq__</code></h2></summary> -->
<summary>
__eq__
</summary>
<!-- ### `__eq__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __eq__(self, other):
        if not isinstance(other, PurePath):
            return NotImplemented
        return self._cparts == other._cparts and self._flavour is other._flavour



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__exit__</code></h2></summary> -->
<summary>
__exit__
</summary>
<!-- ### `__exit__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __exit__(self, t, v, tb):
        # https://bugs.python.org/issue39682
        # In previous versions of pathlib, this method marked this path as
        # closed; subsequent attempts to perform I/O would raise an IOError.
        # This functionality was never documented, and had the effect of
        # making Path objects mutable, contrary to PEP 428. In Python 3.9 the
        # _closed attribute was removed, and this method made a no-op.
        # This method and __enter__()/__exit__() should be deprecated and
        # removed in the future.
        pass



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__fspath__</code></h2></summary> -->
<summary>
__fspath__
</summary>
<!-- ### `__fspath__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __fspath__(self):
        return str(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__ge__</code></h2></summary> -->
<summary>
__ge__
</summary>
<!-- ### `__ge__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __ge__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts >= other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__gt__</code></h2></summary> -->
<summary>
__gt__
</summary>
<!-- ### `__gt__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __gt__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts > other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__hash__</code></h2></summary> -->
<summary>
__hash__
</summary>
<!-- ### `__hash__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __hash__(self):
        try:
            return self._hash
        except AttributeError:
            self._hash = hash(tuple(self._cparts))
            return self._hash



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__le__</code></h2></summary> -->
<summary>
__le__
</summary>
<!-- ### `__le__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __le__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts <= other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__lt__</code></h2></summary> -->
<summary>
__lt__
</summary>
<!-- ### `__lt__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __lt__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts < other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__new__</code></h2></summary> -->
<summary>
__new__
</summary>
<!-- ### `__new__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath
        self = cls._from_parts(args, init=False)
        if not self._flavour.is_supported:
            raise NotImplementedError("cannot instantiate %r on your system"
                                      % (cls.__name__,))
        self._init()
        return self



```

</details>

#### References

- [Path._init](#_init)

</details>


<details>
<!-- <summary><h2><code>__reduce__</code></h2></summary> -->
<summary>
__reduce__
</summary>
<!-- ### `__reduce__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __reduce__(self):
        # Using the parts tuple helps share interned path parts
        # when pickling related paths.
        return (self.__class__, tuple(self._parts))



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__repr__</code></h2></summary> -->
<summary>
__repr__
</summary>
<!-- ### `__repr__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.as_posix())



```

</details>

#### References

- [Path.as_posix](#as_posix)

</details>


<details>
<!-- <summary><h2><code>__rtruediv__</code></h2></summary> -->
<summary>
__rtruediv__
</summary>
<!-- ### `__rtruediv__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __rtruediv__(self, key):
        try:
            return self._from_parts([key] + self._parts)
        except TypeError:
            return NotImplemented



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__str__</code></h2></summary> -->
<summary>
__str__
</summary>
<!-- ### `__str__` -->
Method

Return the string representation of the path, suitable for


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __str__(self):
        """Return the string representation of the path, suitable for
        passing to system calls."""
        try:
            return self._str
        except AttributeError:
            self._str = self._format_parsed_parts(self._drv, self._root,
                                                  self._parts) or '.'
            return self._str



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__truediv__</code></h2></summary> -->
<summary>
__truediv__
</summary>
<!-- ### `__truediv__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __truediv__(self, key):
        try:
            return self._make_child((key,))
        except TypeError:
            return NotImplemented



```

</details>

#### References

- [Path._make_child](#_make_child)

</details>


<details>
<!-- <summary><h2><code>_init</code></h2></summary> -->
<summary>
_init
</summary>
<!-- ### `_init` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _init(self,
              # Private non-constructor arguments
              template=None,
              ):
        if template is not None:
            self._accessor = template._accessor
        else:
            self._accessor = _normal_accessor



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_make_child</code></h2></summary> -->
<summary>
_make_child
</summary>
<!-- ### `_make_child` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _make_child(self, args):
        drv, root, parts = self._parse_args(args)
        drv, root, parts = self._flavour.join_parsed_parts(
            self._drv, self._root, self._parts, drv, root, parts)
        return self._from_parsed_parts(drv, root, parts)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_make_child_relpath</code></h2></summary> -->
<summary>
_make_child_relpath
</summary>
<!-- ### `_make_child_relpath` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _make_child_relpath(self, part):
        # This is an optimization used for dir walking.  `part` must be
        # a single part relative to this path.
        parts = self._parts + [part]
        return self._from_parsed_parts(self._drv, self._root, parts)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_opener</code></h2></summary> -->
<summary>
_opener
</summary>
<!-- ### `_opener` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _opener(self, name, flags, mode=0o666):
        # A stub for the opener argument to built-in open()
        return self._accessor.open(self, flags, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_raw_open</code></h2></summary> -->
<summary>
_raw_open
</summary>
<!-- ### `_raw_open` -->
Method

as os.open() does.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _raw_open(self, flags, mode=0o777):
        """
        Open the file pointed by this path and return a file descriptor,
        as os.open() does.
        """
        return self._accessor.open(self, flags, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>absolute</code></h2></summary> -->
<summary>
absolute
</summary>
<!-- ### `absolute` -->
Method

Return an absolute version of this path.  This function works


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def absolute(self):
        """Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        """
        # XXX untested yet!
        if self.is_absolute():
            return self
        # FIXME this must defer to the specific flavour (and, under Windows,
        # use nt._getfullpathname())
        obj = self._from_parts([os.getcwd()] + self._parts, init=False)
        obj._init(template=self)
        return obj



```

</details>

#### References

- [Path.is_absolute](#is_absolute)

</details>


<details>
<!-- <summary><h2><code>as_posix</code></h2></summary> -->
<summary>
as_posix
</summary>
<!-- ### `as_posix` -->
Method

Return the string representation of the path with forward (/)


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def as_posix(self):
        """Return the string representation of the path with forward (/)
        slashes."""
        f = self._flavour
        return str(self).replace(f.sep, '/')



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>as_uri</code></h2></summary> -->
<summary>
as_uri
</summary>
<!-- ### `as_uri` -->
Method

Return the path as a 'file' URI.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def as_uri(self):
        """Return the path as a 'file' URI."""
        if not self.is_absolute():
            raise ValueError("relative path can't be expressed as a file URI")
        return self._flavour.make_uri(self)



```

</details>

#### References

- [Path.is_absolute](#is_absolute)

</details>


<details>
<!-- <summary><h2><code>chmod</code></h2></summary> -->
<summary>
chmod
</summary>
<!-- ### `chmod` -->
Method

Change the permissions of the path, like os.chmod().


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def chmod(self, mode):
        """
        Change the permissions of the path, like os.chmod().
        """
        self._accessor.chmod(self, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>exists</code></h2></summary> -->
<summary>
exists
</summary>
<!-- ### `exists` -->
Method

Whether this path exists.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def exists(self):
        """
        Whether this path exists.
        """
        try:
            self.stat()
        except OSError as e:
            if not _ignore_error(e):
                raise
            return False
        except ValueError:
            # Non-encodable path
            return False
        return True



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>expanduser</code></h2></summary> -->
<summary>
expanduser
</summary>
<!-- ### `expanduser` -->
Method

Return a new path with expanded ~ and ~user constructs


#### Parameters

##### `(as returned by os.path.expanduser)`





##### ``



- kind, including directories) matching the given relative pattern.

- 

- a drive).

- 

- by the system, if any.

- result for the special paths '.' and '..'.

- 

- new path representing either a subpath (if all arguments are relative

- paths) or a totally different path (if one of the arguments is

- anchored).

- 

- arguments.  If the operation is not possible (because this is not

- a subpath of the other path), raise ValueError.

- 

- directories) matching the given relative pattern, anywhere in

- this subtree.

- 

- (as returned by os.path.samefile()).

- 

- has no suffix, add given suffix.  If the given suffix is an empty

- string, remove the suffix from the path.

- 



#### Source

<details>
<summary>View source</summary>

```python


    def expanduser(self):
        """ Return a new path with expanded ~ and ~user constructs
        (as returned by os.path.expanduser)
        """
        if (not (self._drv or self._root) and
            self._parts and self._parts[0][:1] == '~'):
            homedir = self._flavour.gethomedir(self._parts[0][1:])
            return self._from_parts([homedir] + self._parts[1:])

        return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>glob</code></h2></summary> -->
<summary>
glob
</summary>
<!-- ### `glob` -->
Method

Iterate over this subtree and yield all existing files (of any


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def glob(self, pattern):
        """Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        """
        sys.audit("pathlib.Path.glob", self, pattern)
        if not pattern:
            raise ValueError("Unacceptable pattern: {!r}".format(pattern))
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p



```

</details>

#### References

- [Path.glob](#glob)

</details>


<details>
<!-- <summary><h2><code>group</code></h2></summary> -->
<summary>
group
</summary>
<!-- ### `group` -->
Method

Return the group name of the file gid.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def group(self):
        """
        Return the group name of the file gid.
        """
        return self._accessor.group(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>is_absolute</code></h2></summary> -->
<summary>
is_absolute
</summary>
<!-- ### `is_absolute` -->
Method

True if the path is absolute (has both a root and, if applicable,


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_absolute(self):
        """True if the path is absolute (has both a root and, if applicable,
        a drive)."""
        if not self._root:
            return False
        return not self._flavour.has_drv or bool(self._drv)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>is_block_device</code></h2></summary> -->
<summary>
is_block_device
</summary>
<!-- ### `is_block_device` -->
Method

Whether this path is a block device.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_block_device(self):
        """
        Whether this path is a block device.
        """
        try:
            return S_ISBLK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_char_device</code></h2></summary> -->
<summary>
is_char_device
</summary>
<!-- ### `is_char_device` -->
Method

Whether this path is a character device.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_char_device(self):
        """
        Whether this path is a character device.
        """
        try:
            return S_ISCHR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_dir</code></h2></summary> -->
<summary>
is_dir
</summary>
<!-- ### `is_dir` -->
Method

Whether this path is a directory.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_dir(self):
        """
        Whether this path is a directory.
        """
        try:
            return S_ISDIR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_fifo</code></h2></summary> -->
<summary>
is_fifo
</summary>
<!-- ### `is_fifo` -->
Method

Whether this path is a FIFO.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_fifo(self):
        """
        Whether this path is a FIFO.
        """
        try:
            return S_ISFIFO(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_file</code></h2></summary> -->
<summary>
is_file
</summary>
<!-- ### `is_file` -->
Method

to regular files).


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_file(self):
        """
        Whether this path is a regular file (also True for symlinks pointing
        to regular files).
        """
        try:
            return S_ISREG(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_mount</code></h2></summary> -->
<summary>
is_mount
</summary>
<!-- ### `is_mount` -->
Method

Check if this path is a POSIX mount point


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_mount(self):
        """
        Check if this path is a POSIX mount point
        """
        # Need to exist and be a dir
        if not self.exists() or not self.is_dir():
            return False

        try:
            parent_dev = self.parent.stat().st_dev
        except OSError:
            return False

        dev = self.stat().st_dev
        if dev != parent_dev:
            return True
        ino = self.stat().st_ino
        parent_ino = self.parent.stat().st_ino
        return ino == parent_ino



```

</details>

#### References

- [Path.exists](#exists)
- [Path.is_dir](#is_dir)
- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_relative_to</code></h2></summary> -->
<summary>
is_relative_to
</summary>
<!-- ### `is_relative_to` -->
Method

Return True if the path is relative to another path or False.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_relative_to(self, *other):
        """Return True if the path is relative to another path or False.
        """
        try:
            self.relative_to(*other)
            return True
        except ValueError:
            return False



```

</details>

#### References

- [Path.relative_to](#relative_to)

</details>


<details>
<!-- <summary><h2><code>is_reserved</code></h2></summary> -->
<summary>
is_reserved
</summary>
<!-- ### `is_reserved` -->
Method

Return True if the path contains one of the special names reserved


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_reserved(self):
        """Return True if the path contains one of the special names reserved
        by the system, if any."""
        return self._flavour.is_reserved(self._parts)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>is_socket</code></h2></summary> -->
<summary>
is_socket
</summary>
<!-- ### `is_socket` -->
Method

Whether this path is a socket.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_socket(self):
        """
        Whether this path is a socket.
        """
        try:
            return S_ISSOCK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_symlink</code></h2></summary> -->
<summary>
is_symlink
</summary>
<!-- ### `is_symlink` -->
Method

Whether this path is a symbolic link.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_symlink(self):
        """
        Whether this path is a symbolic link.
        """
        try:
            return S_ISLNK(self.lstat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.lstat](#lstat)

</details>


<details>
<!-- <summary><h2><code>iterdir</code></h2></summary> -->
<summary>
iterdir
</summary>
<!-- ### `iterdir` -->
Method

Iterate over the files in this directory.  Does not yield any


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def iterdir(self):
        """Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        """
        for name in self._accessor.listdir(self):
            if name in {'.', '..'}:
                # Yielding a path object for these makes little sense
                continue
            yield self._make_child_relpath(name)



```

</details>

#### References

- [Path._make_child](#_make_child)
- [Path._make_child_relpath](#_make_child_relpath)

</details>


<details>
<!-- <summary><h2><code>joinpath</code></h2></summary> -->
<summary>
joinpath
</summary>
<!-- ### `joinpath` -->
Method

Combine this path with one or several arguments, and return a


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def joinpath(self, *args):
        """Combine this path with one or several arguments, and return a
        new path representing either a subpath (if all arguments are relative
        paths) or a totally different path (if one of the arguments is
        anchored).
        """
        return self._make_child(args)



```

</details>

#### References

- [Path._make_child](#_make_child)

</details>


<details>
<!-- <summary><h2><code>lchmod</code></h2></summary> -->
<summary>
lchmod
</summary>
<!-- ### `lchmod` -->
Method

permissions are changed, rather than its target's.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def lchmod(self, mode):
        """
        Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
        """
        self._accessor.lchmod(self, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>link_to</code></h2></summary> -->
<summary>
link_to
</summary>
<!-- ### `link_to` -->
Method

Create a hard link pointing to a path named target.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def link_to(self, target):
        """
        Create a hard link pointing to a path named target.
        """
        self._accessor.link_to(self, target)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>lstat</code></h2></summary> -->
<summary>
lstat
</summary>
<!-- ### `lstat` -->
Method

status information is returned, rather than its target's.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def lstat(self):
        """
        Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
        """
        return self._accessor.lstat(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>match</code></h2></summary> -->
<summary>
match
</summary>
<!-- ### `match` -->
Method

Return True if this path matches the given pattern.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def match(self, path_pattern):
        """
        Return True if this path matches the given pattern.
        """
        cf = self._flavour.casefold
        path_pattern = cf(path_pattern)
        drv, root, pat_parts = self._flavour.parse_parts((path_pattern,))
        if not pat_parts:
            raise ValueError("empty pattern")
        if drv and drv != cf(self._drv):
            return False
        if root and root != cf(self._root):
            return False
        parts = self._cparts
        if drv or root:
            if len(pat_parts) != len(parts):
                return False
            pat_parts = pat_parts[1:]
        elif len(pat_parts) > len(parts):
            return False
        for part, pat in zip(reversed(parts), reversed(pat_parts)):
            if not fnmatch.fnmatchcase(part, pat):
                return False
        return True



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>mkdir</code></h2></summary> -->
<summary>
mkdir
</summary>
<!-- ### `mkdir` -->
Method

Create a new directory at this given path.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
            self._accessor.mkdir(self, mode)
        except FileNotFoundError:
            if not parents or self.parent == self:
                raise
            self.parent.mkdir(parents=True, exist_ok=True)
            self.mkdir(mode, parents=False, exist_ok=exist_ok)
        except OSError:
            # Cannot rely on checking for EEXIST, since the operating system
            # could give priority to other errors like EACCES or EROFS
            if not exist_ok or not self.is_dir():
                raise



```

</details>

#### References

- [Path.is_dir](#is_dir)
- [Path.mkdir](#mkdir)

</details>


<details>
<!-- <summary><h2><code>open</code></h2></summary> -->
<summary>
open
</summary>
<!-- ### `open` -->
Method

the built-in open() function does.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def open(self, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None):
        """
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        """
        return io.open(self, mode, buffering, encoding, errors, newline,
                       opener=self._opener)



```

</details>

#### References

- [Path._opener](#_opener)

</details>


<details>
<!-- <summary><h2><code>owner</code></h2></summary> -->
<summary>
owner
</summary>
<!-- ### `owner` -->
Method

Return the login name of the file owner.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def owner(self):
        """
        Return the login name of the file owner.
        """
        return self._accessor.owner(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>read_bytes</code></h2></summary> -->
<summary>
read_bytes
</summary>
<!-- ### `read_bytes` -->
Method

Open the file in bytes mode, read it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def read_bytes(self):
        """
        Open the file in bytes mode, read it, and close the file.
        """
        with self.open(mode='rb') as f:
            return f.read()



```

</details>

#### References

- [Path.open](#open)

</details>


<details>
<!-- <summary><h2><code>read_text</code></h2></summary> -->
<summary>
read_text
</summary>
<!-- ### `read_text` -->
Method

Open the file in text mode, read it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def read_text(self, encoding=None, errors=None):
        """
        Open the file in text mode, read it, and close the file.
        """
        with self.open(mode='r', encoding=encoding, errors=errors) as f:
            return f.read()



```

</details>

#### References

- [Path.open](#open)

</details>


<details>
<!-- <summary><h2><code>readlink</code></h2></summary> -->
<summary>
readlink
</summary>
<!-- ### `readlink` -->
Method

Return the path to which the symbolic link points.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def readlink(self):
        """
        Return the path to which the symbolic link points.
        """
        path = self._accessor.readlink(self)
        obj = self._from_parts((path,), init=False)
        obj._init(template=self)
        return obj



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>relative_to</code></h2></summary> -->
<summary>
relative_to
</summary>
<!-- ### `relative_to` -->
Method

Return the relative path to another path identified by the passed


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def relative_to(self, *other):
        """Return the relative path to another path identified by the passed
        arguments.  If the operation is not possible (because this is not
        a subpath of the other path), raise ValueError.
        """
        # For the purpose of this method, drive and root are considered
        # separate parts, i.e.:
        #   Path('c:/').relative_to('c:')  gives Path('/')
        #   Path('c:/').relative_to('/')   raise ValueError
        if not other:
            raise TypeError("need at least one argument")
        parts = self._parts
        drv = self._drv
        root = self._root
        if root:
            abs_parts = [drv, root] + parts[1:]
        else:
            abs_parts = parts
        to_drv, to_root, to_parts = self._parse_args(other)
        if to_root:
            to_abs_parts = [to_drv, to_root] + to_parts[1:]
        else:
            to_abs_parts = to_parts
        n = len(to_abs_parts)
        cf = self._flavour.casefold_parts
        if (root or drv) if n == 0 else cf(abs_parts[:n]) != cf(to_abs_parts):
            formatted = self._format_parsed_parts(to_drv, to_root, to_parts)
            raise ValueError("{!r} is not in the subpath of {!r}"
                    " OR one path is relative and the other is absolute."
                             .format(str(self), str(formatted)))
        return self._from_parsed_parts('', root if n == 1 else '',
                                       abs_parts[n:])



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>rename</code></h2></summary> -->
<summary>
rename
</summary>
<!-- ### `rename` -->
Method

directory of the Path object.


#### Parameters

##### `Returns the new Path instance pointing to the target path.`

{parameter_info}




#### Source

<details>
<summary>View source</summary>

```python


    def rename(self, target):
        """
        Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.rename(self, target)
        return self.__class__(target)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>replace</code></h2></summary> -->
<summary>
replace
</summary>
<!-- ### `replace` -->
Method

directory of the Path object.


#### Parameters

##### `Returns the new Path instance pointing to the target path.`

{parameter_info}




#### Source

<details>
<summary>View source</summary>

```python


    def replace(self, target):
        """
        Rename this path to the target path, overwriting if that path exists.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.replace(self, target)
        return self.__class__(target)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>resolve</code></h2></summary> -->
<summary>
resolve
</summary>
<!-- ### `resolve` -->
Method

Windows).


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def resolve(self, strict=False):
        """
        Make the path absolute, resolving all symlinks on the way and also
        normalizing it (for example turning slashes into backslashes under
        Windows).
        """
        s = self._flavour.resolve(self, strict=strict)
        if s is None:
            # No symlink resolution => for consistency, raise an error if
            # the path doesn't exist or is forbidden
            self.stat()
            s = str(self.absolute())
        # Now we have no symlinks in the path, it's safe to normalize it.
        normed = self._flavour.pathmod.normpath(s)
        obj = self._from_parts((normed,), init=False)
        obj._init(template=self)
        return obj



```

</details>

#### References

- [Path.absolute](#absolute)
- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>rglob</code></h2></summary> -->
<summary>
rglob
</summary>
<!-- ### `rglob` -->
Method

Recursively yield all existing files (of any kind, including


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def rglob(self, pattern):
        """Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        """
        sys.audit("pathlib.Path.rglob", self, pattern)
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(("**",) + tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p



```

</details>

#### References

- [Path.rglob](#rglob)

</details>


<details>
<!-- <summary><h2><code>rmdir</code></h2></summary> -->
<summary>
rmdir
</summary>
<!-- ### `rmdir` -->
Method

Remove this directory.  The directory must be empty.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def rmdir(self):
        """
        Remove this directory.  The directory must be empty.
        """
        self._accessor.rmdir(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>samefile</code></h2></summary> -->
<summary>
samefile
</summary>
<!-- ### `samefile` -->
Method

Return whether other_path is the same or not as this file


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def samefile(self, other_path):
        """Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        """
        st = self.stat()
        try:
            other_st = other_path.stat()
        except AttributeError:
            other_st = self._accessor.stat(other_path)
        return os.path.samestat(st, other_st)



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>stat</code></h2></summary> -->
<summary>
stat
</summary>
<!-- ### `stat` -->
Method

os.stat() does.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def stat(self):
        """
        Return the result of the stat() system call on this path, like
        os.stat() does.
        """
        return self._accessor.stat(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>symlink_to</code></h2></summary> -->
<summary>
symlink_to
</summary>
<!-- ### `symlink_to` -->
Method

Note the order of arguments (self, target) is the reverse of os.symlink's.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def symlink_to(self, target, target_is_directory=False):
        """
        Make this path a symlink pointing to the given path.
        Note the order of arguments (self, target) is the reverse of os.symlink's.
        """
        self._accessor.symlink(target, self, target_is_directory)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>touch</code></h2></summary> -->
<summary>
touch
</summary>
<!-- ### `touch` -->
Method

Create this file with the given access mode, if it doesn't exist.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def touch(self, mode=0o666, exist_ok=True):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                self._accessor.utime(self, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
        fd = self._raw_open(flags, mode)
        os.close(fd)



```

</details>

#### References

- [Path._raw_open](#_raw_open)

</details>


<details>
<!-- <summary><h2><code>unlink</code></h2></summary> -->
<summary>
unlink
</summary>
<!-- ### `unlink` -->
Method

If the path is a directory, use rmdir() instead.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def unlink(self, missing_ok=False):
        """
        Remove this file or link.
        If the path is a directory, use rmdir() instead.
        """
        try:
            self._accessor.unlink(self)
        except FileNotFoundError:
            if not missing_ok:
                raise



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>with_name</code></h2></summary> -->
<summary>
with_name
</summary>
<!-- ### `with_name` -->
Method

Return a new path with the file name changed.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def with_name(self, name):
        """Return a new path with the file name changed."""
        if not self.name:
            raise ValueError("%r has an empty name" % (self,))
        drv, root, parts = self._flavour.parse_parts((name,))
        if (not name or name[-1] in [self._flavour.sep, self._flavour.altsep]
            or drv or root or len(parts) != 1):
            raise ValueError("Invalid name %r" % (name))
        return self._from_parsed_parts(self._drv, self._root,
                                       self._parts[:-1] + [name])



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>with_stem</code></h2></summary> -->
<summary>
with_stem
</summary>
<!-- ### `with_stem` -->
Method

Return a new path with the stem changed.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def with_stem(self, stem):
        """Return a new path with the stem changed."""
        return self.with_name(stem + self.suffix)



```

</details>

#### References

- [Path.with_name](#with_name)

</details>


<details>
<!-- <summary><h2><code>with_suffix</code></h2></summary> -->
<summary>
with_suffix
</summary>
<!-- ### `with_suffix` -->
Method

Return a new path with the file suffix changed.  If the path


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def with_suffix(self, suffix):
        """Return a new path with the file suffix changed.  If the path
        has no suffix, add given suffix.  If the given suffix is an empty
        string, remove the suffix from the path.
        """
        f = self._flavour
        if f.sep in suffix or f.altsep and f.altsep in suffix:
            raise ValueError("Invalid suffix %r" % (suffix,))
        if suffix and not suffix.startswith('.') or suffix == '.':
            raise ValueError("Invalid suffix %r" % (suffix))
        name = self.name
        if not name:
            raise ValueError("%r has an empty name" % (self,))
        old_suffix = self.suffix
        if not old_suffix:
            name = name + suffix
        else:
            name = name[:-len(old_suffix)] + suffix
        return self._from_parsed_parts(self._drv, self._root,
                                       self._parts[:-1] + [name])



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>write_bytes</code></h2></summary> -->
<summary>
write_bytes
</summary>
<!-- ### `write_bytes` -->
Method

Open the file in bytes mode, write to it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def write_bytes(self, data):
        """
        Open the file in bytes mode, write to it, and close the file.
        """
        # type-check for the buffer interface before truncating the file
        view = memoryview(data)
        with self.open(mode='wb') as f:
            return f.write(view)



```

</details>

#### References

- [Path.open](#open)

</details>


<details>
<!-- <summary><h2><code>write_text</code></h2></summary> -->
<summary>
write_text
</summary>
<!-- ### `write_text` -->
Method

Open the file in text mode, write to it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def write_text(self, data, encoding=None, errors=None):
        """
        Open the file in text mode, write to it, and close the file.
        """
        if not isinstance(data, str):
            raise TypeError('data must be str, not %s' %
                            data.__class__.__name__)
        with self.open(mode='w', encoding=encoding, errors=errors) as f:
            return f.write(data)



```

</details>

#### References

- [Path.open](#open)

</details>


Docs built at 2021-06-16 05:07:07.575726

<details>
<summary>View source</summary>

```python

class Path(PurePath):
    """PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
    """
    __slots__ = (
        '_accessor',
    )

    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath
        self = cls._from_parts(args, init=False)
        if not self._flavour.is_supported:
            raise NotImplementedError("cannot instantiate %r on your system"
                                      % (cls.__name__,))
        self._init()
        return self

    def _init(self,
              # Private non-constructor arguments
              template=None,
              ):
        if template is not None:
            self._accessor = template._accessor
        else:
            self._accessor = _normal_accessor

    def _make_child_relpath(self, part):
        # This is an optimization used for dir walking.  `part` must be
        # a single part relative to this path.
        parts = self._parts + [part]
        return self._from_parsed_parts(self._drv, self._root, parts)

    def __enter__(self):
        return self

    def __exit__(self, t, v, tb):
        # https://bugs.python.org/issue39682
        # In previous versions of pathlib, this method marked this path as
        # closed; subsequent attempts to perform I/O would raise an IOError.
        # This functionality was never documented, and had the effect of
        # making Path objects mutable, contrary to PEP 428. In Python 3.9 the
        # _closed attribute was removed, and this method made a no-op.
        # This method and __enter__()/__exit__() should be deprecated and
        # removed in the future.
        pass

    def _opener(self, name, flags, mode=0o666):
        # A stub for the opener argument to built-in open()
        return self._accessor.open(self, flags, mode)

    def _raw_open(self, flags, mode=0o777):
        """
        Open the file pointed by this path and return a file descriptor,
        as os.open() does.
        """
        return self._accessor.open(self, flags, mode)

    # Public API

    @classmethod
    def cwd(cls):
        """Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        """
        return cls(os.getcwd())

    @classmethod
    def home(cls):
        """Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        """
        return cls(cls()._flavour.gethomedir(None))

    def samefile(self, other_path):
        """Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        """
        st = self.stat()
        try:
            other_st = other_path.stat()
        except AttributeError:
            other_st = self._accessor.stat(other_path)
        return os.path.samestat(st, other_st)

    def iterdir(self):
        """Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        """
        for name in self._accessor.listdir(self):
            if name in {'.', '..'}:
                # Yielding a path object for these makes little sense
                continue
            yield self._make_child_relpath(name)

    def glob(self, pattern):
        """Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        """
        sys.audit("pathlib.Path.glob", self, pattern)
        if not pattern:
            raise ValueError("Unacceptable pattern: {!r}".format(pattern))
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p

    def rglob(self, pattern):
        """Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        """
        sys.audit("pathlib.Path.rglob", self, pattern)
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(("**",) + tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p

    def absolute(self):
        """Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        """
        # XXX untested yet!
        if self.is_absolute():
            return self
        # FIXME this must defer to the specific flavour (and, under Windows,
        # use nt._getfullpathname())
        obj = self._from_parts([os.getcwd()] + self._parts, init=False)
        obj._init(template=self)
        return obj

    def resolve(self, strict=False):
        """
        Make the path absolute, resolving all symlinks on the way and also
        normalizing it (for example turning slashes into backslashes under
        Windows).
        """
        s = self._flavour.resolve(self, strict=strict)
        if s is None:
            # No symlink resolution => for consistency, raise an error if
            # the path doesn't exist or is forbidden
            self.stat()
            s = str(self.absolute())
        # Now we have no symlinks in the path, it's safe to normalize it.
        normed = self._flavour.pathmod.normpath(s)
        obj = self._from_parts((normed,), init=False)
        obj._init(template=self)
        return obj

    def stat(self):
        """
        Return the result of the stat() system call on this path, like
        os.stat() does.
        """
        return self._accessor.stat(self)

    def owner(self):
        """
        Return the login name of the file owner.
        """
        return self._accessor.owner(self)

    def group(self):
        """
        Return the group name of the file gid.
        """
        return self._accessor.group(self)

    def open(self, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None):
        """
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        """
        return io.open(self, mode, buffering, encoding, errors, newline,
                       opener=self._opener)

    def read_bytes(self):
        """
        Open the file in bytes mode, read it, and close the file.
        """
        with self.open(mode='rb') as f:
            return f.read()

    def read_text(self, encoding=None, errors=None):
        """
        Open the file in text mode, read it, and close the file.
        """
        with self.open(mode='r', encoding=encoding, errors=errors) as f:
            return f.read()

    def write_bytes(self, data):
        """
        Open the file in bytes mode, write to it, and close the file.
        """
        # type-check for the buffer interface before truncating the file
        view = memoryview(data)
        with self.open(mode='wb') as f:
            return f.write(view)

    def write_text(self, data, encoding=None, errors=None):
        """
        Open the file in text mode, write to it, and close the file.
        """
        if not isinstance(data, str):
            raise TypeError('data must be str, not %s' %
                            data.__class__.__name__)
        with self.open(mode='w', encoding=encoding, errors=errors) as f:
            return f.write(data)

    def readlink(self):
        """
        Return the path to which the symbolic link points.
        """
        path = self._accessor.readlink(self)
        obj = self._from_parts((path,), init=False)
        obj._init(template=self)
        return obj

    def touch(self, mode=0o666, exist_ok=True):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                self._accessor.utime(self, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
        fd = self._raw_open(flags, mode)
        os.close(fd)

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
            self._accessor.mkdir(self, mode)
        except FileNotFoundError:
            if not parents or self.parent == self:
                raise
            self.parent.mkdir(parents=True, exist_ok=True)
            self.mkdir(mode, parents=False, exist_ok=exist_ok)
        except OSError:
            # Cannot rely on checking for EEXIST, since the operating system
            # could give priority to other errors like EACCES or EROFS
            if not exist_ok or not self.is_dir():
                raise

    def chmod(self, mode):
        """
        Change the permissions of the path, like os.chmod().
        """
        self._accessor.chmod(self, mode)

    def lchmod(self, mode):
        """
        Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
        """
        self._accessor.lchmod(self, mode)

    def unlink(self, missing_ok=False):
        """
        Remove this file or link.
        If the path is a directory, use rmdir() instead.
        """
        try:
            self._accessor.unlink(self)
        except FileNotFoundError:
            if not missing_ok:
                raise

    def rmdir(self):
        """
        Remove this directory.  The directory must be empty.
        """
        self._accessor.rmdir(self)

    def lstat(self):
        """
        Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
        """
        return self._accessor.lstat(self)

    def link_to(self, target):
        """
        Create a hard link pointing to a path named target.
        """
        self._accessor.link_to(self, target)

    def rename(self, target):
        """
        Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.rename(self, target)
        return self.__class__(target)

    def replace(self, target):
        """
        Rename this path to the target path, overwriting if that path exists.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.replace(self, target)
        return self.__class__(target)

    def symlink_to(self, target, target_is_directory=False):
        """
        Make this path a symlink pointing to the given path.
        Note the order of arguments (self, target) is the reverse of os.symlink's.
        """
        self._accessor.symlink(target, self, target_is_directory)

    # Convenience functions for querying the stat results

    def exists(self):
        """
        Whether this path exists.
        """
        try:
            self.stat()
        except OSError as e:
            if not _ignore_error(e):
                raise
            return False
        except ValueError:
            # Non-encodable path
            return False
        return True

    def is_dir(self):
        """
        Whether this path is a directory.
        """
        try:
            return S_ISDIR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_file(self):
        """
        Whether this path is a regular file (also True for symlinks pointing
        to regular files).
        """
        try:
            return S_ISREG(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_mount(self):
        """
        Check if this path is a POSIX mount point
        """
        # Need to exist and be a dir
        if not self.exists() or not self.is_dir():
            return False

        try:
            parent_dev = self.parent.stat().st_dev
        except OSError:
            return False

        dev = self.stat().st_dev
        if dev != parent_dev:
            return True
        ino = self.stat().st_ino
        parent_ino = self.parent.stat().st_ino
        return ino == parent_ino

    def is_symlink(self):
        """
        Whether this path is a symbolic link.
        """
        try:
            return S_ISLNK(self.lstat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_block_device(self):
        """
        Whether this path is a block device.
        """
        try:
            return S_ISBLK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_char_device(self):
        """
        Whether this path is a character device.
        """
        try:
            return S_ISCHR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_fifo(self):
        """
        Whether this path is a FIFO.
        """
        try:
            return S_ISFIFO(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_socket(self):
        """
        Whether this path is a socket.
        """
        try:
            return S_ISSOCK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def expanduser(self):
        """ Return a new path with expanded ~ and ~user constructs
        (as returned by os.path.expanduser)
        """
        if (not (self._drv or self._root) and
            self._parts and self._parts[0][:1] == '~'):
            homedir = self._flavour.gethomedir(self._parts[0][1:])
            return self._from_parts([homedir] + self._parts[1:])

        return self


```
</details>

</details>
