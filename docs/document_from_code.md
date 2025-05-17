# Contents for: document_from_code

* [document\_from\_code](#document_from_code)
  * [os](#document_from_code.os)
  * [Context](#document_from_code.Context)
  * [PythonLoader](#document_from_code.PythonLoader)
  * [MarkdownRenderer](#document_from_code.MarkdownRenderer)
  * [settings](#document_from_code.settings)
  * [VERSION](#document_from_code.VERSION)
  * [DOCSPATH](#document_from_code.DOCSPATH)
  * [SEARCHPATHS](#document_from_code.SEARCHPATHS)
  * [SKIPNAMES](#document_from_code.SKIPNAMES)
  * [checkmodule](#document_from_code.checkmodule)
  * [create\_docs](#document_from_code.create_docs)

<a id="document_from_code"></a>

# document\_from\_code

Gerates documentation from comments in the code
Coded to run in a github action against the master branch
uses:
pydoc-markdown to generate the documentation

<a id="document_from_code.os"></a>

## os

<a id="document_from_code.Context"></a>

## Context

<a id="document_from_code.PythonLoader"></a>

## PythonLoader

<a id="document_from_code.MarkdownRenderer"></a>

## MarkdownRenderer

<a id="document_from_code.settings"></a>

## settings

<a id="document_from_code.VERSION"></a>

## VERSION

<a id="document_from_code.DOCSPATH"></a>

#### DOCSPATH

<a id="document_from_code.SEARCHPATHS"></a>

#### SEARCHPATHS

<a id="document_from_code.SKIPNAMES"></a>

#### SKIPNAMES

<a id="document_from_code.checkmodule"></a>

#### checkmodule

```python
def checkmodule(name)
```

Check if a module is valid for documentation

<a id="document_from_code.create_docs"></a>

#### create\_docs

```python
def create_docs()
```

Create the documents for the project

