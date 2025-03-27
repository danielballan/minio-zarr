
Start MinIO.

```
podman-compose up --env-file=.env.example -d
```

Run demo script, which writes an array, reads it back, and prints it.

```python
pixi run python demo.py
```
