from storages.backends.s3boto3 import S3Boto3Storage
# esto nos permite subir todos nuestros archivos a AWS y guardarlos de manera correcta

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'private'
    
class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'private'
    file_overwrite = False