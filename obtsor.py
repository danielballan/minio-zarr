import zarr
from importlib.metadata import version
from packaging.version import Version
import numpy as np
from obstore.store import S3Store

ZARR_LIB_V2 = Version(version("zarr")) < Version("3")
if ZARR_LIB_V2:
    raise RuntimeError("Zarr 3 is required to run this example.")
else:
    from zarr.storage import ObjectStore


object_store = S3Store(
    endpoint="http://localhost:9000",
    access_key_id="minioadmin",
    secret_access_key="minioadmin",
    bucket="buck",
    virtual_hosted_style_request=False,
    client_options={"allow_http": True},
)

store = ObjectStore(store=object_store)

# Start with the same example as s3fs
data = np.random.random((100, 100))

# zarr.create_array(store=store, shape=(100, 100), chunks=(100, 100), dtype="int32")
# Write
zarr.save(store, data)
# Read
z = zarr.open_array(store)
print(z[:])
