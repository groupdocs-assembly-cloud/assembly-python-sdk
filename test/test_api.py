"""
Module with API test
"""
#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="GroupDocs" file="base_test_context.py">
#   Copyright (c) 2019 GroupDocs.Assembly for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
#
import os
from test.base_test_context import BaseTestContext
import groupdocsassemblycloud.models.requests

class TestApi(BaseTestContext):
    """
    Test API class
    """
    test_folder = 'GroupDocs.Assembly'

    def test_assembly(self):
        """Assemble document test

        """
        filename = 'TestAllChartTypes.docx'
        remote_name = filename
        with open(os.path.join(self.local_test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = groupdocsassemblycloud.models.requests.PostAssembleDocumentRequest(remote_name, os.path.join(self.local_test_folder, "Teams.json"), groupdocsassemblycloud.LoadSaveOptionsData('docx'), os.path.join(self.remote_test_folder, self.test_folder),)
        result = self.assembly_api.post_assemble_document(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while building document')