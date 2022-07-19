# Psetv2 libwally-core

This repo reproduces an error encountered in [libwally-core psetv2 branch](https://github.com/ElementsProject/libwally-core/tree/psbt_v2_merge).

`psbt_get_output_asset` makes the psbt invalid (no asset in output).

# Reproduce

```
make env
source venv/bin/activate
make deps
make test
```

to quiv the virtual env type `deactivate`
