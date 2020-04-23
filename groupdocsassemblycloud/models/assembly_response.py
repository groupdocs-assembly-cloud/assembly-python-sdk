# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="AssemblyResponse.py">
#   Copyright (c) 2020 GroupDocs.Assembly for Cloud
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
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class AssemblyResponse(object):
    """Base class for all responses.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str'
    }

    attribute_map = {
        'request_id': 'RequestId'
    }

    discriminator_value_class_map = {
        'AssemblyApiErrorResponse': 'AssemblyApiErrorResponse',
        'FileFormatsResponse': 'FileFormatsResponse'
    }

    def __init__(self, request_id=None):  # noqa: E501
        """AssemblyResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self.discriminator = 'Type'

        if request_id is not None:
            self.request_id = request_id

    @property
    def request_id(self):
        """Gets the request_id of this AssemblyResponse.  # noqa: E501

        Gets or sets request Id.  # noqa: E501

        :return: The request_id of this AssemblyResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AssemblyResponse.

        Gets or sets request Id.  # noqa: E501

        :param request_id: The request_id of this AssemblyResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id
    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            alias = attr
            if self.attribute_map[alias]:
                alias = self.attribute_map[alias]
            value = getattr(self, attr)
            if isinstance(value, list):
                result[alias] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[alias] = value.to_dict()
            elif isinstance(value, dict):
                result[alias] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[alias] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssemblyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other