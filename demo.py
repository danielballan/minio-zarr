import zarr
import s3fs
import numpy as np

bucket = "buck"
name = "sample"

s3 = s3fs.S3FileSystem(
    client_kwargs={"endpoint_url": "http://localhost:9000"},
    key="minioadmin",
    secret="minioadmin",
    use_ssl=False,
)
s3store = s3fs.S3Map(root=f'{bucket}/{name}', s3=s3)

data = np.random.random((100, 100))
zarr.save(s3store, data)
