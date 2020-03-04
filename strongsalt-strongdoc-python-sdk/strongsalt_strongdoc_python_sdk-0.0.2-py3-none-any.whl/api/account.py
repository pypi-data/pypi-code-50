from strongdoc import client
from strongdoc import constants
from strongdoc.proto import strongdoc_pb2_grpc, accounts_pb2


# register_organization creates an organization
def register_organization(org_name, org_addr, admin_name, admin_password, admin_email):
    """
    Registers a new organization. A new administrator user will also be created.
    New users can be added using this administrator account.
    A gRPC connection timeout will be implemented.

    :param org_name:
        The organization name to create.
    :type org_name:
        `string`
    :param org_addr:
        The organization address.
    :type org_addr:
        `string`
    :param admin_name:
        The organization administrator name.
    :type admin_name:
        `string`
    :param admin_password:
        The organization administrator password.
    :type admin_password:
        `string`
    :param admin_email:
        The organization administrator email.
    :type admin_email:
        `string`
    :raises grpc.RpcError:
        Raised by the gRPC library to indicate non-OK-status RPC termination.

    Returns
    -------
    orgID: string
        The newly created organization ID.
    userID: string
        The newly created user ID.
    """
    with client.connect_to_server_with_no_auth() as no_auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(no_auth_conn)

        request = accounts_pb2.RegisterOrganizationRequest(orgName=org_name,
                                                           orgAddr=org_addr, userName=admin_name,
                                                           password=admin_password, email=admin_email)

        response = client_stub.RegisterOrganization(request, timeout=constants.GRPC_TIMEOUT)

        return response.orgID, response.userID


# remove_organization removes an organization
#    :returns boolean: Whether the removal was a success
def remove_organization(token, force):
    """
    Removes an organization, deleting all data stored with the organization.
    This requires an administrator priviledge.
    A gRPC connection timeout will be implemented.

    :param token: 
        The user JWT token.
    :type token:
        `string`
    :param force: 
        If this is false, removal will fail if there are still data stored with the organization.
        This prevents accidental deletion.
    :type force: 
        `bool`
    :raises grpc.RpcError:
        Raised by the gRPC library to indicate non-OK-status RPC termination.

    :returns:
        Whether the removal was a success.
    :rtype:
        `bool`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request = accounts_pb2.RemoveOrganizationRequest(force=force)

        response = client_stub.RemoveOrganization(request, timeout=constants.GRPC_TIMEOUT)

        return response.success
