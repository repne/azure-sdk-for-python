# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ErrorResponseBody(Model):
    """Error Body contract.

    :param code: Service-defined error code. This code serves as a sub-status
     for the HTTP error code specified in the response.
    :type code: str
    :param message: Human-readable representation of the error.
    :type message: str
    :param details: The list of invalid fields send in request, in case of
     validation error.
    :type details: list[~azure.mgmt.apimanagement.models.ErrorFieldContract]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorFieldContract]'},
    }

    def __init__(self, *, code: str=None, message: str=None, details=None, **kwargs) -> None:
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details
