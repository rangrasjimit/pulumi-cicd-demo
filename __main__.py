"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

bucket = storage.Bucket('jimit-pulumi-demo-bucket', 
    location = "US",
    uniform_bucket_level_access = True
)

pulumi.export('bucket_name', bucket.url)


