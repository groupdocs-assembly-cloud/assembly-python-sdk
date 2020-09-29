# groupdocsassemblycloud.AssemblyApi

All URIs are relative to *https://localhost/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assemble_document**](AssemblyApi.md#assemble_document) | **POST** /assembly/assemble | Builds a document using document template and XML or JSON data passed in request.
[**copy_file**](AssemblyApi.md#copy_file) | **PUT** /assembly/storage/file/copy/{srcPath} | Copy file
[**copy_folder**](AssemblyApi.md#copy_folder) | **PUT** /assembly/storage/folder/copy/{srcPath} | Copy folder
[**create_folder**](AssemblyApi.md#create_folder) | **PUT** /assembly/storage/folder/{path} | Create the folder
[**delete_file**](AssemblyApi.md#delete_file) | **DELETE** /assembly/storage/file/{path} | Delete file
[**delete_folder**](AssemblyApi.md#delete_folder) | **DELETE** /assembly/storage/folder/{path} | Delete folder
[**download_file**](AssemblyApi.md#download_file) | **GET** /assembly/storage/file/{path} | Download file
[**get_files_list**](AssemblyApi.md#get_files_list) | **GET** /assembly/storage/folder/{path} | Get all files and folders within a folder
[**get_supported_file_formats**](AssemblyApi.md#get_supported_file_formats) | **GET** /assembly/formats | Retrieves list of supported file formats.
[**move_file**](AssemblyApi.md#move_file) | **PUT** /assembly/storage/file/move/{srcPath} | Move file
[**move_folder**](AssemblyApi.md#move_folder) | **PUT** /assembly/storage/folder/move/{srcPath} | Move folder
[**upload_file**](AssemblyApi.md#upload_file) | **PUT** /assembly/storage/file/{path} | Upload file


# **assemble_document**
> file assemble_document(assemble_options)

Builds a document using document template and XML or JSON data passed in request.

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
assemble_options = groupdocsassemblycloud.AssembleOptions() # AssembleOptions | Assemble Options. It should be JSON or XML with TemplateFileInfo, SaveFormat, ReportData and etc.             

try:
    # Builds a document using document template and XML or JSON data passed in request.
    api_response = api_instance.assemble_document(assemble_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssemblyApi->assemble_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assemble_options** | [**AssembleOptions**](AssembleOptions.md)| Assemble Options. It should be JSON or XML with TemplateFileInfo, SaveFormat, ReportData and etc.              | 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file**
> copy_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination file path
src_path = 'src_path_example' # str | Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to copy (optional)

try:
    # Copy file
    api_instance.copy_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling AssemblyApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination file path | 
 **src_path** | **str**| Source file&#39;s path e.g. &#39;/Folder 1/file.ext&#39; or &#39;/Bucket/Folder 1/file.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> copy_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination folder path e.g. '/dst'
src_path = 'src_path_example' # str | Source folder path e.g. /Folder1
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Copy folder
    api_instance.copy_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling AssemblyApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_path** | **str**| Source folder path e.g. /Folder1 | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
path = 'path_example' # str | Target folder's path e.g. Folder1/Folder2/. The folders will be created recursively
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Create the folder
    api_instance.create_folder(path, storage_name=storage_name)
except ApiException as e:
    print("Exception when calling AssemblyApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target folder&#39;s path e.g. Folder1/Folder2/. The folders will be created recursively | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
path = 'path_example' # str | Path of the file including file name and extension e.g. /Folder1/file.ext
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to delete (optional)

try:
    # Delete file
    api_instance.delete_file(path, storage_name=storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling AssemblyApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the file including file name and extension e.g. /Folder1/file.ext | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. /Folder1s
storage_name = 'storage_name_example' # str | Storage name (optional)
recursive = false # bool | Enable to delete folders, subfolders and files (optional) (default to false)

try:
    # Delete folder
    api_instance.delete_folder(path, storage_name=storage_name, recursive=recursive)
except ApiException as e:
    print("Exception when calling AssemblyApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. /Folder1s | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(path, storage_name=storage_name, version_id=version_id)

Download file

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
path = 'path_example' # str | Path of the file including the file name and extension e.g. /folder1/file.ext
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to download (optional)

try:
    # Download file
    api_response = api_instance.download_file(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssemblyApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the file including the file name and extension e.g. /folder1/file.ext | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. /Folder1
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get all files and folders within a folder
    api_response = api_instance.get_files_list(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssemblyApi->get_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. /Folder1 | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_file_formats**
> FileFormatsResponse get_supported_file_formats()

Retrieves list of supported file formats.

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))

try:
    # Retrieves list of supported file formats.
    api_response = api_instance.get_supported_file_formats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssemblyApi->get_supported_file_formats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FileFormatsResponse**](FileFormatsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination file path e.g. '/dest.ext'
src_path = 'src_path_example' # str | Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to move (optional)

try:
    # Move file
    api_instance.move_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling AssemblyApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_path** | **str**| Source file&#39;s path e.g. &#39;/Folder 1/file.ext&#39; or &#39;/Bucket/Folder 1/file.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination folder path to move to e.g '/dst'
src_path = 'src_path_example' # str | Source folder path e.g. /Folder1
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Move folder
    api_instance.move_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling AssemblyApi->move_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_path** | **str**| Source folder path e.g. /Folder1 | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(file_content, path, storage_name=storage_name)

Upload file

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = groupdocsassemblycloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi(groupdocsassemblycloud.ApiClient(configuration))
file_content = '/path/to/file.txt' # file | File to upload
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext              If the content is multipart and path does not contains the file name it tries to get them from filename parameter              from Content-Disposition header.
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Upload file
    api_response = api_instance.upload_file(file_content, path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssemblyApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_content** | **file**| File to upload | 
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext              If the content is multipart and path does not contains the file name it tries to get them from filename parameter              from Content-Disposition header. | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

