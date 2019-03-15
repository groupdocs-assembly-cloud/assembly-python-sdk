# groupdocsassemblycloud.AssemblyApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_assemble_document**](AssemblyApi.md#post_assemble_document) | **POST** /assembly/{name}/build | Builds a document using document template and XML or JSON data passed in request


# **post_assemble_document**
> file post_assemble_document(name, data, save_options, folder=folder, dest_file_name=dest_file_name)

Builds a document using document template and XML or JSON data passed in request

### Example
```python
from __future__ import print_function
import time
import groupdocsassemblycloud
from groupdocsassemblycloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = groupdocsassemblycloud.AssemblyApi()
name = 'name_example' # str | File name of template, which is located on a storage
data = '/path/to/file.txt' # file | Report data in JSON or XML format
save_options = groupdocsassemblycloud.LoadSaveOptionsData() # LoadSaveOptionsData | Save options in json format
folder = 'folder_example' # str | Folder path where template file is located(on a storage) (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of built document (optional)

try:
    # Builds a document using document template and XML or JSON data passed in request
    api_response = api_instance.post_assemble_document(name, data, save_options, folder=folder, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssemblyApi->post_assemble_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| File name of template, which is located on a storage | 
 **data** | **file**| Report data in JSON or XML format | 
 **save_options** | [**LoadSaveOptionsData**](LoadSaveOptionsData.md)| Save options in json format | 
 **folder** | **str**| Folder path where template file is located(on a storage) | [optional] 
 **dest_file_name** | **str**| Result name of built document | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

