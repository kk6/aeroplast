# aeroplast

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8a948b4c79474577a00c30618f689ed8)](https://app.codacy.com/app/hiro.ashiya/aeroplast?utm_source=github.com&utm_medium=referral&utm_content=kk6/aeroplast&utm_campaign=Badge_Grade_Dashboard)

Transparent PNG conversion (Mainly for Twitter)

## Required packaging tool:

[Poetry](https://poetry.eustace.io/)

## Usage:

### Install packages

```shell
$ poetry install
```

### Invoke commands

```shell
$ poetry run aeroplast ...
```

or

```shell
$ poetry shell
$ poetry develop
$ aeroplast
```

### Convert image

```shell
$ poetry run aeroplast convert original.png converted.png
```

### help

```shell
$ poetry run aeroplast --help
```

## Origin of the name

```
aeroplast == Bubble wrap == 気泡緩衝材 == プチプチ
```

## License

MIT
