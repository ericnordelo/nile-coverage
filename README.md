# nile-coverage

[![PyPI](https://img.shields.io/pypi/v/nile-coverage)](https://pypi.org/project/nile-coverage/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nile-coverage)

> _[Nile](https://github.com/OpenZeppelin/nile) plugin adding coverage reports for Cairo Smart Contracts._

## Getting started

Install the plugin inside the virtual environment of your Nile project:

```sh
(env): pip install nile-coverage
```

Nile automatically detects installed plugins using python [entry points](https://packaging.python.org/en/latest/specifications/entry-points/) feature. You should see the coverage command listed running `nile`, and you can run the report with:

```sh
(env): nile coverage
```

For a full list of options run:

```sh
(env): nile coverage --help
```

## Recipes

### 1. Run coverage in a subset of the tests suite.

Mark tests with [pytest marks](https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark) and use the `--mark` argument to run a subset of tests:

```sh
(env): nile coverage -m unit
```

### 2. Integrate with [codecov.io](https://about.codecov.io/).

Generate a cobertura format coverage xml file named "coverage.xml" using the `--xml` flag:

```sh
(env): nile coverage --xml
```

### 3. Change the default folder containing Smart Contracts.

If your Smart Contracts are in a different folder than "contracts" (Nile default), use the
`--contracts-folder` flag to set the correct one:

```sh
(env): nile coverage -c src
```

## Troubleshooting

### 1. Report doesn't catch execution when multiple threads are used with [pytest-xdist](https://pypi.org/project/pytest-xdist/).

To solve this, pass the `--single-thread` option to the coverage command:

```sh
(env): nile coverage -s
```

## Acknowledgements

This package uses the [starknet-edu/cairo-coverage](https://github.com/starknet-edu/cairo-coverage) Virtual Machine override to get covered lines for the final report. Special thanks to [@LucasLvy](https://github.com/LucasLvy) from StarkWare!
