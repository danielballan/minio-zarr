from minio import Minio
from minio.deleteobjects import DeleteObject

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False,
)

if client.bucket_exists("buck"):
    delete_object_list = map(
        lambda x: DeleteObject(x.object_name),
        client.list_objects("buck", recursive=True),
    )
    errors = client.remove_objects("buck", delete_object_list)
    for error in errors:
        print("error occurred when deleting object", error)
else:
    client.make_bucket("buck")

print("🚮 bucket has been emptied 🚮")
