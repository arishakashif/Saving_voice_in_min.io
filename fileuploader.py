# Import MinIO library.
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import os

# Initialize minioClient with an endpoint and access/secret keys.
def getMinioClient(access,secret):
       return Minio(
              'localhost:9000',
              access_key=access,
              secret_key=secret,
              secure=False
       )

if __name__=='__main__':
       minioClient = getMinioClient('arisha_kashif','prejudice_35')

       if(not minioClient.bucket_exists('testbucket')):
              try:
                     minioClient.make_bucket('testbucket')
              except ResponseError as err:
                     raise

       #Adding files in the bucket
       try:
              with open('/tmp/test.wav','rb') as testfile:
                     statdata = os.stat('/tmp//test.wav')
                     minioClient.put_object(
                            'testbucket',
                            'output.wav',
                            testfile,
                            statdata.st_size
                     )
       except ResponseError as err:
              raise

       #Removing files from the bucket

       # try:
       #        minioClient.remove_object('testbucket','output.wav')
       # except ResponseError as err:
       #        pass

       #Removing bucket

       # try:
       #        minioClient.remove_bucket('testbucket')
       # except ResponseError as err:
       #        pass