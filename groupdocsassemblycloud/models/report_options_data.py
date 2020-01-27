# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="GroupDocs" file="ReportOptionsData.py">
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
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class ReportOptionsData(object):
    """Save options data which is using for specifying additional save options, like save format and etc.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'save_format': 'str',
        'report_data': 'str'
    }

    attribute_map = {
        'save_format': 'SaveFormat',
        'report_data': 'ReportData'
    }

    def __init__(self, save_format=None, report_data=None):  # noqa: E501
        """ReportOptionsData - a model defined in Swagger"""  # noqa: E501

        self._save_format = None
        self._report_data = None
        self.discriminator = None

        if save_format is not None:
            self.save_format = save_format
        if report_data is not None:
            self.report_data = report_data

    @property
    def save_format(self):
        """Gets the save_format of this ReportOptionsData.  # noqa: E501

        Save format for assembled document  # noqa: E501

        :return: The save_format of this ReportOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this ReportOptionsData.

        Save format for assembled document  # noqa: E501

        :param save_format: The save_format of this ReportOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format
    @property
    def report_data(self):
        """Gets the report_data of this ReportOptionsData.  # noqa: E501

        Data for report  # noqa: E501

        :return: The report_data of this ReportOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._report_data

    @report_data.setter
    def report_data(self, report_data):
        """Sets the report_data of this ReportOptionsData.

        Data for report  # noqa: E501

        :param report_data: The report_data of this ReportOptionsData.  # noqa: E501
        :type: str
        """
        self._report_data = report_data
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
        if not isinstance(other, ReportOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
