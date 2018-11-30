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

from .azure_resource_base import AzureResourceBase


class AssignmentOperation(AzureResourceBase):
    """Represents underlying deployment detail for each update to the assignment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar name: Name of this resource.
    :vartype name: str
    :param blueprint_version: The blueprint version used for the assignment
     operation.
    :type blueprint_version: str
    :param assignment_state: State of this assignment operation.
    :type assignment_state: str
    :param time_created: Create time of this Assignment Operation.
    :type time_created: str
    :param time_started: Start time of the underlying deployment.
    :type time_started: str
    :param time_finished: Finish time of the overall underlying deployments.
    :type time_finished: str
    :param deployments: list of jobs in this assignment operation.
    :type deployments:
     list[~azure.mgmt.blueprint.models.AssignmentDeploymentJob]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'blueprint_version': {'key': 'properties.blueprintVersion', 'type': 'str'},
        'assignment_state': {'key': 'properties.assignmentState', 'type': 'str'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'str'},
        'time_started': {'key': 'properties.timeStarted', 'type': 'str'},
        'time_finished': {'key': 'properties.timeFinished', 'type': 'str'},
        'deployments': {'key': 'properties.deployments', 'type': '[AssignmentDeploymentJob]'},
    }

    def __init__(self, **kwargs):
        super(AssignmentOperation, self).__init__(**kwargs)
        self.blueprint_version = kwargs.get('blueprint_version', None)
        self.assignment_state = kwargs.get('assignment_state', None)
        self.time_created = kwargs.get('time_created', None)
        self.time_started = kwargs.get('time_started', None)
        self.time_finished = kwargs.get('time_finished', None)
        self.deployments = kwargs.get('deployments', None)
