
Start MinIO.

```
podman-compose up --env-file=.env.example -d
```

Demonstrate and experiment with various backends for writing `zarr` arrays to bucket storage:

### 🔙 Run an example which uses S3FS as a backend
```python
pixi run s3fs
```
### 🆕 Run an example which uses obstore as a backend
```python
pixi run obstore
```

### 🚮 Empty bucket contents between example runs
This avoids collisions within zarr artifacts and metadata
```python
pixi run empty
```