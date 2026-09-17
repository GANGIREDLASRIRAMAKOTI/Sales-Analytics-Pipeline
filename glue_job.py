import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()

df=spark.read.format('csv').option('header','true').load('s3://project-2-165811308743-ap-southeast-2-an/project/')
df.show()
df.write.mode('overwrite').format('parquet').save('s3://project-target-165811308743-ap-southeast-2-an/project-01/')
