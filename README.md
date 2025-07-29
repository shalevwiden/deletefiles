## Delete Files Function

```python
clearfiles(folderpath,filetype,avoid)
```

<br>
This function will delete any file with a given filetype parameter in the path specified by the folderpath parameter.
In addition it will avoid files in a list passed in the avoid parameter.
<br>
This is incredibly useful when working with a python script that is creating lots of files, especially during development when you might be changing file names or still solidifying paths.
