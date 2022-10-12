# nile-coverage

> _[Nile](https://github.com/OpenZeppelin/nile) plugin adding coverage reports for Cairo Smart Contracts._

## Getting started

> :warning: **This package requires cairo-lang >= 0.10.1. If you are using older versions, check [this](https://github.com/ericnordelo/cairo-coverage#how-to-make-it-work) section before continuing.**

Install the plugin inside the virtual environment of your Nile project:

```sh
(env): pip install nile-coverage
```

Nile automatically detecs installed plugins using python [entry points](https://packaging.python.org/en/latest/specifications/entry-points/) feature. You should see the coverage command listed running nile, and you can run the report with:

```sh
(env): nile coverage
```


