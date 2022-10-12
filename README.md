# nile-coverage

> _[Nile](https://github.com/OpenZeppelin/nile) plugin adding coverage reports for Cairo Smart Contracts._

## Getting started

> :warning: WARNING
>
> **This package requires cairo-lang >= 0.10.1. If you are using older versions, check [this](https://github.com/ericnordelo/cairo-coverage#how-to-make-it-work) section before continuing.**

Install the plugin inside the virtual environment of your Nile project:

```sh
(env): pip install nile-coverage
```

Nile automatically detecs installed plugins using python [entry points](https://packaging.python.org/en/latest/specifications/entry-points/) feature. You should see the coverage command listed running `nile`, and you can run the report with:

```sh
(env): nile coverage
```

For a full list of options run:

```sh
(env): nile coverage --help
```

## Troubleshooting

### 1. Report doesn't catch execution when multiple threads are used with [pytest-xdist](https://pypi.org/project/pytest-xdist/)

In order to solve this, pass the `--single-thread` option to the coverage command:

```sh
(env): nile coverage -s
```

### 2. How to run the coverage in a subset of the tests suite

Mark tests in with [pytest marks](https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark) and use the `--mark` argument to run a subset of tests:

```sh
(env): nile coverage -m unit
```
