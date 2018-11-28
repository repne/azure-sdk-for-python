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


class BackendServiceFabricClusterProperties(Model):
    """Properties of the Service Fabric Type Backend.

    All required parameters must be populated in order to send to Azure.

    :param client_certificatethumbprint: Required. The client certificate
     thumbprint for the management endpoint.
    :type client_certificatethumbprint: str
    :param max_partition_resolution_retries: Maximum number of retries while
     attempting resolve the partition.
    :type max_partition_resolution_retries: int
    :param management_endpoints: Required. The cluster management endpoint.
    :type management_endpoints: list[str]
    :param server_certificate_thumbprints: Thumbprints of certificates cluster
     management service uses for tls communication
    :type server_certificate_thumbprints: list[str]
    :param server_x509_names: Server X509 Certificate Names Collection
    :type server_x509_names:
     list[~azure.mgmt.apimanagement.models.X509CertificateName]
    """

    _validation = {
        'client_certificatethumbprint': {'required': True},
        'management_endpoints': {'required': True},
    }

    _attribute_map = {
        'client_certificatethumbprint': {'key': 'clientCertificatethumbprint', 'type': 'str'},
        'max_partition_resolution_retries': {'key': 'maxPartitionResolutionRetries', 'type': 'int'},
        'management_endpoints': {'key': 'managementEndpoints', 'type': '[str]'},
        'server_certificate_thumbprints': {'key': 'serverCertificateThumbprints', 'type': '[str]'},
        'server_x509_names': {'key': 'serverX509Names', 'type': '[X509CertificateName]'},
    }

    def __init__(self, **kwargs):
        super(BackendServiceFabricClusterProperties, self).__init__(**kwargs)
        self.client_certificatethumbprint = kwargs.get('client_certificatethumbprint', None)
        self.max_partition_resolution_retries = kwargs.get('max_partition_resolution_retries', None)
        self.management_endpoints = kwargs.get('management_endpoints', None)
        self.server_certificate_thumbprints = kwargs.get('server_certificate_thumbprints', None)
        self.server_x509_names = kwargs.get('server_x509_names', None)
