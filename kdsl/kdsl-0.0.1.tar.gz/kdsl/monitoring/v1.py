from __future__ import annotations
import attr
import kdsl.monitoring.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import Any, ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class ThanosRulerSpecAlertmanagersConfig(K8sObjectBase):
    """
    | Define configuration for connecting to alertmanager.  Only available with thanos v0.10.0 and higher.  Maps to the `alertmanagers.config` arg.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArrayValueFromConfigMapKeyRef(K8sObjectBase):
    """
    | Selects a key of a ConfigMap.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArrayValueFromFieldRef(K8sObjectBase):
    """
    | Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArrayValueFromResourceFieldRef(K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArrayValueFromSecretKeyRef(K8sObjectBase):
    """
    | Selects a key of a secret in the pod's namespace
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArrayValueFrom(K8sObjectBase):
    """
    | Source for the environment variable's value. Cannot be used if value is not empty.
    
    :param configMapKeyRef: Selects a key of a ConfigMap.
    :param fieldRef: Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    :param secretKeyRef: Selects a key of a secret in the pod's namespace
    """
    configMapKeyRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromConfigMapKeyRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromConfigMapKeyRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMapKeyRef'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromFieldRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromFieldRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromResourceFieldRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})
    secretKeyRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromSecretKeyRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromSecretKeyRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secretKeyRef'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArray(K8sObjectBase):
    """
    | VolumeMount describes a mounting of a Volume within a container.
    
    :param mountPath: Path within the container at which the volume should be mounted.  Must not contain ':'.
    :param name: This must match the Name of a Volume.
    :param mountPropagation: mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.
    :param readOnly: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.
    :param subPath: Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).
    :param subPathExpr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive. This field is beta in 1.15.
    """
    mountPath: str = attr.ib(metadata={'yaml_name': 'mountPath'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    mountPropagation: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'mountPropagation'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    subPath: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'subPath'})
    subPathExpr: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'subPathExpr'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArrayConfigMapRef(K8sObjectBase):
    """
    | The ConfigMap to select from
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayArraySecretRef(K8sObjectBase):
    """
    | The Secret to select from
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePostStartExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePostStartHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePostStartHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePostStartTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePostStart(K8sObjectBase):
    """
    | PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGetTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePreStopExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePreStopHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePreStopHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePreStopTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecyclePreStop(K8sObjectBase):
    """
    | PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGetTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLifecycle(K8sObjectBase):
    """
    | Actions that the management system should take in response to container lifecycle events. Cannot be updated.
    
    :param postStart: PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    :param preStop: PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """
    postStart: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStart,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'postStart'})
    preStop: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStop,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'preStop'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLivenessProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLivenessProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLivenessProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLivenessProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayLivenessProbe(K8sObjectBase):
    """
    | Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeTcpSocketTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayReadinessProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayReadinessProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayReadinessProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayReadinessProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayReadinessProbe(K8sObjectBase):
    """
    | Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayResources(K8sObjectBase):
    """
    | Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class ThanosRulerSpecArraySecurityContextCapabilities(K8sObjectBase):
    """
    | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    
    :param add: Added capabilities
    :param drop: Removed capabilities
    """
    add: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'add'})
    drop: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'drop'})


@attr.s(kw_only=True)
class ThanosRulerSpecArraySecurityContextSeLinuxOptions(K8sObjectBase):
    """
    | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param level: Level is SELinux level label that applies to the container.
    :param role: Role is a SELinux role label that applies to the container.
    :param type: Type is a SELinux type label that applies to the container.
    :param user: User is a SELinux user label that applies to the container.
    """
    level: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'level'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class ThanosRulerSpecArraySecurityContextWindowsOptions(K8sObjectBase):
    """
    | The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is alpha-level and it is only honored by servers that enable the WindowsRunAsUserName feature flag.
    """
    gmsaCredentialSpec: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'gmsaCredentialSpec'})
    gmsaCredentialSpecName: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'gmsaCredentialSpecName'})
    runAsUserName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsUserName'})


@attr.s(kw_only=True)
class ThanosRulerSpecArraySecurityContext(K8sObjectBase):
    """
    | Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    
    :param allowPrivilegeEscalation: AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN
    :param capabilities: The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.
    :param procMount: procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.
    :param readOnlyRootFilesystem: Whether this container has a read-only root filesystem. Default is false.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param seLinuxOptions: The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    allowPrivilegeEscalation: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'allowPrivilegeEscalation'})
    capabilities: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextCapabilities,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextCapabilitiesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'capabilities'})
    privileged: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'privileged'})
    procMount: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'procMount'})
    readOnlyRootFilesystem: Optional[bool] = attr.ib(default=None, metadata
        ={'yaml_name': 'readOnlyRootFilesystem'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextSeLinuxOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'seLinuxOptions'})
    windowsOptions: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextWindowsOptions,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextWindowsOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStartupProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStartupProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStartupProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStartupProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStartupProbe(K8sObjectBase):
    """
    | StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeTcpSocketTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class ThanosRulerSpecArray(K8sObjectBase):
    """
    | Volume represents a named volume in a pod that may be accessed by any container in the pod.
    
    :param name: Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param awsElasticBlockStore: AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param azureDisk: AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    :param azureFile: AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    :param cephfs: CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    :param cinder: Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param configMap: ConfigMap represents a configMap that should populate this volume
    :param csi: CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    :param downwardAPI: DownwardAPI represents downward API about the pod that should populate this volume
    :param emptyDir: EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param fc: FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    :param flexVolume: FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    :param flocker: Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    :param gcePersistentDisk: GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param gitRepo: GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    :param glusterfs: Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    :param hostPath: HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
    :param iscsi: ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    :param nfs: NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param persistentVolumeClaim: PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param photonPersistentDisk: PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    :param portworxVolume: PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    :param projected: Items for all in one resources secrets, configmaps, and downward API
    :param quobyte: Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    :param rbd: RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    :param scaleIO: ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    :param secret: Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    :param storageos: StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    :param vsphereVolume: VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    awsElasticBlockStore: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayAwsElasticBlockStore,
        kdsl.monitoring.v1.ThanosRulerSpecArrayAwsElasticBlockStoreTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'awsElasticBlockStore'})
    azureDisk: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayAzureDisk,
        kdsl.monitoring.v1.ThanosRulerSpecArrayAzureDiskTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureDisk'})
    azureFile: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayAzureFile,
        kdsl.monitoring.v1.ThanosRulerSpecArrayAzureFileTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureFile'})
    cephfs: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCephfs,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCephfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cephfs'})
    cinder: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCinder,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCinderTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cinder'})
    configMap: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMap,
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMapTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'configMap'})
    csi: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCsi,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCsiTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'csi'})
    downwardAPI: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPI,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPITypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'downwardAPI'})
    emptyDir: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayEmptyDir,
        kdsl.monitoring.v1.ThanosRulerSpecArrayEmptyDirTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'emptyDir'})
    fc: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayFc,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFcTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'fc'})
    flexVolume: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolume,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolumeTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'flexVolume'})
    flocker: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayFlocker,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlockerTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'flocker'})
    gcePersistentDisk: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayGcePersistentDisk,
        kdsl.monitoring.v1.ThanosRulerSpecArrayGcePersistentDiskTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'gcePersistentDisk'})
    gitRepo: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayGitRepo,
        kdsl.monitoring.v1.ThanosRulerSpecArrayGitRepoTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'gitRepo'})
    glusterfs: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayGlusterfs,
        kdsl.monitoring.v1.ThanosRulerSpecArrayGlusterfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'glusterfs'})
    hostPath: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayHostPath,
        kdsl.monitoring.v1.ThanosRulerSpecArrayHostPathTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'hostPath'})
    iscsi: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayIscsi,
        kdsl.monitoring.v1.ThanosRulerSpecArrayIscsiTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'iscsi'})
    nfs: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayNfs,
        kdsl.monitoring.v1.ThanosRulerSpecArrayNfsTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'nfs'})
    persistentVolumeClaim: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayPersistentVolumeClaim,
        kdsl.monitoring.v1.ThanosRulerSpecArrayPersistentVolumeClaimTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'persistentVolumeClaim'})
    photonPersistentDisk: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayPhotonPersistentDisk,
        kdsl.monitoring.v1.ThanosRulerSpecArrayPhotonPersistentDiskTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'photonPersistentDisk'})
    portworxVolume: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayPortworxVolume,
        kdsl.monitoring.v1.ThanosRulerSpecArrayPortworxVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'portworxVolume'})
    projected: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjected,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'projected'})
    quobyte: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayQuobyte,
        kdsl.monitoring.v1.ThanosRulerSpecArrayQuobyteTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'quobyte'})
    rbd: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayRbd,
        kdsl.monitoring.v1.ThanosRulerSpecArrayRbdTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'rbd'})
    scaleIO: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIO,
        kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIOTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'scaleIO'})
    secret: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecArraySecret,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecretTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'secret'})
    storageos: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageos,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageosTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'storageos'})
    vsphereVolume: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayVsphereVolume,
        kdsl.monitoring.v1.ThanosRulerSpecArrayVsphereVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'vsphereVolume'})


@attr.s(kw_only=True)
class ThanosRulerSpecObjectStorageConfig(K8sObjectBase):
    """
    | ObjectStorageConfig configures object storage in Thanos.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecResources(K8sObjectBase):
    """
    | Resources defines the resource requirements for the Thanos sidecar. If not provided, no requests/limits will be set
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class ThanosRulerSpecRuleNamespaceSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ThanosRulerSpecRuleNamespaceSelector(K8sObjectBase):
    """
    | Namespaces to be selected for Rules discovery. If unspecified, only the same namespace as the ThanosRuler object is in is used.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelectorArray,
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ThanosRulerSpecRuleSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ThanosRulerSpecRuleSelector(K8sObjectBase):
    """
    | A label selector to select which PrometheusRules to mount for alerting and recording.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelectorArray,
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageEmptyDir(K8sObjectBase):
    """
    | EmptyDirVolumeSource to be used by the Prometheus StatefulSets. If specified, used in place of any volumeClaimTemplate. More info: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSource(K8sObjectBase):
    """
    | This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    
    :param kind: Kind is the type of resource being referenced
    :param name: Name is the name of resource being referenced
    :param apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    apiGroup: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiGroup'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateSpecResources(K8sObjectBase):
    """
    | Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArray(K8sObjectBase
    ):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateSpecSelector(K8sObjectBase):
    """
    | A label query over volumes to consider for binding.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArray
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateSpec(K8sObjectBase):
    """
    | Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param accessModes: AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param dataSource: This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    :param resources: Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    :param selector: A label query over volumes to consider for binding.
    :param storageClassName: Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
    :param volumeMode: volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. This is a beta feature.
    :param volumeName: VolumeName is the binding reference to the PersistentVolume backing this claim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    dataSource: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSource
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'dataSource'})
    resources: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecResources
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecResourcesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resources'})
    selector: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelector
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'selector'})
    storageClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageClassName'})
    volumeMode: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeMode'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateStatusArray(K8sObjectBase):
    """
    | PersistentVolumeClaimCondition contails details about state of pvc
    
    :param status: None
    :param type: PersistentVolumeClaimConditionType is a valid value of PersistentVolumeClaimCondition.Type
    :param lastProbeTime: Last time we probed the condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param message: Human-readable message indicating details about last transition.
    :param reason: Unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastProbeTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastProbeTime'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplateStatus(K8sObjectBase):
    """
    | Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param accessModes: AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param capacity: Represents the actual resources of the underlying volume.
    :param conditions: Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.
    :param phase: Phase represents the current phase of PersistentVolumeClaim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    capacity: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'capacity'})
    conditions: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatusArray
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatusArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'conditions'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorageVolumeClaimTemplate(K8sObjectBase):
    """
    | A PVC spec to be used by the Prometheus StatefulSets.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param spec: Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param status: Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Mapping[str, Any]] = attr.ib(default=None, metadata=
        {'yaml_name': 'metadata'})
    spec: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpec,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'spec'})
    status: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatus,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatusTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'status'})


@attr.s(kw_only=True)
class ThanosRulerSpecStorage(K8sObjectBase):
    """
    | Storage spec to specify how storage shall be used.
    
    :param emptyDir: EmptyDirVolumeSource to be used by the Prometheus StatefulSets. If specified, used in place of any volumeClaimTemplate. More info: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir
    :param volumeClaimTemplate: A PVC spec to be used by the Prometheus StatefulSets.
    """
    emptyDir: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageEmptyDir,
        kdsl.monitoring.v1.ThanosRulerSpecStorageEmptyDirTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'emptyDir'})
    volumeClaimTemplate: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplate,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'volumeClaimTemplate'}
        )


@attr.s(kw_only=True)
class ThanosRulerSpecTracingConfig(K8sObjectBase):
    """
    | TracingConfig configures tracing in Thanos. This is an experimental feature, it may change in any upcoming release in a breaking way.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayAwsElasticBlockStore(K8sObjectBase):
    """
    | AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    
    :param volumeID: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore TODO: how do we prevent errors in the filesystem from compromising the machine
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).
    :param readOnly: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayAzureDisk(K8sObjectBase):
    """
    | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    
    :param diskName: The Name of the data disk in the blob storage
    :param diskURI: The URI the data disk in the blob storage
    :param cachingMode: Host Caching mode: None, Read Only, Read Write.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param kind: Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    diskName: str = attr.ib(metadata={'yaml_name': 'diskName'})
    diskURI: str = attr.ib(metadata={'yaml_name': 'diskURI'})
    cachingMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'cachingMode'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayAzureFile(K8sObjectBase):
    """
    | AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    
    :param secretName: the name of secret that contains Azure Storage Account Name and Key
    :param shareName: Share Name
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})
    shareName: str = attr.ib(metadata={'yaml_name': 'shareName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayCephfsSecretRef(K8sObjectBase):
    """
    | Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayCephfs(K8sObjectBase):
    """
    | CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    
    :param monitors: Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param path: Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretFile: Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretRef: Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param user: Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretFile'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayCephfsSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCephfsSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayCinderSecretRef(K8sObjectBase):
    """
    | Optional: points to a secret object containing parameters used to connect to OpenStack.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayCinder(K8sObjectBase):
    """
    | Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    
    :param volumeID: volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param secretRef: Optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayCinderSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCinderSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayConfigMapArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayConfigMap(K8sObjectBase):
    """
    | ConfigMap represents a configMap that should populate this volume
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMapArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMapArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayCsiNodePublishSecretRef(K8sObjectBase):
    """
    | NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayCsi(K8sObjectBase):
    """
    | CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    
    :param driver: Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.
    :param fsType: Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.
    :param nodePublishSecretRef: NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    :param readOnly: Specifies a read-only configuration for the volume. Defaults to false (read/write).
    :param volumeAttributes: VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    nodePublishSecretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayCsiNodePublishSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCsiNodePublishSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'nodePublishSecretRef'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    volumeAttributes: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeAttributes'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayDownwardAPIArrayFieldRef(K8sObjectBase):
    """
    | Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRef(K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayDownwardAPIArray(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayFieldRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayDownwardAPI(K8sObjectBase):
    """
    | DownwardAPI represents downward API about the pod that should populate this volume
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: Items is a list of downward API volume file
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayEmptyDir(K8sObjectBase):
    """
    | EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayFc(K8sObjectBase):
    """
    | FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. TODO: how do we prevent errors in the filesystem from compromising the machine
    :param lun: Optional: FC target lun number
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param targetWWNs: Optional: FC target worldwide names (WWNs)
    :param wwids: Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    lun: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'lun'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    targetWWNs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'targetWWNs'})
    wwids: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'wwids'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayFlexVolumeSecretRef(K8sObjectBase):
    """
    | Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayFlexVolume(K8sObjectBase):
    """
    | FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    
    :param driver: Driver is the name of the driver to use for this volume.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    :param options: Optional: Extra command options if any.
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    options: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'options'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolumeSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolumeSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayFlocker(K8sObjectBase):
    """
    | Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    
    :param datasetName: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated
    :param datasetUUID: UUID of the dataset. This is unique identifier of a Flocker dataset
    """
    datasetName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetName'})
    datasetUUID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetUUID'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayGcePersistentDisk(K8sObjectBase):
    """
    | GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    
    :param pdName: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk TODO: how do we prevent errors in the filesystem from compromising the machine
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    pdName: str = attr.ib(metadata={'yaml_name': 'pdName'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayGitRepo(K8sObjectBase):
    """
    | GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    
    :param repository: Repository URL
    :param directory: Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.
    :param revision: Commit hash for the specified revision.
    """
    repository: str = attr.ib(metadata={'yaml_name': 'repository'})
    directory: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'directory'})
    revision: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'revision'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayGlusterfs(K8sObjectBase):
    """
    | Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    
    :param endpoints: EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param path: Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param readOnly: ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints: str = attr.ib(metadata={'yaml_name': 'endpoints'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayHostPath(K8sObjectBase):
    """
    | HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
    
    :param path: Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    :param type: Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayIscsiSecretRef(K8sObjectBase):
    """
    | CHAP Secret for iSCSI target and initiator authentication
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayIscsi(K8sObjectBase):
    """
    | ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    
    :param iqn: Target iSCSI Qualified Name.
    :param lun: iSCSI Target Lun number.
    :param targetPortal: iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param chapAuthDiscovery: whether support iSCSI Discovery CHAP authentication
    :param chapAuthSession: whether support iSCSI Session CHAP authentication
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi TODO: how do we prevent errors in the filesystem from compromising the machine
    :param initiatorName: Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    :param iscsiInterface: iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    :param portals: iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    :param secretRef: CHAP Secret for iSCSI target and initiator authentication
    """
    iqn: str = attr.ib(metadata={'yaml_name': 'iqn'})
    lun: int = attr.ib(metadata={'yaml_name': 'lun'})
    targetPortal: str = attr.ib(metadata={'yaml_name': 'targetPortal'})
    chapAuthDiscovery: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthDiscovery'})
    chapAuthSession: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthSession'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    initiatorName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'initiatorName'})
    iscsiInterface: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'iscsiInterface'})
    portals: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'portals'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayIscsiSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayIscsiSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayNfs(K8sObjectBase):
    """
    | NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    
    :param path: Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param server: Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param readOnly: ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayPersistentVolumeClaim(K8sObjectBase):
    """
    | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param claimName: ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param readOnly: Will force the ReadOnly setting in VolumeMounts. Default false.
    """
    claimName: str = attr.ib(metadata={'yaml_name': 'claimName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayPhotonPersistentDisk(K8sObjectBase):
    """
    | PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    
    :param pdID: ID that identifies Photon Controller persistent disk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    pdID: str = attr.ib(metadata={'yaml_name': 'pdID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayPortworxVolume(K8sObjectBase):
    """
    | PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    
    :param volumeID: VolumeID uniquely identifies a Portworx volume
    :param fsType: FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayConfigMapArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayConfigMap(K8sObjectBase):
    """
    | information about the configMap data to project
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMapArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMapArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRef(K8sObjectBase
    ):
    """
    | Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef(
    K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayDownwardAPIArray(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRef
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayDownwardAPI(K8sObjectBase):
    """
    | information about the downwardAPI data to project
    
    :param items: Items is a list of DownwardAPIVolume file
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArraySecretArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArraySecret(K8sObjectBase):
    """
    | information about the secret data to project
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecretArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecretArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArrayServiceAccountToken(K8sObjectBase):
    """
    | information about the serviceAccountToken data to project
    
    :param path: Path is the path relative to the mount point of the file to project the token into.
    :param audience: Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.
    :param expirationSeconds: ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    audience: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'audience'})
    expirationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'expirationSeconds'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjectedArray(K8sObjectBase):
    """
    | Projection that may be projected along with other supported volume types
    
    :param configMap: information about the configMap data to project
    :param downwardAPI: information about the downwardAPI data to project
    :param secret: information about the secret data to project
    :param serviceAccountToken: information about the serviceAccountToken data to project
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMap,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    downwardAPI: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPI,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPITypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'downwardAPI'})
    secret: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecret,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})
    serviceAccountToken: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayServiceAccountToken
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayServiceAccountTokenTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceAccountToken'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayProjected(K8sObjectBase):
    """
    | Items for all in one resources secrets, configmaps, and downward API
    
    :param sources: list of volume projections
    :param defaultMode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    sources: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'sources'})
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayQuobyte(K8sObjectBase):
    """
    | Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    
    :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes
    :param volume: Volume is a string that references an already created Quobyte volume by name.
    :param group: Group to map volume access to Default is no group
    :param readOnly: ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.
    :param tenant: Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin
    :param user: User to map volume access to Defaults to serivceaccount user
    """
    registry: str = attr.ib(metadata={'yaml_name': 'registry'})
    volume: str = attr.ib(metadata={'yaml_name': 'volume'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    tenant: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'tenant'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayRbdSecretRef(K8sObjectBase):
    """
    | SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayRbd(K8sObjectBase):
    """
    | RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    
    :param image: The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param monitors: A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd TODO: how do we prevent errors in the filesystem from compromising the machine
    :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param pool: The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param secretRef: SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param user: The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    image: str = attr.ib(metadata={'yaml_name': 'image'})
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    keyring: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyring'})
    pool: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'pool'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayRbdSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayRbdSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayScaleIOSecretRef(K8sObjectBase):
    """
    | SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayScaleIO(K8sObjectBase):
    """
    | ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    
    :param gateway: The host address of the ScaleIO API Gateway.
    :param secretRef: SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    :param system: The name of the storage system as configured in ScaleIO.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".
    :param protectionDomain: The name of the ScaleIO Protection Domain for the configured storage.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param sslEnabled: Flag to enable/disable SSL communication with Gateway, default false
    :param storageMode: Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    :param storagePool: The ScaleIO Storage Pool associated with the protection domain.
    :param volumeName: The name of a volume already created in the ScaleIO system that is associated with this volume source.
    """
    gateway: str = attr.ib(metadata={'yaml_name': 'gateway'})
    secretRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIOSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIOSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})
    system: str = attr.ib(metadata={'yaml_name': 'system'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    protectionDomain: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'protectionDomain'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    sslEnabled: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'sslEnabled'})
    storageMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageMode'})
    storagePool: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePool'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class ThanosRulerSpecArraySecretArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class ThanosRulerSpecArraySecret(K8sObjectBase):
    """
    | Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param optional: Specify whether the Secret or its keys must be defined
    :param secretName: Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecretArray,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecretArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})
    secretName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretName'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStorageosSecretRef(K8sObjectBase):
    """
    | SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayStorageos(K8sObjectBase):
    """
    | StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    :param volumeName: VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    :param volumeNamespace: VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageosSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageosSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})
    volumeNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'volumeNamespace'})


@attr.s(kw_only=True)
class ThanosRulerSpecArrayVsphereVolume(K8sObjectBase):
    """
    | VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    
    :param volumePath: Path that identifies vSphere volume vmdk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param storagePolicyID: Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.
    :param storagePolicyName: Storage Policy Based Management (SPBM) profile name.
    """
    volumePath: str = attr.ib(metadata={'yaml_name': 'volumePath'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    storagePolicyID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyID'})
    storagePolicyName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyName'})


@attr.s(kw_only=True)
class ThanosRulerSpec(K8sObjectBase):
    """
    | Specification of the desired behavior of the ThanosRuler cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    
    :param queryEndpoints: QueryEndpoints defines Thanos querier endpoints from which to query metrics. Maps to the --query flag of thanos ruler.
    :param alertDropLabels: AlertDropLabels configure the label names which should be dropped in ThanosRuler alerts. If `labels` field is not provided, `thanos_ruler_replica` will be dropped in alerts by default.
    :param alertmanagersConfig: Define configuration for connecting to alertmanager.  Only available with thanos v0.10.0 and higher.  Maps to the `alertmanagers.config` arg.
    :param alertmanagersUrl: Define URL to send alerts to alertmanager.  For Thanos v0.10.0 and higher, AlertManagersConfig should be used instead. Maps to the `alertmanagers.url` arg.
    :param containers: Containers allows injecting additional containers or modifying operator generated containers. This can be used to allow adding an authentication proxy to a ThanosRuler pod or to change the behavior of an operator generated container. Containers described here modify an operator generated container if they share the same name and modifications are done via a strategic merge patch. The current container names are: `thanos-ruler` and `rules-configmap-reloader`. Overriding containers is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice.
    :param enforcedNamespaceLabel: EnforcedNamespaceLabel enforces adding a namespace label of origin for each alert and metric that is user created. The label value will always be the namespace of the object that is being created.
    :param evaluationInterval: Interval between consecutive evaluations.
    :param image: Thanos container image URL.
    :param imagePullSecrets: An optional list of references to secrets in the same namespace to use for pulling thanos images from registries see http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod
    :param initContainers: InitContainers allows adding initContainers to the pod definition. Those can be used to e.g. fetch secrets for injection into the ThanosRuler configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ Using initContainers for any use case other then secret fetching is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice.
    :param labels: Labels configure the external label pairs to ThanosRuler. If not provided, default replica label `thanos_ruler_replica` will be added as a label and be dropped in alerts.
    :param listenLocal: ListenLocal makes the Thanos ruler listen on loopback, so that it does not bind against the Pod IP.
    :param logFormat: Log format for ThanosRuler to be configured with.
    :param logLevel: Log level for ThanosRuler to be configured with.
    :param objectStorageConfig: ObjectStorageConfig configures object storage in Thanos.
    :param paused: When a ThanosRuler deployment is paused, no actions except for deletion will be performed on the underlying objects.
    :param podMetadata: Standard object’s metadata. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata Metadata Labels and Annotations gets propagated to the prometheus pods.
    :param portName: Port name used for the pods and governing service. This defaults to web
    :param replicas: Number of thanos ruler instances to deploy.
    :param resources: Resources defines the resource requirements for the Thanos sidecar. If not provided, no requests/limits will be set
    :param retention: Time duration ThanosRuler shall retain data for. Default is '24h', and must match the regular expression `[0-9]+(ms|s|m|h|d|w|y)` (milliseconds seconds minutes hours days weeks years).
    :param ruleNamespaceSelector: Namespaces to be selected for Rules discovery. If unspecified, only the same namespace as the ThanosRuler object is in is used.
    :param ruleSelector: A label selector to select which PrometheusRules to mount for alerting and recording.
    :param storage: Storage spec to specify how storage shall be used.
    :param tracingConfig: TracingConfig configures tracing in Thanos. This is an experimental feature, it may change in any upcoming release in a breaking way.
    :param volumes: Volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects.
    """
    queryEndpoints: Sequence[str] = attr.ib(metadata={'yaml_name':
        'queryEndpoints'})
    alertDropLabels: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'alertDropLabels'})
    alertmanagersConfig: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecAlertmanagersConfig,
        kdsl.monitoring.v1.ThanosRulerSpecAlertmanagersConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'alertmanagersConfig'}
        )
    alertmanagersUrl: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'alertmanagersUrl'})
    containers: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'containers'})
    enforcedNamespaceLabel: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'enforcedNamespaceLabel'})
    evaluationInterval: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'evaluationInterval'})
    image: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'image'})
    imagePullSecrets: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'imagePullSecrets'})
    initContainers: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'initContainers'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'labels'})
    listenLocal: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'listenLocal'})
    logFormat: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'logFormat'})
    logLevel: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'logLevel'})
    objectStorageConfig: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecObjectStorageConfig,
        kdsl.monitoring.v1.ThanosRulerSpecObjectStorageConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'objectStorageConfig'}
        )
    paused: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'paused'})
    podMetadata: Optional[Mapping[str, Any]] = attr.ib(default=None,
        metadata={'yaml_name': 'podMetadata'})
    portName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'portName'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    resources: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecResources,
        kdsl.monitoring.v1.ThanosRulerSpecResourcesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resources'})
    retention: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'retention'})
    ruleNamespaceSelector: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelector,
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'ruleNamespaceSelector'})
    ruleSelector: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelector,
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelectorTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'ruleSelector'})
    storage: Optional[Union[kdsl.monitoring.v1.ThanosRulerSpecStorage,
        kdsl.monitoring.v1.ThanosRulerSpecStorageTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'storage'})
    tracingConfig: Optional[Union[
        kdsl.monitoring.v1.ThanosRulerSpecTracingConfig,
        kdsl.monitoring.v1.ThanosRulerSpecTracingConfigTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'tracingConfig'})
    volumes: Optional[Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'volumes'})


@attr.s(kw_only=True)
class ThanosRuler(K8sResourceBase):
    """
    | ThanosRuler defines a ThanosRuler deployment.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Specification of the desired behavior of the ThanosRuler cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'monitoring.coreos.com/v1'
    kind: ClassVar[str] = 'ThanosRuler'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.monitoring.v1.ThanosRulerSpec,
        kdsl.monitoring.v1.ThanosRulerSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayBasicAuthPassword(K8sObjectBase):
    """
    | The secret in the service monitor namespace that contains the password for authentication.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayBasicAuthUsername(K8sObjectBase):
    """
    | The secret in the service monitor namespace that contains the username for authentication.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayBasicAuth(K8sObjectBase):
    """
    | BasicAuth allow an endpoint to authenticate over basic authentication More info: https://prometheus.io/docs/operating/configuration/#endpoints
    
    :param password: The secret in the service monitor namespace that contains the password for authentication.
    :param username: The secret in the service monitor namespace that contains the username for authentication.
    """
    password: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthPassword,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthPasswordTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'password'})
    username: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthUsername,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthUsernameTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'username'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayBearerTokenSecret(K8sObjectBase):
    """
    | Secret to mount to read bearer token for scraping targets. The secret needs to be in the same namespace as the service monitor and accessible by the Prometheus Operator.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayArray(K8sObjectBase):
    """
    | RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion. It defines `<metric_relabel_configs>`-section of Prometheus configuration. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs
    
    :param action: Action to perform based on regex matching. Default is 'replace'
    :param modulus: Modulus to take of the hash of the source label values.
    :param regex: Regular expression against which the extracted value is matched. Default is '(.*)'
    :param replacement: Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1'
    :param separator: Separator placed between concatenated source label values. default is ';'.
    :param sourceLabels: The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.
    :param targetLabel: Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.
    """
    action: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'action'})
    modulus: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'modulus'})
    regex: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'regex'})
    replacement: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'replacement'})
    separator: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'separator'})
    sourceLabels: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'sourceLabels'})
    targetLabel: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'targetLabel'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigCaConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigCaSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigCa(K8sObjectBase):
    """
    | Stuct containing the CA cert to use for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaConfigMap,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaSecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaSecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigCertConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigCertSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigCert(K8sObjectBase):
    """
    | Struct containing the client cert file for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertConfigMap,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertSecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertSecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfigKeySecret(K8sObjectBase):
    """
    | Secret containing the client key file for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArrayTlsConfig(K8sObjectBase):
    """
    | TLS configuration to use when scraping the endpoint
    
    :param ca: Stuct containing the CA cert to use for the targets.
    :param caFile: Path to the CA cert in the Prometheus container to use for the targets.
    :param cert: Struct containing the client cert file for the targets.
    :param certFile: Path to the client cert file in the Prometheus container for the targets.
    :param insecureSkipVerify: Disable target certificate validation.
    :param keyFile: Path to the client key file in the Prometheus container for the targets.
    :param keySecret: Secret containing the client key file for the targets.
    :param serverName: Used to verify the hostname for the targets.
    """
    ca: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCa,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'ca'})
    caFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caFile'})
    cert: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCert,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cert'})
    certFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'certFile'})
    insecureSkipVerify: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'insecureSkipVerify'})
    keyFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyFile'})
    keySecret: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigKeySecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigKeySecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'keySecret'})
    serverName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'serverName'})


@attr.s(kw_only=True)
class ServiceMonitorSpecArray(K8sObjectBase):
    """
    | Endpoint defines a scrapeable endpoint serving Prometheus metrics.
    
    :param basicAuth: BasicAuth allow an endpoint to authenticate over basic authentication More info: https://prometheus.io/docs/operating/configuration/#endpoints
    :param bearerTokenFile: File to read bearer token for scraping targets.
    :param bearerTokenSecret: Secret to mount to read bearer token for scraping targets. The secret needs to be in the same namespace as the service monitor and accessible by the Prometheus Operator.
    :param honorLabels: HonorLabels chooses the metric's labels on collisions with target labels.
    :param honorTimestamps: HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data.
    :param interval: Interval at which metrics should be scraped
    :param metricRelabelings: MetricRelabelConfigs to apply to samples before ingestion.
    :param params: Optional HTTP URL parameters
    :param path: HTTP path to scrape for metrics.
    :param port: Name of the service port this endpoint refers to. Mutually exclusive with targetPort.
    :param proxyUrl: ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint.
    :param relabelings: RelabelConfigs to apply to samples before scraping. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config
    :param scheme: HTTP scheme to use for scraping.
    :param scrapeTimeout: Timeout after which the scrape is ended
    :param targetPort: Name or number of the target port of the endpoint. Mutually exclusive with port.
    :param tlsConfig: TLS configuration to use when scraping the endpoint
    """
    basicAuth: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuth,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'basicAuth'})
    bearerTokenFile: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'bearerTokenFile'})
    bearerTokenSecret: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBearerTokenSecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBearerTokenSecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'bearerTokenSecret'})
    honorLabels: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'honorLabels'})
    honorTimestamps: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'honorTimestamps'})
    interval: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'interval'})
    metricRelabelings: Optional[Sequence[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArray,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'metricRelabelings'})
    params: Optional[Mapping[str, Sequence[str]]] = attr.ib(default=None,
        metadata={'yaml_name': 'params'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    port: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'port'})
    proxyUrl: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'proxyUrl'})
    relabelings: Optional[Sequence[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArray,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'relabelings'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})
    scrapeTimeout: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'scrapeTimeout'})
    targetPort: Optional[Any] = attr.ib(default=None, metadata={'yaml_name':
        'targetPort'})
    tlsConfig: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfig,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tlsConfig'})


@attr.s(kw_only=True)
class ServiceMonitorSpecNamespaceSelector(K8sObjectBase):
    """
    | Selector to select which namespaces the Endpoints objects are discovered from.
    
    :param any: Boolean describing whether all namespaces are selected in contrast to a list restricting them.
    :param matchNames: List of namespace names.
    """
    any: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'any'})
    matchNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'matchNames'})


@attr.s(kw_only=True)
class ServiceMonitorSpecSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ServiceMonitorSpecSelector(K8sObjectBase):
    """
    | Selector to select Endpoints objects.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecSelectorArray,
        kdsl.monitoring.v1.ServiceMonitorSpecSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ServiceMonitorSpec(K8sObjectBase):
    """
    | Specification of desired Service selection for target discovery by Prometheus.
    
    :param endpoints: A list of endpoints allowed as part of this ServiceMonitor.
    :param selector: Selector to select Endpoints objects.
    :param jobLabel: The label to use to retrieve the job name from.
    :param namespaceSelector: Selector to select which namespaces the Endpoints objects are discovered from.
    :param podTargetLabels: PodTargetLabels transfers labels on the Kubernetes Pod onto the target.
    :param sampleLimit: SampleLimit defines per-scrape limit on number of scraped samples that will be accepted.
    :param targetLabels: TargetLabels transfers labels on the Kubernetes Service onto the target.
    """
    endpoints: Sequence[Union[kdsl.monitoring.v1.ServiceMonitorSpecArray,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTypedDict]] = attr.ib(
        metadata={'yaml_name': 'endpoints'})
    selector: Union[kdsl.monitoring.v1.ServiceMonitorSpecSelector,
        kdsl.monitoring.v1.ServiceMonitorSpecSelectorTypedDict] = attr.ib(
        metadata={'yaml_name': 'selector'})
    jobLabel: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'jobLabel'})
    namespaceSelector: Optional[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecNamespaceSelector,
        kdsl.monitoring.v1.ServiceMonitorSpecNamespaceSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'namespaceSelector'})
    podTargetLabels: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'podTargetLabels'})
    sampleLimit: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'sampleLimit'})
    targetLabels: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'targetLabels'})


@attr.s(kw_only=True)
class ServiceMonitor(K8sResourceBase):
    """
    | ServiceMonitor defines monitoring for a set of services.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Specification of desired Service selection for target discovery by Prometheus.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'monitoring.coreos.com/v1'
    kind: ClassVar[str] = 'ServiceMonitor'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.monitoring.v1.ServiceMonitorSpec,
        kdsl.monitoring.v1.ServiceMonitorSpecTypedDict] = attr.ib(metadata=
        {'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class PrometheusRuleSpecArrayArray(K8sObjectBase):
    """
    | Rule describes an alerting or recording rule.
    
    :param expr: None
    :param alert: None
    :param annotations: None
    :param for_: None
    :param labels: None
    :param record: None
    """
    expr: Any = attr.ib(metadata={'yaml_name': 'expr'})
    alert: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'alert'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'annotations'})
    for_: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'for'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'labels'})
    record: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'record'})


@attr.s(kw_only=True)
class PrometheusRuleSpecArray(K8sObjectBase):
    """
    | RuleGroup is a list of sequentially evaluated recording and alerting rules. Note: PartialResponseStrategy is only used by ThanosRuler and will be ignored by Prometheus instances.  Valid values for this field are 'warn' or 'abort'.  More info: https://github.com/thanos-io/thanos/blob/master/docs/components/rule.md#partial-response
    
    :param name: None
    :param rules: None
    :param interval: None
    :param partial_response_strategy: None
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    rules: Sequence[Union[kdsl.monitoring.v1.PrometheusRuleSpecArrayArray,
        kdsl.monitoring.v1.PrometheusRuleSpecArrayArrayTypedDict]] = attr.ib(
        metadata={'yaml_name': 'rules'})
    interval: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'interval'})
    partial_response_strategy: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'partial_response_strategy'})


@attr.s(kw_only=True)
class PrometheusRuleSpec(K8sObjectBase):
    """
    | Specification of desired alerting rule definitions for Prometheus.
    
    :param groups: Content of Prometheus rule file
    """
    groups: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusRuleSpecArray,
        kdsl.monitoring.v1.PrometheusRuleSpecArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'groups'})


@attr.s(kw_only=True)
class PrometheusRule(K8sResourceBase):
    """
    | PrometheusRule defines alerting rules for a Prometheus instance
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Specification of desired alerting rule definitions for Prometheus.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'monitoring.coreos.com/v1'
    kind: ClassVar[str] = 'PrometheusRule'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.monitoring.v1.PrometheusRuleSpec,
        kdsl.monitoring.v1.PrometheusRuleSpecTypedDict] = attr.ib(metadata=
        {'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class PrometheusSpecAdditionalAlertManagerConfigs(K8sObjectBase):
    """
    | AdditionalAlertManagerConfigs allows specifying a key of a Secret containing additional Prometheus AlertManager configurations. AlertManager configurations specified are appended to the configurations generated by the Prometheus Operator. Job configurations specified must have the form as specified in the official Prometheus documentation: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config. As AlertManager configs are appended, the user is responsible to make sure it is valid. Note that using this feature may expose the possibility to break upgrades of Prometheus. It is advised to review Prometheus release notes to ensure that no incompatible AlertManager configs are going to break Prometheus after the upgrade.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAdditionalAlertRelabelConfigs(K8sObjectBase):
    """
    | AdditionalAlertRelabelConfigs allows specifying a key of a Secret containing additional Prometheus alert relabel configurations. Alert relabel configurations specified are appended to the configurations generated by the Prometheus Operator. Alert relabel configurations specified must have the form as specified in the official Prometheus documentation: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs. As alert relabel configs are appended, the user is responsible to make sure it is valid. Note that using this feature may expose the possibility to break upgrades of Prometheus. It is advised to review Prometheus release notes to ensure that no incompatible alert relabel configs are going to break Prometheus after the upgrade.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAdditionalScrapeConfigs(K8sObjectBase):
    """
    | AdditionalScrapeConfigs allows specifying a key of a Secret containing additional Prometheus scrape configurations. Scrape configurations specified are appended to the configurations generated by the Prometheus Operator. Job configurations specified must have the form as specified in the official Prometheus documentation: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config. As scrape configs are appended, the user is responsible to make sure it is valid. Note that using this feature may expose the possibility to break upgrades of Prometheus. It is advised to review Prometheus release notes to ensure that no incompatible scrape configs are going to break Prometheus after the upgrade.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinityArrayPreferenceArray(K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinityArrayPreference(K8sObjectBase):
    """
    | A node selector term, associated with the corresponding weight.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinityArray(K8sObjectBase):
    """
    | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    
    :param preference: A node selector term, associated with the corresponding weight.
    :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """
    preference: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreference,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'preference'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray(
    K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray(
    K8sObjectBase):
    """
    | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(
    K8sObjectBase):
    """
    | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    
    :param nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.
    """
    nodeSelectorTerms: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]] = attr.ib(metadata={'yaml_name': 'nodeSelectorTerms'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityNodeAffinity(K8sObjectBase):
    """
    | Describes node affinity scheduling rules for the pod.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinityArrayPodAffinityTerm(K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinityArray(K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelector,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinityArrayLabelSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinityArrayLabelSelector(K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAffinity(K8sObjectBase):
    """
    | Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTerm(K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinityArray(K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArray(
    K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinityArrayLabelSelector(K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecAffinityPodAntiAffinity(K8sObjectBase):
    """
    | Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class PrometheusSpecAffinity(K8sObjectBase):
    """
    | If specified, the pod's scheduling constraints.
    
    :param nodeAffinity: Describes node affinity scheduling rules for the pod.
    :param podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    :param podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """
    nodeAffinity: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'nodeAffinity'})
    podAffinity: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'podAffinity'})
    podAntiAffinity: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'podAntiAffinity'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigCaConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigCaSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigCa(K8sObjectBase):
    """
    | Stuct containing the CA cert to use for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaConfigMap,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaSecret,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaSecretTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigCertConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigCertSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigCert(K8sObjectBase):
    """
    | Struct containing the client cert file for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertConfigMap,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertSecret,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertSecretTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfigKeySecret(K8sObjectBase):
    """
    | Secret containing the client key file for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArrayTlsConfig(K8sObjectBase):
    """
    | TLS Config to use for alertmanager connection.
    
    :param ca: Stuct containing the CA cert to use for the targets.
    :param caFile: Path to the CA cert in the Prometheus container to use for the targets.
    :param cert: Struct containing the client cert file for the targets.
    :param certFile: Path to the client cert file in the Prometheus container for the targets.
    :param insecureSkipVerify: Disable target certificate validation.
    :param keyFile: Path to the client key file in the Prometheus container for the targets.
    :param keySecret: Secret containing the client key file for the targets.
    :param serverName: Used to verify the hostname for the targets.
    """
    ca: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCa,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'ca'})
    caFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caFile'})
    cert: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCert,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cert'})
    certFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'certFile'})
    insecureSkipVerify: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'insecureSkipVerify'})
    keyFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyFile'})
    keySecret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigKeySecret,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigKeySecretTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'keySecret'})
    serverName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'serverName'})


@attr.s(kw_only=True)
class PrometheusSpecAlertingArray(K8sObjectBase):
    """
    | AlertmanagerEndpoints defines a selection of a single Endpoints object containing alertmanager IPs to fire alerts against.
    
    :param name: Name of Endpoints object in Namespace.
    :param namespace: Namespace of Endpoints object.
    :param port: Port the Alertmanager API is exposed on.
    :param apiVersion: Version of the Alertmanager API that Prometheus uses to send alerts. It can be "v1" or "v2".
    :param bearerTokenFile: BearerTokenFile to read from filesystem to use when authenticating to Alertmanager.
    :param pathPrefix: Prefix for the HTTP path alerts are pushed to.
    :param scheme: Scheme to use when firing alerts.
    :param tlsConfig: TLS Config to use for alertmanager connection.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    namespace: str = attr.ib(metadata={'yaml_name': 'namespace'})
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    bearerTokenFile: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'bearerTokenFile'})
    pathPrefix: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'pathPrefix'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})
    tlsConfig: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfig,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tlsConfig'})


@attr.s(kw_only=True)
class PrometheusSpecAlerting(K8sObjectBase):
    """
    | Define details regarding alerting.
    
    :param alertmanagers: AlertmanagerEndpoints Prometheus should fire alerts against.
    """
    alertmanagers: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArray,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTypedDict]] = attr.ib(
        metadata={'yaml_name': 'alertmanagers'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigBasicAuthPassword(K8sObjectBase):
    """
    | The secret in the service monitor namespace that contains the password for authentication.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigBasicAuthUsername(K8sObjectBase):
    """
    | The secret in the service monitor namespace that contains the username for authentication.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigBasicAuth(K8sObjectBase):
    """
    | BasicAuth allow an endpoint to authenticate over basic authentication
    
    :param password: The secret in the service monitor namespace that contains the password for authentication.
    :param username: The secret in the service monitor namespace that contains the username for authentication.
    """
    password: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthPassword,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthPasswordTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'password'})
    username: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthUsername,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthUsernameTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'username'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigCaConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigCaSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigCa(K8sObjectBase):
    """
    | Stuct containing the CA cert to use for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaConfigMap,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaSecret,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaSecretTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigCertConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigCertSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigCert(K8sObjectBase):
    """
    | Struct containing the client cert file for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertConfigMap,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertSecret,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertSecretTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfigKeySecret(K8sObjectBase):
    """
    | Secret containing the client key file for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfigTlsConfig(K8sObjectBase):
    """
    | TLS Config to use for accessing apiserver.
    
    :param ca: Stuct containing the CA cert to use for the targets.
    :param caFile: Path to the CA cert in the Prometheus container to use for the targets.
    :param cert: Struct containing the client cert file for the targets.
    :param certFile: Path to the client cert file in the Prometheus container for the targets.
    :param insecureSkipVerify: Disable target certificate validation.
    :param keyFile: Path to the client key file in the Prometheus container for the targets.
    :param keySecret: Secret containing the client key file for the targets.
    :param serverName: Used to verify the hostname for the targets.
    """
    ca: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCa,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'ca'})
    caFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caFile'})
    cert: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCert,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cert'})
    certFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'certFile'})
    insecureSkipVerify: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'insecureSkipVerify'})
    keyFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyFile'})
    keySecret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigKeySecret,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigKeySecretTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'keySecret'})
    serverName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'serverName'})


@attr.s(kw_only=True)
class PrometheusSpecApiserverConfig(K8sObjectBase):
    """
    | APIServerConfig allows specifying a host and auth methods to access apiserver. If left empty, Prometheus is assumed to run inside of the cluster and will discover API servers automatically and use the pod's CA certificate and bearer token file at /var/run/secrets/kubernetes.io/serviceaccount/.
    
    :param host: Host of apiserver. A valid string consisting of a hostname or IP followed by an optional port number
    :param basicAuth: BasicAuth allow an endpoint to authenticate over basic authentication
    :param bearerToken: Bearer token for accessing apiserver.
    :param bearerTokenFile: File to read bearer token for accessing apiserver.
    :param tlsConfig: TLS Config to use for accessing apiserver.
    """
    host: str = attr.ib(metadata={'yaml_name': 'host'})
    basicAuth: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuth,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'basicAuth'})
    bearerToken: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'bearerToken'})
    bearerTokenFile: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'bearerTokenFile'})
    tlsConfig: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfig,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tlsConfig'})


@attr.s(kw_only=True)
class PrometheusSpecArbitraryFSAccessThroughSMs(K8sObjectBase):
    """
    | ArbitraryFSAccessThroughSMs configures whether configuration based on a service monitor can access arbitrary files on the file system of the Prometheus container e.g. bearer token files.
    
    :param deny: None
    """
    deny: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'deny'}
        )


@attr.s(kw_only=True)
class PrometheusSpecArrayArrayValueFromConfigMapKeyRef(K8sObjectBase):
    """
    | Selects a key of a ConfigMap.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArrayValueFromFieldRef(K8sObjectBase):
    """
    | Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArrayValueFromResourceFieldRef(K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArrayValueFromSecretKeyRef(K8sObjectBase):
    """
    | Selects a key of a secret in the pod's namespace
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArrayValueFrom(K8sObjectBase):
    """
    | Source for the environment variable's value. Cannot be used if value is not empty.
    
    :param configMapKeyRef: Selects a key of a ConfigMap.
    :param fieldRef: Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    :param secretKeyRef: Selects a key of a secret in the pod's namespace
    """
    configMapKeyRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromConfigMapKeyRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromConfigMapKeyRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMapKeyRef'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromFieldRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromResourceFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})
    secretKeyRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromSecretKeyRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromSecretKeyRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secretKeyRef'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArray(K8sObjectBase):
    """
    | RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion. It defines `<metric_relabel_configs>`-section of Prometheus configuration. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs
    
    :param action: Action to perform based on regex matching. Default is 'replace'
    :param modulus: Modulus to take of the hash of the source label values.
    :param regex: Regular expression against which the extracted value is matched. Default is '(.*)'
    :param replacement: Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1'
    :param separator: Separator placed between concatenated source label values. default is ';'.
    :param sourceLabels: The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.
    :param targetLabel: Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.
    """
    action: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'action'})
    modulus: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'modulus'})
    regex: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'regex'})
    replacement: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'replacement'})
    separator: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'separator'})
    sourceLabels: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'sourceLabels'})
    targetLabel: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'targetLabel'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArrayConfigMapRef(K8sObjectBase):
    """
    | The ConfigMap to select from
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayArraySecretRef(K8sObjectBase):
    """
    | The Secret to select from
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePostStartExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePostStartHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePostStartHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePostStartTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePostStart(K8sObjectBase):
    """
    | PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartExec,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGetTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePreStopExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePreStopHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePreStopHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePreStopTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecyclePreStop(K8sObjectBase):
    """
    | PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopExec,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLifecycle(K8sObjectBase):
    """
    | Actions that the management system should take in response to container lifecycle events. Cannot be updated.
    
    :param postStart: PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    :param preStop: PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """
    postStart: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStart,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'postStart'})
    preStop: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStop,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'preStop'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLivenessProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLivenessProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLivenessProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLivenessProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class PrometheusSpecArrayLivenessProbe(K8sObjectBase):
    """
    | Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeExec,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeTcpSocketTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class PrometheusSpecArrayReadinessProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class PrometheusSpecArrayReadinessProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class PrometheusSpecArrayReadinessProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class PrometheusSpecArrayReadinessProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class PrometheusSpecArrayReadinessProbe(K8sObjectBase):
    """
    | Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeExec,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeTcpSocketTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class PrometheusSpecArrayResources(K8sObjectBase):
    """
    | Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class PrometheusSpecArraySecurityContextCapabilities(K8sObjectBase):
    """
    | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    
    :param add: Added capabilities
    :param drop: Removed capabilities
    """
    add: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'add'})
    drop: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'drop'})


@attr.s(kw_only=True)
class PrometheusSpecArraySecurityContextSeLinuxOptions(K8sObjectBase):
    """
    | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param level: Level is SELinux level label that applies to the container.
    :param role: Role is a SELinux role label that applies to the container.
    :param type: Type is a SELinux type label that applies to the container.
    :param user: User is a SELinux user label that applies to the container.
    """
    level: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'level'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class PrometheusSpecArraySecurityContextWindowsOptions(K8sObjectBase):
    """
    | The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is alpha-level and it is only honored by servers that enable the WindowsRunAsUserName feature flag.
    """
    gmsaCredentialSpec: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'gmsaCredentialSpec'})
    gmsaCredentialSpecName: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'gmsaCredentialSpecName'})
    runAsUserName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsUserName'})


@attr.s(kw_only=True)
class PrometheusSpecArraySecurityContext(K8sObjectBase):
    """
    | Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    
    :param allowPrivilegeEscalation: AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN
    :param capabilities: The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.
    :param procMount: procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.
    :param readOnlyRootFilesystem: Whether this container has a read-only root filesystem. Default is false.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param seLinuxOptions: The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    allowPrivilegeEscalation: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'allowPrivilegeEscalation'})
    capabilities: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextCapabilities,
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextCapabilitiesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'capabilities'})
    privileged: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'privileged'})
    procMount: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'procMount'})
    readOnlyRootFilesystem: Optional[bool] = attr.ib(default=None, metadata
        ={'yaml_name': 'readOnlyRootFilesystem'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextSeLinuxOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'seLinuxOptions'})
    windowsOptions: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextWindowsOptions,
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextWindowsOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStartupProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStartupProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStartupProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStartupProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStartupProbe(K8sObjectBase):
    """
    | StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeExec,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeTcpSocketTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class PrometheusSpecArray(K8sObjectBase):
    """
    | Volume represents a named volume in a pod that may be accessed by any container in the pod.
    
    :param name: Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param awsElasticBlockStore: AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param azureDisk: AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    :param azureFile: AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    :param cephfs: CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    :param cinder: Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param configMap: ConfigMap represents a configMap that should populate this volume
    :param csi: CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    :param downwardAPI: DownwardAPI represents downward API about the pod that should populate this volume
    :param emptyDir: EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param fc: FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    :param flexVolume: FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    :param flocker: Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    :param gcePersistentDisk: GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param gitRepo: GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    :param glusterfs: Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    :param hostPath: HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
    :param iscsi: ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    :param nfs: NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param persistentVolumeClaim: PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param photonPersistentDisk: PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    :param portworxVolume: PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    :param projected: Items for all in one resources secrets, configmaps, and downward API
    :param quobyte: Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    :param rbd: RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    :param scaleIO: ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    :param secret: Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    :param storageos: StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    :param vsphereVolume: VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    awsElasticBlockStore: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayAwsElasticBlockStore,
        kdsl.monitoring.v1.PrometheusSpecArrayAwsElasticBlockStoreTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'awsElasticBlockStore'})
    azureDisk: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayAzureDisk,
        kdsl.monitoring.v1.PrometheusSpecArrayAzureDiskTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureDisk'})
    azureFile: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayAzureFile,
        kdsl.monitoring.v1.PrometheusSpecArrayAzureFileTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureFile'})
    cephfs: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayCephfs,
        kdsl.monitoring.v1.PrometheusSpecArrayCephfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cephfs'})
    cinder: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayCinder,
        kdsl.monitoring.v1.PrometheusSpecArrayCinderTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cinder'})
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMapTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'configMap'})
    csi: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayCsi,
        kdsl.monitoring.v1.PrometheusSpecArrayCsiTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'csi'})
    downwardAPI: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPI,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPITypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'downwardAPI'})
    emptyDir: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayEmptyDir,
        kdsl.monitoring.v1.PrometheusSpecArrayEmptyDirTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'emptyDir'})
    fc: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayFc,
        kdsl.monitoring.v1.PrometheusSpecArrayFcTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'fc'})
    flexVolume: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolume,
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolumeTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'flexVolume'})
    flocker: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayFlocker,
        kdsl.monitoring.v1.PrometheusSpecArrayFlockerTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'flocker'})
    gcePersistentDisk: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayGcePersistentDisk,
        kdsl.monitoring.v1.PrometheusSpecArrayGcePersistentDiskTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'gcePersistentDisk'})
    gitRepo: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayGitRepo,
        kdsl.monitoring.v1.PrometheusSpecArrayGitRepoTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'gitRepo'})
    glusterfs: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayGlusterfs,
        kdsl.monitoring.v1.PrometheusSpecArrayGlusterfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'glusterfs'})
    hostPath: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayHostPath,
        kdsl.monitoring.v1.PrometheusSpecArrayHostPathTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'hostPath'})
    iscsi: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayIscsi,
        kdsl.monitoring.v1.PrometheusSpecArrayIscsiTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'iscsi'})
    nfs: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayNfs,
        kdsl.monitoring.v1.PrometheusSpecArrayNfsTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'nfs'})
    persistentVolumeClaim: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayPersistentVolumeClaim,
        kdsl.monitoring.v1.PrometheusSpecArrayPersistentVolumeClaimTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'persistentVolumeClaim'})
    photonPersistentDisk: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayPhotonPersistentDisk,
        kdsl.monitoring.v1.PrometheusSpecArrayPhotonPersistentDiskTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'photonPersistentDisk'})
    portworxVolume: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayPortworxVolume,
        kdsl.monitoring.v1.PrometheusSpecArrayPortworxVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'portworxVolume'})
    projected: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjected,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'projected'})
    quobyte: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayQuobyte,
        kdsl.monitoring.v1.PrometheusSpecArrayQuobyteTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'quobyte'})
    rbd: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayRbd,
        kdsl.monitoring.v1.PrometheusSpecArrayRbdTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'rbd'})
    scaleIO: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayScaleIO,
        kdsl.monitoring.v1.PrometheusSpecArrayScaleIOTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'scaleIO'})
    secret: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArraySecret,
        kdsl.monitoring.v1.PrometheusSpecArraySecretTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'secret'})
    storageos: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStorageos,
        kdsl.monitoring.v1.PrometheusSpecArrayStorageosTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'storageos'})
    vsphereVolume: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayVsphereVolume,
        kdsl.monitoring.v1.PrometheusSpecArrayVsphereVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'vsphereVolume'})


@attr.s(kw_only=True)
class PrometheusSpecPodMonitorNamespaceSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecPodMonitorNamespaceSelector(K8sObjectBase):
    """
    | Namespaces to be selected for PodMonitor discovery. If nil, only check own namespace.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecPodMonitorSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecPodMonitorSelector(K8sObjectBase):
    """
    | *Experimental* PodMonitors to be selected for target discovery.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecQuery(K8sObjectBase):
    """
    | QuerySpec defines the query command line flags when starting Prometheus.
    
    :param lookbackDelta: The delta difference allowed for retrieving metrics during expression evaluations.
    :param maxConcurrency: Number of concurrent queries that can be run at once.
    :param maxSamples: Maximum number of samples a single query can load into memory. Note that queries will fail if they would load more samples than this into memory, so this also limits the number of samples a query can return.
    :param timeout: Maximum time a query may take before being aborted.
    """
    lookbackDelta: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lookbackDelta'})
    maxConcurrency: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'maxConcurrency'})
    maxSamples: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'maxSamples'})
    timeout: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'timeout'})


@attr.s(kw_only=True)
class PrometheusSpecArrayBasicAuthPassword(K8sObjectBase):
    """
    | The secret in the service monitor namespace that contains the password for authentication.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayBasicAuthUsername(K8sObjectBase):
    """
    | The secret in the service monitor namespace that contains the username for authentication.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayBasicAuth(K8sObjectBase):
    """
    | BasicAuth for the URL.
    
    :param password: The secret in the service monitor namespace that contains the password for authentication.
    :param username: The secret in the service monitor namespace that contains the username for authentication.
    """
    password: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthPassword,
        kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthPasswordTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'password'})
    username: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthUsername,
        kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthUsernameTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'username'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigCaConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigCaSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigCa(K8sObjectBase):
    """
    | Stuct containing the CA cert to use for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaConfigMapTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaSecret,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaSecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigCertConfigMap(K8sObjectBase):
    """
    | ConfigMap containing data to use for the targets.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigCertSecret(K8sObjectBase):
    """
    | Secret containing data to use for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigCert(K8sObjectBase):
    """
    | Struct containing the client cert file for the targets.
    
    :param configMap: ConfigMap containing data to use for the targets.
    :param secret: Secret containing data to use for the targets.
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertConfigMapTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertSecret,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertSecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfigKeySecret(K8sObjectBase):
    """
    | Secret containing the client key file for the targets.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayTlsConfig(K8sObjectBase):
    """
    | TLS Config to use for remote write.
    
    :param ca: Stuct containing the CA cert to use for the targets.
    :param caFile: Path to the CA cert in the Prometheus container to use for the targets.
    :param cert: Struct containing the client cert file for the targets.
    :param certFile: Path to the client cert file in the Prometheus container for the targets.
    :param insecureSkipVerify: Disable target certificate validation.
    :param keyFile: Path to the client key file in the Prometheus container for the targets.
    :param keySecret: Secret containing the client key file for the targets.
    :param serverName: Used to verify the hostname for the targets.
    """
    ca: Optional[Union[kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCa,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'ca'})
    caFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caFile'})
    cert: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCert,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cert'})
    certFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'certFile'})
    insecureSkipVerify: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'insecureSkipVerify'})
    keyFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyFile'})
    keySecret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigKeySecret,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigKeySecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'keySecret'})
    serverName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'serverName'})


@attr.s(kw_only=True)
class PrometheusSpecArrayQueueConfig(K8sObjectBase):
    """
    | QueueConfig allows tuning of the remote write queue parameters.
    
    :param batchSendDeadline: BatchSendDeadline is the maximum time a sample will wait in buffer.
    :param capacity: Capacity is the number of samples to buffer per shard before we start dropping them.
    :param maxBackoff: MaxBackoff is the maximum retry delay.
    :param maxRetries: MaxRetries is the maximum number of times to retry a batch on recoverable errors.
    :param maxSamplesPerSend: MaxSamplesPerSend is the maximum number of samples per send.
    :param maxShards: MaxShards is the maximum number of shards, i.e. amount of concurrency.
    :param minBackoff: MinBackoff is the initial retry delay. Gets doubled for every retry.
    :param minShards: MinShards is the minimum number of shards, i.e. amount of concurrency.
    """
    batchSendDeadline: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'batchSendDeadline'})
    capacity: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'capacity'})
    maxBackoff: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'maxBackoff'})
    maxRetries: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'maxRetries'})
    maxSamplesPerSend: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'maxSamplesPerSend'})
    maxShards: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'maxShards'})
    minBackoff: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'minBackoff'})
    minShards: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'minShards'})


@attr.s(kw_only=True)
class PrometheusSpecResources(K8sObjectBase):
    """
    | Define resources requests and limits for single Pods.
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class PrometheusSpecRuleNamespaceSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecRuleNamespaceSelector(K8sObjectBase):
    """
    | Namespaces to be selected for PrometheusRules discovery. If unspecified, only the same namespace as the Prometheus object is in is used.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecRuleSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecRuleSelector(K8sObjectBase):
    """
    | A selector to select which PrometheusRules to mount for loading alerting rules from. Until (excluding) Prometheus Operator v0.24.0 Prometheus Operator will migrate any legacy rule ConfigMaps to PrometheusRule custom resources selected by RuleSelector. Make sure it does not match any config maps that you do not want to be migrated.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecRuleSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecRuleSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecRulesAlert(K8sObjectBase):
    """
    | /--rules.alert.*/ command-line arguments
    
    :param forGracePeriod: Minimum duration between alert and restored 'for' state. This is maintained only for alerts with configured 'for' time greater than grace period.
    :param forOutageTolerance: Max time to tolerate prometheus outage for restoring 'for' state of alert.
    :param resendDelay: Minimum amount of time to wait before resending an alert to Alertmanager.
    """
    forGracePeriod: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'forGracePeriod'})
    forOutageTolerance: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'forOutageTolerance'})
    resendDelay: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'resendDelay'})


@attr.s(kw_only=True)
class PrometheusSpecRules(K8sObjectBase):
    """
    | /--rules.*/ command-line arguments.
    
    :param alert: /--rules.alert.*/ command-line arguments
    """
    alert: Optional[Union[kdsl.monitoring.v1.PrometheusSpecRulesAlert,
        kdsl.monitoring.v1.PrometheusSpecRulesAlertTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'alert'})


@attr.s(kw_only=True)
class PrometheusSpecSecurityContextSeLinuxOptions(K8sObjectBase):
    """
    | The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    
    :param level: Level is SELinux level label that applies to the container.
    :param role: Role is a SELinux role label that applies to the container.
    :param type: Type is a SELinux type label that applies to the container.
    :param user: User is a SELinux user label that applies to the container.
    """
    level: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'level'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class PrometheusSpecSecurityContextArray(K8sObjectBase):
    """
    | Sysctl defines a kernel parameter to be set
    
    :param name: Name of a property to set
    :param value: Value of a property to set
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class PrometheusSpecSecurityContextWindowsOptions(K8sObjectBase):
    """
    | The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is alpha-level and it is only honored by servers that enable the WindowsRunAsUserName feature flag.
    """
    gmsaCredentialSpec: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'gmsaCredentialSpec'})
    gmsaCredentialSpecName: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'gmsaCredentialSpecName'})
    runAsUserName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsUserName'})


@attr.s(kw_only=True)
class PrometheusSpecSecurityContext(K8sObjectBase):
    """
    | SecurityContext holds pod-level security attributes and common container settings. This defaults to the default PodSecurityContext.
    
    :param fsGroup: A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod: 
     1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw---- 
     If unset, the Kubelet will not modify the ownership and permissions of any volume.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param seLinuxOptions: The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param supplementalGroups: A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.
    :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    fsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'fsGroup'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextSeLinuxOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'seLinuxOptions'})
    supplementalGroups: Optional[Sequence[int]] = attr.ib(default=None,
        metadata={'yaml_name': 'supplementalGroups'})
    sysctls: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContextArray,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'sysctls'})
    windowsOptions: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContextWindowsOptions,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextWindowsOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class PrometheusSpecServiceMonitorNamespaceSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecServiceMonitorNamespaceSelector(K8sObjectBase):
    """
    | Namespaces to be selected for ServiceMonitor discovery. If nil, only check own namespace.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecServiceMonitorSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecServiceMonitorSelector(K8sObjectBase):
    """
    | ServiceMonitors to be selected for target discovery.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelectorArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecStorageEmptyDir(K8sObjectBase):
    """
    | EmptyDirVolumeSource to be used by the Prometheus StatefulSets. If specified, used in place of any volumeClaimTemplate. More info: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateSpecDataSource(K8sObjectBase):
    """
    | This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    
    :param kind: Kind is the type of resource being referenced
    :param name: Name is the name of resource being referenced
    :param apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    apiGroup: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiGroup'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateSpecResources(K8sObjectBase):
    """
    | Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateSpecSelector(K8sObjectBase):
    """
    | A label query over volumes to consider for binding.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateSpec(K8sObjectBase):
    """
    | Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param accessModes: AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param dataSource: This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    :param resources: Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    :param selector: A label query over volumes to consider for binding.
    :param storageClassName: Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
    :param volumeMode: volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. This is a beta feature.
    :param volumeName: VolumeName is the binding reference to the PersistentVolume backing this claim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    dataSource: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecDataSource
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'dataSource'})
    resources: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecResources
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecResourcesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resources'})
    selector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'selector'})
    storageClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageClassName'})
    volumeMode: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeMode'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateStatusArray(K8sObjectBase):
    """
    | PersistentVolumeClaimCondition contails details about state of pvc
    
    :param status: None
    :param type: PersistentVolumeClaimConditionType is a valid value of PersistentVolumeClaimCondition.Type
    :param lastProbeTime: Last time we probed the condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param message: Human-readable message indicating details about last transition.
    :param reason: Unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastProbeTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastProbeTime'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplateStatus(K8sObjectBase):
    """
    | Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param accessModes: AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param capacity: Represents the actual resources of the underlying volume.
    :param conditions: Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.
    :param phase: Phase represents the current phase of PersistentVolumeClaim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    capacity: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'capacity'})
    conditions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatusArray,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatusArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'conditions'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})


@attr.s(kw_only=True)
class PrometheusSpecStorageVolumeClaimTemplate(K8sObjectBase):
    """
    | A PVC spec to be used by the Prometheus StatefulSets.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param spec: Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param status: Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Mapping[str, Any]] = attr.ib(default=None, metadata=
        {'yaml_name': 'metadata'})
    spec: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpec,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'spec'})
    status: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatus,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatusTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'status'})


@attr.s(kw_only=True)
class PrometheusSpecStorage(K8sObjectBase):
    """
    | Storage spec to specify how storage shall be used.
    
    :param emptyDir: EmptyDirVolumeSource to be used by the Prometheus StatefulSets. If specified, used in place of any volumeClaimTemplate. More info: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir
    :param volumeClaimTemplate: A PVC spec to be used by the Prometheus StatefulSets.
    """
    emptyDir: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageEmptyDir,
        kdsl.monitoring.v1.PrometheusSpecStorageEmptyDirTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'emptyDir'})
    volumeClaimTemplate: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplate,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'volumeClaimTemplate'}
        )


@attr.s(kw_only=True)
class PrometheusSpecThanosObjectStorageConfig(K8sObjectBase):
    """
    | ObjectStorageConfig configures object storage in Thanos.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecThanosResources(K8sObjectBase):
    """
    | Resources defines the resource requirements for the Thanos sidecar. If not provided, no requests/limits will be set
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class PrometheusSpecThanosTracingConfig(K8sObjectBase):
    """
    | TracingConfig configures tracing in Thanos. This is an experimental feature, it may change in any upcoming release in a breaking way.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecThanos(K8sObjectBase):
    """
    | Thanos configuration allows configuring various aspects of a Prometheus server in a Thanos environment. 
     This section is experimental, it may change significantly without deprecation notice in any release. 
     This is experimental and may change significantly without backward compatibility in any release.
    
    :param baseImage: Thanos base image if other than default.
    :param image: Image if specified has precedence over baseImage, tag and sha combinations. Specifying the version is still necessary to ensure the Prometheus Operator knows what version of Thanos is being configured.
    :param listenLocal: ListenLocal makes the Thanos sidecar listen on loopback, so that it does not bind against the Pod IP.
    :param objectStorageConfig: ObjectStorageConfig configures object storage in Thanos.
    :param resources: Resources defines the resource requirements for the Thanos sidecar. If not provided, no requests/limits will be set
    :param sha: SHA of Thanos container image to be deployed. Defaults to the value of `version`. Similar to a tag, but the SHA explicitly deploys an immutable container image. Version and Tag are ignored if SHA is set.
    :param tag: Tag of Thanos sidecar container image to be deployed. Defaults to the value of `version`. Version is ignored if Tag is set.
    :param tracingConfig: TracingConfig configures tracing in Thanos. This is an experimental feature, it may change in any upcoming release in a breaking way.
    :param version: Version describes the version of Thanos to use.
    """
    baseImage: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'baseImage'})
    image: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'image'})
    listenLocal: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'listenLocal'})
    objectStorageConfig: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecThanosObjectStorageConfig,
        kdsl.monitoring.v1.PrometheusSpecThanosObjectStorageConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'objectStorageConfig'}
        )
    resources: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecThanosResources,
        kdsl.monitoring.v1.PrometheusSpecThanosResourcesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resources'})
    sha: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'sha'})
    tag: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'tag'})
    tracingConfig: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecThanosTracingConfig,
        kdsl.monitoring.v1.PrometheusSpecThanosTracingConfigTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tracingConfig'})
    version: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'version'})


@attr.s(kw_only=True)
class PrometheusSpecArrayAwsElasticBlockStore(K8sObjectBase):
    """
    | AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    
    :param volumeID: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore TODO: how do we prevent errors in the filesystem from compromising the machine
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).
    :param readOnly: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayAzureDisk(K8sObjectBase):
    """
    | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    
    :param diskName: The Name of the data disk in the blob storage
    :param diskURI: The URI the data disk in the blob storage
    :param cachingMode: Host Caching mode: None, Read Only, Read Write.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param kind: Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    diskName: str = attr.ib(metadata={'yaml_name': 'diskName'})
    diskURI: str = attr.ib(metadata={'yaml_name': 'diskURI'})
    cachingMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'cachingMode'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayAzureFile(K8sObjectBase):
    """
    | AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    
    :param secretName: the name of secret that contains Azure Storage Account Name and Key
    :param shareName: Share Name
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})
    shareName: str = attr.ib(metadata={'yaml_name': 'shareName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayCephfsSecretRef(K8sObjectBase):
    """
    | Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayCephfs(K8sObjectBase):
    """
    | CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    
    :param monitors: Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param path: Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretFile: Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretRef: Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param user: Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretFile'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayCephfsSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayCephfsSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class PrometheusSpecArrayCinderSecretRef(K8sObjectBase):
    """
    | Optional: points to a secret object containing parameters used to connect to OpenStack.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayCinder(K8sObjectBase):
    """
    | Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    
    :param volumeID: volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param secretRef: Optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayCinderSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayCinderSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class PrometheusSpecArrayConfigMapArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class PrometheusSpecArrayConfigMap(K8sObjectBase):
    """
    | ConfigMap represents a configMap that should populate this volume
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMapArray,
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMapArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayCsiNodePublishSecretRef(K8sObjectBase):
    """
    | NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayCsi(K8sObjectBase):
    """
    | CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    
    :param driver: Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.
    :param fsType: Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.
    :param nodePublishSecretRef: NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    :param readOnly: Specifies a read-only configuration for the volume. Defaults to false (read/write).
    :param volumeAttributes: VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    nodePublishSecretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayCsiNodePublishSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayCsiNodePublishSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'nodePublishSecretRef'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    volumeAttributes: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeAttributes'})


@attr.s(kw_only=True)
class PrometheusSpecArrayDownwardAPIArrayFieldRef(K8sObjectBase):
    """
    | Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class PrometheusSpecArrayDownwardAPIArrayResourceFieldRef(K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class PrometheusSpecArrayDownwardAPIArray(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayResourceFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class PrometheusSpecArrayDownwardAPI(K8sObjectBase):
    """
    | DownwardAPI represents downward API about the pod that should populate this volume
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: Items is a list of downward API volume file
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArray,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class PrometheusSpecArrayEmptyDir(K8sObjectBase):
    """
    | EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class PrometheusSpecArrayFc(K8sObjectBase):
    """
    | FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. TODO: how do we prevent errors in the filesystem from compromising the machine
    :param lun: Optional: FC target lun number
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param targetWWNs: Optional: FC target worldwide names (WWNs)
    :param wwids: Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    lun: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'lun'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    targetWWNs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'targetWWNs'})
    wwids: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'wwids'})


@attr.s(kw_only=True)
class PrometheusSpecArrayFlexVolumeSecretRef(K8sObjectBase):
    """
    | Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayFlexVolume(K8sObjectBase):
    """
    | FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    
    :param driver: Driver is the name of the driver to use for this volume.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    :param options: Optional: Extra command options if any.
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    options: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'options'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolumeSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolumeSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class PrometheusSpecArrayFlocker(K8sObjectBase):
    """
    | Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    
    :param datasetName: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated
    :param datasetUUID: UUID of the dataset. This is unique identifier of a Flocker dataset
    """
    datasetName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetName'})
    datasetUUID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetUUID'})


@attr.s(kw_only=True)
class PrometheusSpecArrayGcePersistentDisk(K8sObjectBase):
    """
    | GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    
    :param pdName: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk TODO: how do we prevent errors in the filesystem from compromising the machine
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    pdName: str = attr.ib(metadata={'yaml_name': 'pdName'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayGitRepo(K8sObjectBase):
    """
    | GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    
    :param repository: Repository URL
    :param directory: Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.
    :param revision: Commit hash for the specified revision.
    """
    repository: str = attr.ib(metadata={'yaml_name': 'repository'})
    directory: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'directory'})
    revision: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'revision'})


@attr.s(kw_only=True)
class PrometheusSpecArrayGlusterfs(K8sObjectBase):
    """
    | Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    
    :param endpoints: EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param path: Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param readOnly: ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints: str = attr.ib(metadata={'yaml_name': 'endpoints'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayHostPath(K8sObjectBase):
    """
    | HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
    
    :param path: Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    :param type: Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class PrometheusSpecArrayIscsiSecretRef(K8sObjectBase):
    """
    | CHAP Secret for iSCSI target and initiator authentication
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayIscsi(K8sObjectBase):
    """
    | ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    
    :param iqn: Target iSCSI Qualified Name.
    :param lun: iSCSI Target Lun number.
    :param targetPortal: iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param chapAuthDiscovery: whether support iSCSI Discovery CHAP authentication
    :param chapAuthSession: whether support iSCSI Session CHAP authentication
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi TODO: how do we prevent errors in the filesystem from compromising the machine
    :param initiatorName: Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    :param iscsiInterface: iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    :param portals: iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    :param secretRef: CHAP Secret for iSCSI target and initiator authentication
    """
    iqn: str = attr.ib(metadata={'yaml_name': 'iqn'})
    lun: int = attr.ib(metadata={'yaml_name': 'lun'})
    targetPortal: str = attr.ib(metadata={'yaml_name': 'targetPortal'})
    chapAuthDiscovery: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthDiscovery'})
    chapAuthSession: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthSession'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    initiatorName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'initiatorName'})
    iscsiInterface: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'iscsiInterface'})
    portals: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'portals'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayIscsiSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayIscsiSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class PrometheusSpecArrayNfs(K8sObjectBase):
    """
    | NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    
    :param path: Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param server: Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param readOnly: ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayPersistentVolumeClaim(K8sObjectBase):
    """
    | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param claimName: ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param readOnly: Will force the ReadOnly setting in VolumeMounts. Default false.
    """
    claimName: str = attr.ib(metadata={'yaml_name': 'claimName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayPhotonPersistentDisk(K8sObjectBase):
    """
    | PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    
    :param pdID: ID that identifies Photon Controller persistent disk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    pdID: str = attr.ib(metadata={'yaml_name': 'pdID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})


@attr.s(kw_only=True)
class PrometheusSpecArrayPortworxVolume(K8sObjectBase):
    """
    | PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    
    :param volumeID: VolumeID uniquely identifies a Portworx volume
    :param fsType: FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayConfigMapArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayConfigMap(K8sObjectBase):
    """
    | information about the configMap data to project
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMapArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMapArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRef(K8sObjectBase):
    """
    | Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef(
    K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayDownwardAPIArray(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRef
        ,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayDownwardAPI(K8sObjectBase):
    """
    | information about the downwardAPI data to project
    
    :param items: Items is a list of DownwardAPIVolume file
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArraySecretArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArraySecret(K8sObjectBase):
    """
    | information about the secret data to project
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecretArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecretArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArrayServiceAccountToken(K8sObjectBase):
    """
    | information about the serviceAccountToken data to project
    
    :param path: Path is the path relative to the mount point of the file to project the token into.
    :param audience: Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.
    :param expirationSeconds: ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    audience: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'audience'})
    expirationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'expirationSeconds'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjectedArray(K8sObjectBase):
    """
    | Projection that may be projected along with other supported volume types
    
    :param configMap: information about the configMap data to project
    :param downwardAPI: information about the downwardAPI data to project
    :param secret: information about the secret data to project
    :param serviceAccountToken: information about the serviceAccountToken data to project
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMapTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    downwardAPI: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPI,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPITypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'downwardAPI'})
    secret: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecret,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})
    serviceAccountToken: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayServiceAccountToken
        ,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayServiceAccountTokenTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceAccountToken'})


@attr.s(kw_only=True)
class PrometheusSpecArrayProjected(K8sObjectBase):
    """
    | Items for all in one resources secrets, configmaps, and downward API
    
    :param sources: list of volume projections
    :param defaultMode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    sources: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'sources'})
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})


@attr.s(kw_only=True)
class PrometheusSpecArrayQuobyte(K8sObjectBase):
    """
    | Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    
    :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes
    :param volume: Volume is a string that references an already created Quobyte volume by name.
    :param group: Group to map volume access to Default is no group
    :param readOnly: ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.
    :param tenant: Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin
    :param user: User to map volume access to Defaults to serivceaccount user
    """
    registry: str = attr.ib(metadata={'yaml_name': 'registry'})
    volume: str = attr.ib(metadata={'yaml_name': 'volume'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    tenant: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'tenant'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class PrometheusSpecArrayRbdSecretRef(K8sObjectBase):
    """
    | SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayRbd(K8sObjectBase):
    """
    | RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    
    :param image: The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param monitors: A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd TODO: how do we prevent errors in the filesystem from compromising the machine
    :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param pool: The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param secretRef: SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param user: The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    image: str = attr.ib(metadata={'yaml_name': 'image'})
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    keyring: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyring'})
    pool: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'pool'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayRbdSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayRbdSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class PrometheusSpecArrayScaleIOSecretRef(K8sObjectBase):
    """
    | SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayScaleIO(K8sObjectBase):
    """
    | ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    
    :param gateway: The host address of the ScaleIO API Gateway.
    :param secretRef: SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    :param system: The name of the storage system as configured in ScaleIO.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".
    :param protectionDomain: The name of the ScaleIO Protection Domain for the configured storage.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param sslEnabled: Flag to enable/disable SSL communication with Gateway, default false
    :param storageMode: Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    :param storagePool: The ScaleIO Storage Pool associated with the protection domain.
    :param volumeName: The name of a volume already created in the ScaleIO system that is associated with this volume source.
    """
    gateway: str = attr.ib(metadata={'yaml_name': 'gateway'})
    secretRef: Union[kdsl.monitoring.v1.PrometheusSpecArrayScaleIOSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayScaleIOSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})
    system: str = attr.ib(metadata={'yaml_name': 'system'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    protectionDomain: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'protectionDomain'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    sslEnabled: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'sslEnabled'})
    storageMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageMode'})
    storagePool: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePool'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class PrometheusSpecArraySecretArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class PrometheusSpecArraySecret(K8sObjectBase):
    """
    | Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param optional: Specify whether the Secret or its keys must be defined
    :param secretName: Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecretArray,
        kdsl.monitoring.v1.PrometheusSpecArraySecretArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})
    secretName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretName'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStorageosSecretRef(K8sObjectBase):
    """
    | SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class PrometheusSpecArrayStorageos(K8sObjectBase):
    """
    | StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    :param volumeName: VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    :param volumeNamespace: VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStorageosSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayStorageosSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})
    volumeNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'volumeNamespace'})


@attr.s(kw_only=True)
class PrometheusSpecArrayVsphereVolume(K8sObjectBase):
    """
    | VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    
    :param volumePath: Path that identifies vSphere volume vmdk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param storagePolicyID: Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.
    :param storagePolicyName: Storage Policy Based Management (SPBM) profile name.
    """
    volumePath: str = attr.ib(metadata={'yaml_name': 'volumePath'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    storagePolicyID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyID'})
    storagePolicyName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyName'})


@attr.s(kw_only=True)
class PrometheusSpec(K8sObjectBase):
    """
    | Specification of the desired behavior of the Prometheus cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    
    :param additionalAlertManagerConfigs: AdditionalAlertManagerConfigs allows specifying a key of a Secret containing additional Prometheus AlertManager configurations. AlertManager configurations specified are appended to the configurations generated by the Prometheus Operator. Job configurations specified must have the form as specified in the official Prometheus documentation: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config. As AlertManager configs are appended, the user is responsible to make sure it is valid. Note that using this feature may expose the possibility to break upgrades of Prometheus. It is advised to review Prometheus release notes to ensure that no incompatible AlertManager configs are going to break Prometheus after the upgrade.
    :param additionalAlertRelabelConfigs: AdditionalAlertRelabelConfigs allows specifying a key of a Secret containing additional Prometheus alert relabel configurations. Alert relabel configurations specified are appended to the configurations generated by the Prometheus Operator. Alert relabel configurations specified must have the form as specified in the official Prometheus documentation: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs. As alert relabel configs are appended, the user is responsible to make sure it is valid. Note that using this feature may expose the possibility to break upgrades of Prometheus. It is advised to review Prometheus release notes to ensure that no incompatible alert relabel configs are going to break Prometheus after the upgrade.
    :param additionalScrapeConfigs: AdditionalScrapeConfigs allows specifying a key of a Secret containing additional Prometheus scrape configurations. Scrape configurations specified are appended to the configurations generated by the Prometheus Operator. Job configurations specified must have the form as specified in the official Prometheus documentation: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config. As scrape configs are appended, the user is responsible to make sure it is valid. Note that using this feature may expose the possibility to break upgrades of Prometheus. It is advised to review Prometheus release notes to ensure that no incompatible scrape configs are going to break Prometheus after the upgrade.
    :param affinity: If specified, the pod's scheduling constraints.
    :param alerting: Define details regarding alerting.
    :param apiserverConfig: APIServerConfig allows specifying a host and auth methods to access apiserver. If left empty, Prometheus is assumed to run inside of the cluster and will discover API servers automatically and use the pod's CA certificate and bearer token file at /var/run/secrets/kubernetes.io/serviceaccount/.
    :param arbitraryFSAccessThroughSMs: ArbitraryFSAccessThroughSMs configures whether configuration based on a service monitor can access arbitrary files on the file system of the Prometheus container e.g. bearer token files.
    :param baseImage: Base image to use for a Prometheus deployment.
    :param configMaps: ConfigMaps is a list of ConfigMaps in the same namespace as the Prometheus object, which shall be mounted into the Prometheus Pods. The ConfigMaps are mounted into /etc/prometheus/configmaps/<configmap-name>.
    :param containers: Containers allows injecting additional containers or modifying operator generated containers. This can be used to allow adding an authentication proxy to a Prometheus pod or to change the behavior of an operator generated container. Containers described here modify an operator generated container if they share the same name and modifications are done via a strategic merge patch. The current container names are: `prometheus`, `prometheus-config-reloader`, `rules-configmap-reloader`, and `thanos-sidecar`. Overriding containers is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice.
    :param disableCompaction: Disable prometheus compaction.
    :param enableAdminAPI: Enable access to prometheus web admin API. Defaults to the value of `false`. WARNING: Enabling the admin APIs enables mutating endpoints, to delete data, shutdown Prometheus, and more. Enabling this should be done with care and the user is advised to add additional authentication authorization via a proxy to ensure only clients authorized to perform these actions can do so. For more information see https://prometheus.io/docs/prometheus/latest/querying/api/#tsdb-admin-apis
    :param enforcedNamespaceLabel: EnforcedNamespaceLabel enforces adding a namespace label of origin for each alert and metric that is user created. The label value will always be the namespace of the object that is being created.
    :param evaluationInterval: Interval between consecutive evaluations.
    :param externalLabels: The labels to add to any time series or alerts when communicating with external systems (federation, remote storage, Alertmanager).
    :param externalUrl: The external URL the Prometheus instances will be available under. This is necessary to generate correct URLs. This is necessary if Prometheus is not served from root of a DNS name.
    :param ignoreNamespaceSelectors: IgnoreNamespaceSelectors if set to true will ignore NamespaceSelector settings from the podmonitor and servicemonitor configs, and they will only discover endpoints within their current namespace.  Defaults to false.
    :param image: Image if specified has precedence over baseImage, tag and sha combinations. Specifying the version is still necessary to ensure the Prometheus Operator knows what version of Prometheus is being configured.
    :param imagePullSecrets: An optional list of references to secrets in the same namespace to use for pulling prometheus and alertmanager images from registries see http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod
    :param initContainers: InitContainers allows adding initContainers to the pod definition. Those can be used to e.g. fetch secrets for injection into the Prometheus configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ Using initContainers for any use case other then secret fetching is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice.
    :param listenLocal: ListenLocal makes the Prometheus server listen on loopback, so that it does not bind against the Pod IP.
    :param logFormat: Log format for Prometheus to be configured with.
    :param logLevel: Log level for Prometheus to be configured with.
    :param nodeSelector: Define which Nodes the Pods are scheduled on.
    :param overrideHonorLabels: OverrideHonorLabels if set to true overrides all user configured honor_labels. If HonorLabels is set in ServiceMonitor or PodMonitor to true, this overrides honor_labels to false.
    :param overrideHonorTimestamps: OverrideHonorTimestamps allows to globally enforce honoring timestamps in all scrape configs.
    :param paused: When a Prometheus deployment is paused, no actions except for deletion will be performed on the underlying objects.
    :param podMetadata: Standard object’s metadata. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata Metadata Labels and Annotations gets propagated to the prometheus pods.
    :param podMonitorNamespaceSelector: Namespaces to be selected for PodMonitor discovery. If nil, only check own namespace.
    :param podMonitorSelector: *Experimental* PodMonitors to be selected for target discovery.
    :param portName: Port name used for the pods and governing service. This defaults to web
    :param priorityClassName: Priority class assigned to the Pods
    :param prometheusExternalLabelName: Name of Prometheus external label used to denote Prometheus instance name. Defaults to the value of `prometheus`. External label will _not_ be added when value is set to empty string (`""`).
    :param query: QuerySpec defines the query command line flags when starting Prometheus.
    :param remoteRead: If specified, the remote_read spec. This is an experimental feature, it may change in any upcoming release in a breaking way.
    :param remoteWrite: If specified, the remote_write spec. This is an experimental feature, it may change in any upcoming release in a breaking way.
    :param replicaExternalLabelName: Name of Prometheus external label used to denote replica name. Defaults to the value of `prometheus_replica`. External label will _not_ be added when value is set to empty string (`""`).
    :param replicas: Number of instances to deploy for a Prometheus deployment.
    :param resources: Define resources requests and limits for single Pods.
    :param retention: Time duration Prometheus shall retain data for. Default is '24h', and must match the regular expression `[0-9]+(ms|s|m|h|d|w|y)` (milliseconds seconds minutes hours days weeks years).
    :param retentionSize: Maximum amount of disk space used by blocks.
    :param routePrefix: The route prefix Prometheus registers HTTP handlers for. This is useful, if using ExternalURL and a proxy is rewriting HTTP routes of a request, and the actual ExternalURL is still true, but the server serves requests under a different route prefix. For example for use with `kubectl proxy`.
    :param ruleNamespaceSelector: Namespaces to be selected for PrometheusRules discovery. If unspecified, only the same namespace as the Prometheus object is in is used.
    :param ruleSelector: A selector to select which PrometheusRules to mount for loading alerting rules from. Until (excluding) Prometheus Operator v0.24.0 Prometheus Operator will migrate any legacy rule ConfigMaps to PrometheusRule custom resources selected by RuleSelector. Make sure it does not match any config maps that you do not want to be migrated.
    :param rules: /--rules.*/ command-line arguments.
    :param scrapeInterval: Interval between consecutive scrapes.
    :param secrets: Secrets is a list of Secrets in the same namespace as the Prometheus object, which shall be mounted into the Prometheus Pods. The Secrets are mounted into /etc/prometheus/secrets/<secret-name>.
    :param securityContext: SecurityContext holds pod-level security attributes and common container settings. This defaults to the default PodSecurityContext.
    :param serviceAccountName: ServiceAccountName is the name of the ServiceAccount to use to run the Prometheus Pods.
    :param serviceMonitorNamespaceSelector: Namespaces to be selected for ServiceMonitor discovery. If nil, only check own namespace.
    :param serviceMonitorSelector: ServiceMonitors to be selected for target discovery.
    :param sha: SHA of Prometheus container image to be deployed. Defaults to the value of `version`. Similar to a tag, but the SHA explicitly deploys an immutable container image. Version and Tag are ignored if SHA is set.
    :param storage: Storage spec to specify how storage shall be used.
    :param tag: Tag of Prometheus container image to be deployed. Defaults to the value of `version`. Version is ignored if Tag is set.
    :param thanos: Thanos configuration allows configuring various aspects of a Prometheus server in a Thanos environment. 
     This section is experimental, it may change significantly without deprecation notice in any release. 
     This is experimental and may change significantly without backward compatibility in any release.
    :param tolerations: If specified, the pod's tolerations.
    :param version: Version of Prometheus to be deployed.
    :param volumes: Volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects.
    :param walCompression: Enable compression of the write-ahead log using Snappy. This flag is only available in versions of Prometheus >= 2.11.0.
    """
    additionalAlertManagerConfigs: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertManagerConfigs,
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertManagerConfigsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'additionalAlertManagerConfigs'})
    additionalAlertRelabelConfigs: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertRelabelConfigs,
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertRelabelConfigsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'additionalAlertRelabelConfigs'})
    additionalScrapeConfigs: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecAdditionalScrapeConfigs,
        kdsl.monitoring.v1.PrometheusSpecAdditionalScrapeConfigsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'additionalScrapeConfigs'})
    affinity: Optional[Union[kdsl.monitoring.v1.PrometheusSpecAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'affinity'})
    alerting: Optional[Union[kdsl.monitoring.v1.PrometheusSpecAlerting,
        kdsl.monitoring.v1.PrometheusSpecAlertingTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'alerting'})
    apiserverConfig: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfig,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'apiserverConfig'})
    arbitraryFSAccessThroughSMs: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecArbitraryFSAccessThroughSMs,
        kdsl.monitoring.v1.PrometheusSpecArbitraryFSAccessThroughSMsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'arbitraryFSAccessThroughSMs'})
    baseImage: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'baseImage'})
    configMaps: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'configMaps'})
    containers: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'containers'})
    disableCompaction: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'disableCompaction'})
    enableAdminAPI: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'enableAdminAPI'})
    enforcedNamespaceLabel: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'enforcedNamespaceLabel'})
    evaluationInterval: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'evaluationInterval'})
    externalLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'externalLabels'})
    externalUrl: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'externalUrl'})
    ignoreNamespaceSelectors: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'ignoreNamespaceSelectors'})
    image: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'image'})
    imagePullSecrets: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'imagePullSecrets'})
    initContainers: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'initContainers'})
    listenLocal: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'listenLocal'})
    logFormat: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'logFormat'})
    logLevel: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'logLevel'})
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    overrideHonorLabels: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'overrideHonorLabels'})
    overrideHonorTimestamps: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'overrideHonorTimestamps'})
    paused: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'paused'})
    podMetadata: Optional[Mapping[str, Any]] = attr.ib(default=None,
        metadata={'yaml_name': 'podMetadata'})
    podMonitorNamespaceSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelector,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'podMonitorNamespaceSelector'})
    podMonitorSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelector,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'podMonitorSelector'})
    portName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'portName'})
    priorityClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'priorityClassName'})
    prometheusExternalLabelName: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'prometheusExternalLabelName'})
    query: Optional[Union[kdsl.monitoring.v1.PrometheusSpecQuery,
        kdsl.monitoring.v1.PrometheusSpecQueryTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'query'})
    remoteRead: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'remoteRead'})
    remoteWrite: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'remoteWrite'})
    replicaExternalLabelName: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'replicaExternalLabelName'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    resources: Optional[Union[kdsl.monitoring.v1.PrometheusSpecResources,
        kdsl.monitoring.v1.PrometheusSpecResourcesTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'resources'})
    retention: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'retention'})
    retentionSize: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'retentionSize'})
    routePrefix: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'routePrefix'})
    ruleNamespaceSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelector,
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'ruleNamespaceSelector'})
    ruleSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecRuleSelector,
        kdsl.monitoring.v1.PrometheusSpecRuleSelectorTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'ruleSelector'})
    rules: Optional[Union[kdsl.monitoring.v1.PrometheusSpecRules,
        kdsl.monitoring.v1.PrometheusSpecRulesTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'rules'})
    scrapeInterval: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'scrapeInterval'})
    secrets: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'secrets'})
    securityContext: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContext,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'securityContext'})
    serviceAccountName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceAccountName'})
    serviceMonitorNamespaceSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelector,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceMonitorNamespaceSelector'})
    serviceMonitorSelector: Optional[Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelector,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'serviceMonitorSelector'})
    sha: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'sha'})
    storage: Optional[Union[kdsl.monitoring.v1.PrometheusSpecStorage,
        kdsl.monitoring.v1.PrometheusSpecStorageTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'storage'})
    tag: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'tag'})
    thanos: Optional[Union[kdsl.monitoring.v1.PrometheusSpecThanos,
        kdsl.monitoring.v1.PrometheusSpecThanosTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'thanos'})
    tolerations: Optional[Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'tolerations'})
    version: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'version'})
    volumes: Optional[Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'volumes'})
    walCompression: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'walCompression'})


@attr.s(kw_only=True)
class Prometheus(K8sResourceBase):
    """
    | Prometheus defines a Prometheus deployment.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Specification of the desired behavior of the Prometheus cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'monitoring.coreos.com/v1'
    kind: ClassVar[str] = 'Prometheus'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.monitoring.v1.PrometheusSpec,
        kdsl.monitoring.v1.PrometheusSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class PodMonitorSpecNamespaceSelector(K8sObjectBase):
    """
    | Selector to select which namespaces the Endpoints objects are discovered from.
    
    :param any: Boolean describing whether all namespaces are selected in contrast to a list restricting them.
    :param matchNames: List of namespace names.
    """
    any: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'any'})
    matchNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'matchNames'})


@attr.s(kw_only=True)
class PodMonitorSpecArrayArray(K8sObjectBase):
    """
    | RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion. It defines `<metric_relabel_configs>`-section of Prometheus configuration. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs
    
    :param action: Action to perform based on regex matching. Default is 'replace'
    :param modulus: Modulus to take of the hash of the source label values.
    :param regex: Regular expression against which the extracted value is matched. Default is '(.*)'
    :param replacement: Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1'
    :param separator: Separator placed between concatenated source label values. default is ';'.
    :param sourceLabels: The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.
    :param targetLabel: Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.
    """
    action: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'action'})
    modulus: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'modulus'})
    regex: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'regex'})
    replacement: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'replacement'})
    separator: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'separator'})
    sourceLabels: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'sourceLabels'})
    targetLabel: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'targetLabel'})


@attr.s(kw_only=True)
class PodMonitorSpecArray(K8sObjectBase):
    """
    | PodMetricsEndpoint defines a scrapeable endpoint of a Kubernetes Pod serving Prometheus metrics.
    
    :param honorLabels: HonorLabels chooses the metric's labels on collisions with target labels.
    :param honorTimestamps: HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data.
    :param interval: Interval at which metrics should be scraped
    :param metricRelabelings: MetricRelabelConfigs to apply to samples before ingestion.
    :param params: Optional HTTP URL parameters
    :param path: HTTP path to scrape for metrics.
    :param port: Name of the port this endpoint refers to. Mutually exclusive with targetPort.
    :param proxyUrl: ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint.
    :param relabelings: RelabelConfigs to apply to samples before ingestion. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config
    :param scheme: HTTP scheme to use for scraping.
    :param scrapeTimeout: Timeout after which the scrape is ended
    :param targetPort: Name or number of the target port of the endpoint. Mutually exclusive with port.
    """
    honorLabels: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'honorLabels'})
    honorTimestamps: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'honorTimestamps'})
    interval: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'interval'})
    metricRelabelings: Optional[Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecArrayArray,
        kdsl.monitoring.v1.PodMonitorSpecArrayArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'metricRelabelings'})
    params: Optional[Mapping[str, Sequence[str]]] = attr.ib(default=None,
        metadata={'yaml_name': 'params'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    port: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'port'})
    proxyUrl: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'proxyUrl'})
    relabelings: Optional[Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecArrayArray,
        kdsl.monitoring.v1.PodMonitorSpecArrayArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'relabelings'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})
    scrapeTimeout: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'scrapeTimeout'})
    targetPort: Optional[Any] = attr.ib(default=None, metadata={'yaml_name':
        'targetPort'})


@attr.s(kw_only=True)
class PodMonitorSpecSelectorArray(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class PodMonitorSpecSelector(K8sObjectBase):
    """
    | Selector to select Pod objects.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecSelectorArray,
        kdsl.monitoring.v1.PodMonitorSpecSelectorArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class PodMonitorSpec(K8sObjectBase):
    """
    | Specification of desired Pod selection for target discovery by Prometheus.
    
    :param podMetricsEndpoints: A list of endpoints allowed as part of this PodMonitor.
    :param selector: Selector to select Pod objects.
    :param jobLabel: The label to use to retrieve the job name from.
    :param namespaceSelector: Selector to select which namespaces the Endpoints objects are discovered from.
    :param podTargetLabels: PodTargetLabels transfers labels on the Kubernetes Pod onto the target.
    :param sampleLimit: SampleLimit defines per-scrape limit on number of scraped samples that will be accepted.
    """
    podMetricsEndpoints: Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecArray,
        kdsl.monitoring.v1.PodMonitorSpecArrayTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'podMetricsEndpoints'})
    selector: Union[kdsl.monitoring.v1.PodMonitorSpecSelector,
        kdsl.monitoring.v1.PodMonitorSpecSelectorTypedDict] = attr.ib(metadata
        ={'yaml_name': 'selector'})
    jobLabel: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'jobLabel'})
    namespaceSelector: Optional[Union[
        kdsl.monitoring.v1.PodMonitorSpecNamespaceSelector,
        kdsl.monitoring.v1.PodMonitorSpecNamespaceSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'namespaceSelector'})
    podTargetLabels: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'podTargetLabels'})
    sampleLimit: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'sampleLimit'})


@attr.s(kw_only=True)
class PodMonitor(K8sResourceBase):
    """
    | PodMonitor defines monitoring for a set of pods.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Specification of desired Pod selection for target discovery by Prometheus.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'monitoring.coreos.com/v1'
    kind: ClassVar[str] = 'PodMonitor'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.monitoring.v1.PodMonitorSpec,
        kdsl.monitoring.v1.PodMonitorSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArray(K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinityArrayPreference(K8sObjectBase):
    """
    | A node selector term, associated with the corresponding weight.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinityArray(K8sObjectBase):
    """
    | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    
    :param preference: A node selector term, associated with the corresponding weight.
    :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """
    preference: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreference,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'preference'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray(
    K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray(
    K8sObjectBase):
    """
    | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(
    K8sObjectBase):
    """
    | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    
    :param nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.
    """
    nodeSelectorTerms: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]] = attr.ib(metadata={'yaml_name': 'nodeSelectorTerms'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityNodeAffinity(K8sObjectBase):
    """
    | Describes node affinity scheduling rules for the pod.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTerm(K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinityArray(K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArray(K8sObjectBase
    ):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinityArrayLabelSelector(K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAffinity(K8sObjectBase):
    """
    | Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTerm(K8sObjectBase
    ):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinityArray(K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArray(
    K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelector(K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinityPodAntiAffinity(K8sObjectBase):
    """
    | Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class AlertmanagerSpecAffinity(K8sObjectBase):
    """
    | If specified, the pod's scheduling constraints.
    
    :param nodeAffinity: Describes node affinity scheduling rules for the pod.
    :param podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    :param podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """
    nodeAffinity: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'nodeAffinity'})
    podAffinity: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'podAffinity'})
    podAntiAffinity: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'podAntiAffinity'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArrayValueFromConfigMapKeyRef(K8sObjectBase):
    """
    | Selects a key of a ConfigMap.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArrayValueFromFieldRef(K8sObjectBase):
    """
    | Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArrayValueFromResourceFieldRef(K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArrayValueFromSecretKeyRef(K8sObjectBase):
    """
    | Selects a key of a secret in the pod's namespace
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArrayValueFrom(K8sObjectBase):
    """
    | Source for the environment variable's value. Cannot be used if value is not empty.
    
    :param configMapKeyRef: Selects a key of a ConfigMap.
    :param fieldRef: Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    :param secretKeyRef: Selects a key of a secret in the pod's namespace
    """
    configMapKeyRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromConfigMapKeyRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromConfigMapKeyRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMapKeyRef'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromFieldRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromResourceFieldRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})
    secretKeyRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromSecretKeyRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromSecretKeyRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'secretKeyRef'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArray(K8sObjectBase):
    """
    | VolumeMount describes a mounting of a Volume within a container.
    
    :param mountPath: Path within the container at which the volume should be mounted.  Must not contain ':'.
    :param name: This must match the Name of a Volume.
    :param mountPropagation: mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.
    :param readOnly: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.
    :param subPath: Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).
    :param subPathExpr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive. This field is beta in 1.15.
    """
    mountPath: str = attr.ib(metadata={'yaml_name': 'mountPath'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    mountPropagation: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'mountPropagation'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    subPath: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'subPath'})
    subPathExpr: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'subPathExpr'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArrayConfigMapRef(K8sObjectBase):
    """
    | The ConfigMap to select from
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayArraySecretRef(K8sObjectBase):
    """
    | The Secret to select from
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePostStartExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePostStartHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePostStartHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePostStartTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePostStart(K8sObjectBase):
    """
    | PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartExecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGetTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePreStopExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePreStopHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePreStopHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePreStopTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecyclePreStop(K8sObjectBase):
    """
    | PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGetTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLifecycle(K8sObjectBase):
    """
    | Actions that the management system should take in response to container lifecycle events. Cannot be updated.
    
    :param postStart: PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    :param preStop: PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """
    postStart: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStart,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'postStart'})
    preStop: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStop,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'preStop'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLivenessProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLivenessProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLivenessProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLivenessProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayLivenessProbe(K8sObjectBase):
    """
    | Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayReadinessProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayReadinessProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayReadinessProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayReadinessProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayReadinessProbe(K8sObjectBase):
    """
    | Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeTcpSocketTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayResources(K8sObjectBase):
    """
    | Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class AlertmanagerSpecArraySecurityContextCapabilities(K8sObjectBase):
    """
    | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    
    :param add: Added capabilities
    :param drop: Removed capabilities
    """
    add: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'add'})
    drop: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'drop'})


@attr.s(kw_only=True)
class AlertmanagerSpecArraySecurityContextSeLinuxOptions(K8sObjectBase):
    """
    | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param level: Level is SELinux level label that applies to the container.
    :param role: Role is a SELinux role label that applies to the container.
    :param type: Type is a SELinux type label that applies to the container.
    :param user: User is a SELinux user label that applies to the container.
    """
    level: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'level'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class AlertmanagerSpecArraySecurityContextWindowsOptions(K8sObjectBase):
    """
    | The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is alpha-level and it is only honored by servers that enable the WindowsRunAsUserName feature flag.
    """
    gmsaCredentialSpec: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'gmsaCredentialSpec'})
    gmsaCredentialSpecName: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'gmsaCredentialSpecName'})
    runAsUserName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsUserName'})


@attr.s(kw_only=True)
class AlertmanagerSpecArraySecurityContext(K8sObjectBase):
    """
    | Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    
    :param allowPrivilegeEscalation: AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN
    :param capabilities: The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.
    :param procMount: procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.
    :param readOnlyRootFilesystem: Whether this container has a read-only root filesystem. Default is false.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param seLinuxOptions: The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    allowPrivilegeEscalation: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'allowPrivilegeEscalation'})
    capabilities: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextCapabilities,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextCapabilitiesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'capabilities'})
    privileged: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'privileged'})
    procMount: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'procMount'})
    readOnlyRootFilesystem: Optional[bool] = attr.ib(default=None, metadata
        ={'yaml_name': 'readOnlyRootFilesystem'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextSeLinuxOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'seLinuxOptions'})
    windowsOptions: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextWindowsOptions,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextWindowsOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStartupProbeExec(K8sObjectBase):
    """
    | One and only one of the following should be specified. Exec specifies the action to take.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStartupProbeHttpGetArray(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStartupProbeHttpGet(K8sObjectBase):
    """
    | HTTPGet specifies the http request to perform.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGetArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStartupProbeTcpSocket(K8sObjectBase):
    """
    | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Any = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStartupProbe(K8sObjectBase):
    """
    | StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeExecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGetTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeTcpSocketTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class AlertmanagerSpecArray(K8sObjectBase):
    """
    | Volume represents a named volume in a pod that may be accessed by any container in the pod.
    
    :param name: Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param awsElasticBlockStore: AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param azureDisk: AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    :param azureFile: AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    :param cephfs: CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    :param cinder: Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param configMap: ConfigMap represents a configMap that should populate this volume
    :param csi: CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    :param downwardAPI: DownwardAPI represents downward API about the pod that should populate this volume
    :param emptyDir: EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param fc: FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    :param flexVolume: FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    :param flocker: Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    :param gcePersistentDisk: GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param gitRepo: GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    :param glusterfs: Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    :param hostPath: HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
    :param iscsi: ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    :param nfs: NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param persistentVolumeClaim: PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param photonPersistentDisk: PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    :param portworxVolume: PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    :param projected: Items for all in one resources secrets, configmaps, and downward API
    :param quobyte: Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    :param rbd: RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    :param scaleIO: ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    :param secret: Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    :param storageos: StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    :param vsphereVolume: VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    awsElasticBlockStore: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayAwsElasticBlockStore,
        kdsl.monitoring.v1.AlertmanagerSpecArrayAwsElasticBlockStoreTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'awsElasticBlockStore'})
    azureDisk: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayAzureDisk,
        kdsl.monitoring.v1.AlertmanagerSpecArrayAzureDiskTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureDisk'})
    azureFile: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayAzureFile,
        kdsl.monitoring.v1.AlertmanagerSpecArrayAzureFileTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureFile'})
    cephfs: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayCephfs,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCephfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cephfs'})
    cinder: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayCinder,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCinderTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cinder'})
    configMap: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMap,
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMapTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'configMap'})
    csi: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayCsi,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCsiTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'csi'})
    downwardAPI: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPI,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPITypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'downwardAPI'})
    emptyDir: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayEmptyDir,
        kdsl.monitoring.v1.AlertmanagerSpecArrayEmptyDirTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'emptyDir'})
    fc: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayFc,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFcTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'fc'})
    flexVolume: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolume,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'flexVolume'})
    flocker: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayFlocker,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlockerTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'flocker'})
    gcePersistentDisk: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayGcePersistentDisk,
        kdsl.monitoring.v1.AlertmanagerSpecArrayGcePersistentDiskTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'gcePersistentDisk'})
    gitRepo: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayGitRepo,
        kdsl.monitoring.v1.AlertmanagerSpecArrayGitRepoTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'gitRepo'})
    glusterfs: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayGlusterfs,
        kdsl.monitoring.v1.AlertmanagerSpecArrayGlusterfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'glusterfs'})
    hostPath: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayHostPath,
        kdsl.monitoring.v1.AlertmanagerSpecArrayHostPathTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'hostPath'})
    iscsi: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayIscsi,
        kdsl.monitoring.v1.AlertmanagerSpecArrayIscsiTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'iscsi'})
    nfs: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayNfs,
        kdsl.monitoring.v1.AlertmanagerSpecArrayNfsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'nfs'})
    persistentVolumeClaim: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayPersistentVolumeClaim,
        kdsl.monitoring.v1.AlertmanagerSpecArrayPersistentVolumeClaimTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'persistentVolumeClaim'})
    photonPersistentDisk: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayPhotonPersistentDisk,
        kdsl.monitoring.v1.AlertmanagerSpecArrayPhotonPersistentDiskTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'photonPersistentDisk'})
    portworxVolume: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayPortworxVolume,
        kdsl.monitoring.v1.AlertmanagerSpecArrayPortworxVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'portworxVolume'})
    projected: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjected,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'projected'})
    quobyte: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayQuobyte,
        kdsl.monitoring.v1.AlertmanagerSpecArrayQuobyteTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'quobyte'})
    rbd: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayRbd,
        kdsl.monitoring.v1.AlertmanagerSpecArrayRbdTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'rbd'})
    scaleIO: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIO,
        kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIOTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'scaleIO'})
    secret: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecArraySecret,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecretTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'secret'})
    storageos: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageos,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageosTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'storageos'})
    vsphereVolume: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayVsphereVolume,
        kdsl.monitoring.v1.AlertmanagerSpecArrayVsphereVolumeTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'vsphereVolume'})


@attr.s(kw_only=True)
class AlertmanagerSpecResources(K8sObjectBase):
    """
    | Define resources requests and limits for single Pods.
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class AlertmanagerSpecSecurityContextSeLinuxOptions(K8sObjectBase):
    """
    | The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    
    :param level: Level is SELinux level label that applies to the container.
    :param role: Role is a SELinux role label that applies to the container.
    :param type: Type is a SELinux type label that applies to the container.
    :param user: User is a SELinux user label that applies to the container.
    """
    level: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'level'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class AlertmanagerSpecSecurityContextArray(K8sObjectBase):
    """
    | Sysctl defines a kernel parameter to be set
    
    :param name: Name of a property to set
    :param value: Value of a property to set
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class AlertmanagerSpecSecurityContextWindowsOptions(K8sObjectBase):
    """
    | The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    
    :param gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is alpha-level and it is only honored by servers that enable the WindowsRunAsUserName feature flag.
    """
    gmsaCredentialSpec: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'gmsaCredentialSpec'})
    gmsaCredentialSpecName: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'gmsaCredentialSpecName'})
    runAsUserName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsUserName'})


@attr.s(kw_only=True)
class AlertmanagerSpecSecurityContext(K8sObjectBase):
    """
    | SecurityContext holds pod-level security attributes and common container settings. This defaults to the default PodSecurityContext.
    
    :param fsGroup: A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod: 
     1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw---- 
     If unset, the Kubelet will not modify the ownership and permissions of any volume.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param seLinuxOptions: The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param supplementalGroups: A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.
    :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    fsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'fsGroup'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextSeLinuxOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'seLinuxOptions'})
    supplementalGroups: Optional[Sequence[int]] = attr.ib(default=None,
        metadata={'yaml_name': 'supplementalGroups'})
    sysctls: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextArray,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'sysctls'})
    windowsOptions: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextWindowsOptions,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextWindowsOptionsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageEmptyDir(K8sObjectBase):
    """
    | EmptyDirVolumeSource to be used by the Prometheus StatefulSets. If specified, used in place of any volumeClaimTemplate. More info: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSource(K8sObjectBase):
    """
    | This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    
    :param kind: Kind is the type of resource being referenced
    :param name: Name is the name of resource being referenced
    :param apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    apiGroup: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiGroup'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateSpecResources(K8sObjectBase):
    """
    | Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArray(K8sObjectBase
    ):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateSpecSelector(K8sObjectBase):
    """
    | A label query over volumes to consider for binding.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateSpec(K8sObjectBase):
    """
    | Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param accessModes: AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param dataSource: This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    :param resources: Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    :param selector: A label query over volumes to consider for binding.
    :param storageClassName: Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
    :param volumeMode: volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. This is a beta feature.
    :param volumeName: VolumeName is the binding reference to the PersistentVolume backing this claim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    dataSource: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSource
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'dataSource'})
    resources: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecResources
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecResourcesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resources'})
    selector: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'selector'})
    storageClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageClassName'})
    volumeMode: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeMode'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateStatusArray(K8sObjectBase):
    """
    | PersistentVolumeClaimCondition contails details about state of pvc
    
    :param status: None
    :param type: PersistentVolumeClaimConditionType is a valid value of PersistentVolumeClaimCondition.Type
    :param lastProbeTime: Last time we probed the condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param message: Human-readable message indicating details about last transition.
    :param reason: Unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastProbeTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastProbeTime'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplateStatus(K8sObjectBase):
    """
    | Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param accessModes: AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param capacity: Represents the actual resources of the underlying volume.
    :param conditions: Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.
    :param phase: Phase represents the current phase of PersistentVolumeClaim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    capacity: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'capacity'})
    conditions: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatusArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatusArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'conditions'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorageVolumeClaimTemplate(K8sObjectBase):
    """
    | A PVC spec to be used by the Prometheus StatefulSets.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param spec: Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param status: Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Mapping[str, Any]] = attr.ib(default=None, metadata=
        {'yaml_name': 'metadata'})
    spec: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpec,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'spec'})
    status: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatus,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatusTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'status'})


@attr.s(kw_only=True)
class AlertmanagerSpecStorage(K8sObjectBase):
    """
    | Storage is the definition of how storage will be used by the Alertmanager instances.
    
    :param emptyDir: EmptyDirVolumeSource to be used by the Prometheus StatefulSets. If specified, used in place of any volumeClaimTemplate. More info: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir
    :param volumeClaimTemplate: A PVC spec to be used by the Prometheus StatefulSets.
    """
    emptyDir: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageEmptyDir,
        kdsl.monitoring.v1.AlertmanagerSpecStorageEmptyDirTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'emptyDir'})
    volumeClaimTemplate: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplate,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'volumeClaimTemplate'}
        )


@attr.s(kw_only=True)
class AlertmanagerSpecArrayAwsElasticBlockStore(K8sObjectBase):
    """
    | AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    
    :param volumeID: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore TODO: how do we prevent errors in the filesystem from compromising the machine
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).
    :param readOnly: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayAzureDisk(K8sObjectBase):
    """
    | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    
    :param diskName: The Name of the data disk in the blob storage
    :param diskURI: The URI the data disk in the blob storage
    :param cachingMode: Host Caching mode: None, Read Only, Read Write.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param kind: Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    diskName: str = attr.ib(metadata={'yaml_name': 'diskName'})
    diskURI: str = attr.ib(metadata={'yaml_name': 'diskURI'})
    cachingMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'cachingMode'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayAzureFile(K8sObjectBase):
    """
    | AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    
    :param secretName: the name of secret that contains Azure Storage Account Name and Key
    :param shareName: Share Name
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})
    shareName: str = attr.ib(metadata={'yaml_name': 'shareName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayCephfsSecretRef(K8sObjectBase):
    """
    | Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayCephfs(K8sObjectBase):
    """
    | CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    
    :param monitors: Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param path: Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretFile: Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretRef: Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param user: Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretFile'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayCephfsSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCephfsSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayCinderSecretRef(K8sObjectBase):
    """
    | Optional: points to a secret object containing parameters used to connect to OpenStack.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayCinder(K8sObjectBase):
    """
    | Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    
    :param volumeID: volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param secretRef: Optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayCinderSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCinderSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayConfigMapArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayConfigMap(K8sObjectBase):
    """
    | ConfigMap represents a configMap that should populate this volume
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMapArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMapArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayCsiNodePublishSecretRef(K8sObjectBase):
    """
    | NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayCsi(K8sObjectBase):
    """
    | CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    
    :param driver: Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.
    :param fsType: Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.
    :param nodePublishSecretRef: NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    :param readOnly: Specifies a read-only configuration for the volume. Defaults to false (read/write).
    :param volumeAttributes: VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    nodePublishSecretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayCsiNodePublishSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCsiNodePublishSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'nodePublishSecretRef'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    volumeAttributes: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeAttributes'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayDownwardAPIArrayFieldRef(K8sObjectBase):
    """
    | Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRef(K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayDownwardAPIArray(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayFieldRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayDownwardAPI(K8sObjectBase):
    """
    | DownwardAPI represents downward API about the pod that should populate this volume
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: Items is a list of downward API volume file
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayEmptyDir(K8sObjectBase):
    """
    | EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayFc(K8sObjectBase):
    """
    | FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. TODO: how do we prevent errors in the filesystem from compromising the machine
    :param lun: Optional: FC target lun number
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param targetWWNs: Optional: FC target worldwide names (WWNs)
    :param wwids: Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    lun: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'lun'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    targetWWNs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'targetWWNs'})
    wwids: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'wwids'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayFlexVolumeSecretRef(K8sObjectBase):
    """
    | Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayFlexVolume(K8sObjectBase):
    """
    | FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    
    :param driver: Driver is the name of the driver to use for this volume.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    :param options: Optional: Extra command options if any.
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    options: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'options'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolumeSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolumeSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayFlocker(K8sObjectBase):
    """
    | Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    
    :param datasetName: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated
    :param datasetUUID: UUID of the dataset. This is unique identifier of a Flocker dataset
    """
    datasetName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetName'})
    datasetUUID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetUUID'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayGcePersistentDisk(K8sObjectBase):
    """
    | GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    
    :param pdName: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk TODO: how do we prevent errors in the filesystem from compromising the machine
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    pdName: str = attr.ib(metadata={'yaml_name': 'pdName'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayGitRepo(K8sObjectBase):
    """
    | GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    
    :param repository: Repository URL
    :param directory: Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.
    :param revision: Commit hash for the specified revision.
    """
    repository: str = attr.ib(metadata={'yaml_name': 'repository'})
    directory: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'directory'})
    revision: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'revision'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayGlusterfs(K8sObjectBase):
    """
    | Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    
    :param endpoints: EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param path: Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param readOnly: ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints: str = attr.ib(metadata={'yaml_name': 'endpoints'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayHostPath(K8sObjectBase):
    """
    | HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
    
    :param path: Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    :param type: Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayIscsiSecretRef(K8sObjectBase):
    """
    | CHAP Secret for iSCSI target and initiator authentication
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayIscsi(K8sObjectBase):
    """
    | ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    
    :param iqn: Target iSCSI Qualified Name.
    :param lun: iSCSI Target Lun number.
    :param targetPortal: iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param chapAuthDiscovery: whether support iSCSI Discovery CHAP authentication
    :param chapAuthSession: whether support iSCSI Session CHAP authentication
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi TODO: how do we prevent errors in the filesystem from compromising the machine
    :param initiatorName: Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    :param iscsiInterface: iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    :param portals: iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    :param secretRef: CHAP Secret for iSCSI target and initiator authentication
    """
    iqn: str = attr.ib(metadata={'yaml_name': 'iqn'})
    lun: int = attr.ib(metadata={'yaml_name': 'lun'})
    targetPortal: str = attr.ib(metadata={'yaml_name': 'targetPortal'})
    chapAuthDiscovery: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthDiscovery'})
    chapAuthSession: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthSession'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    initiatorName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'initiatorName'})
    iscsiInterface: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'iscsiInterface'})
    portals: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'portals'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayIscsiSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayIscsiSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayNfs(K8sObjectBase):
    """
    | NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    
    :param path: Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param server: Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param readOnly: ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayPersistentVolumeClaim(K8sObjectBase):
    """
    | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    
    :param claimName: ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param readOnly: Will force the ReadOnly setting in VolumeMounts. Default false.
    """
    claimName: str = attr.ib(metadata={'yaml_name': 'claimName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayPhotonPersistentDisk(K8sObjectBase):
    """
    | PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    
    :param pdID: ID that identifies Photon Controller persistent disk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    pdID: str = attr.ib(metadata={'yaml_name': 'pdID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayPortworxVolume(K8sObjectBase):
    """
    | PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    
    :param volumeID: VolumeID uniquely identifies a Portworx volume
    :param fsType: FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayConfigMapArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayConfigMap(K8sObjectBase):
    """
    | information about the configMap data to project
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMapArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMapArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRef(K8sObjectBase
    ):
    """
    | Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef(
    K8sObjectBase):
    """
    | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayDownwardAPIArray(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRef
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayDownwardAPI(K8sObjectBase):
    """
    | information about the downwardAPI data to project
    
    :param items: Items is a list of DownwardAPIVolume file
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArraySecretArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArraySecret(K8sObjectBase):
    """
    | information about the secret data to project
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param optional: Specify whether the Secret or its key must be defined
    """
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecretArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecretArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArrayServiceAccountToken(K8sObjectBase):
    """
    | information about the serviceAccountToken data to project
    
    :param path: Path is the path relative to the mount point of the file to project the token into.
    :param audience: Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.
    :param expirationSeconds: ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    audience: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'audience'})
    expirationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'expirationSeconds'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjectedArray(K8sObjectBase):
    """
    | Projection that may be projected along with other supported volume types
    
    :param configMap: information about the configMap data to project
    :param downwardAPI: information about the downwardAPI data to project
    :param secret: information about the secret data to project
    :param serviceAccountToken: information about the serviceAccountToken data to project
    """
    configMap: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMap,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMapTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'configMap'})
    downwardAPI: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPI,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPITypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'downwardAPI'})
    secret: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecret,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecretTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secret'})
    serviceAccountToken: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayServiceAccountToken
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayServiceAccountTokenTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceAccountToken'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayProjected(K8sObjectBase):
    """
    | Items for all in one resources secrets, configmaps, and downward API
    
    :param sources: list of volume projections
    :param defaultMode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    sources: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'sources'})
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayQuobyte(K8sObjectBase):
    """
    | Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    
    :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes
    :param volume: Volume is a string that references an already created Quobyte volume by name.
    :param group: Group to map volume access to Default is no group
    :param readOnly: ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.
    :param tenant: Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin
    :param user: User to map volume access to Defaults to serivceaccount user
    """
    registry: str = attr.ib(metadata={'yaml_name': 'registry'})
    volume: str = attr.ib(metadata={'yaml_name': 'volume'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    tenant: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'tenant'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayRbdSecretRef(K8sObjectBase):
    """
    | SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayRbd(K8sObjectBase):
    """
    | RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    
    :param image: The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param monitors: A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd TODO: how do we prevent errors in the filesystem from compromising the machine
    :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param pool: The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param secretRef: SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param user: The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    image: str = attr.ib(metadata={'yaml_name': 'image'})
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    keyring: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyring'})
    pool: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'pool'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayRbdSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayRbdSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayScaleIOSecretRef(K8sObjectBase):
    """
    | SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayScaleIO(K8sObjectBase):
    """
    | ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    
    :param gateway: The host address of the ScaleIO API Gateway.
    :param secretRef: SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    :param system: The name of the storage system as configured in ScaleIO.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".
    :param protectionDomain: The name of the ScaleIO Protection Domain for the configured storage.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param sslEnabled: Flag to enable/disable SSL communication with Gateway, default false
    :param storageMode: Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    :param storagePool: The ScaleIO Storage Pool associated with the protection domain.
    :param volumeName: The name of a volume already created in the ScaleIO system that is associated with this volume source.
    """
    gateway: str = attr.ib(metadata={'yaml_name': 'gateway'})
    secretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIOSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIOSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})
    system: str = attr.ib(metadata={'yaml_name': 'system'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    protectionDomain: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'protectionDomain'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    sslEnabled: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'sslEnabled'})
    storageMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageMode'})
    storagePool: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePool'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class AlertmanagerSpecArraySecretArray(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class AlertmanagerSpecArraySecret(K8sObjectBase):
    """
    | Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param optional: Specify whether the Secret or its keys must be defined
    :param secretName: Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecretArray,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecretArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'items'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})
    secretName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretName'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStorageosSecretRef(K8sObjectBase):
    """
    | SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayStorageos(K8sObjectBase):
    """
    | StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    :param volumeName: VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    :param volumeNamespace: VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageosSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageosSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'secretRef'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})
    volumeNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'volumeNamespace'})


@attr.s(kw_only=True)
class AlertmanagerSpecArrayVsphereVolume(K8sObjectBase):
    """
    | VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    
    :param volumePath: Path that identifies vSphere volume vmdk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param storagePolicyID: Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.
    :param storagePolicyName: Storage Policy Based Management (SPBM) profile name.
    """
    volumePath: str = attr.ib(metadata={'yaml_name': 'volumePath'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    storagePolicyID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyID'})
    storagePolicyName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyName'})


@attr.s(kw_only=True)
class AlertmanagerSpec(K8sObjectBase):
    """
    | Specification of the desired behavior of the Alertmanager cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    
    :param additionalPeers: AdditionalPeers allows injecting a set of additional Alertmanagers to peer with to form a highly available cluster.
    :param affinity: If specified, the pod's scheduling constraints.
    :param baseImage: Base image that is used to deploy pods, without tag.
    :param configMaps: ConfigMaps is a list of ConfigMaps in the same namespace as the Alertmanager object, which shall be mounted into the Alertmanager Pods. The ConfigMaps are mounted into /etc/alertmanager/configmaps/<configmap-name>.
    :param configSecret: ConfigSecret is the name of a Kubernetes Secret in the same namespace as the Alertmanager object, which contains configuration for this Alertmanager instance. Defaults to 'alertmanager-<alertmanager-name>' The secret is mounted into /etc/alertmanager/config.
    :param containers: Containers allows injecting additional containers. This is meant to allow adding an authentication proxy to an Alertmanager pod.
    :param externalUrl: The external URL the Alertmanager instances will be available under. This is necessary to generate correct URLs. This is necessary if Alertmanager is not served from root of a DNS name.
    :param image: Image if specified has precedence over baseImage, tag and sha combinations. Specifying the version is still necessary to ensure the Prometheus Operator knows what version of Alertmanager is being configured.
    :param imagePullSecrets: An optional list of references to secrets in the same namespace to use for pulling prometheus and alertmanager images from registries see http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod
    :param initContainers: InitContainers allows adding initContainers to the pod definition. Those can be used to e.g. fetch secrets for injection into the Alertmanager configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ Using initContainers for any use case other then secret fetching is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice.
    :param listenLocal: ListenLocal makes the Alertmanager server listen on loopback, so that it does not bind against the Pod IP. Note this is only for the Alertmanager UI, not the gossip communication.
    :param logFormat: Log format for Alertmanager to be configured with.
    :param logLevel: Log level for Alertmanager to be configured with.
    :param nodeSelector: Define which Nodes the Pods are scheduled on.
    :param paused: If set to true all actions on the underlaying managed objects are not goint to be performed, except for delete actions.
    :param podMetadata: Standard object’s metadata. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata Metadata Labels and Annotations gets propagated to the prometheus pods.
    :param portName: Port name used for the pods and governing service. This defaults to web
    :param priorityClassName: Priority class assigned to the Pods
    :param replicas: Size is the expected size of the alertmanager cluster. The controller will eventually make the size of the running cluster equal to the expected size.
    :param resources: Define resources requests and limits for single Pods.
    :param retention: Time duration Alertmanager shall retain data for. Default is '120h', and must match the regular expression `[0-9]+(ms|s|m|h)` (milliseconds seconds minutes hours).
    :param routePrefix: The route prefix Alertmanager registers HTTP handlers for. This is useful, if using ExternalURL and a proxy is rewriting HTTP routes of a request, and the actual ExternalURL is still true, but the server serves requests under a different route prefix. For example for use with `kubectl proxy`.
    :param secrets: Secrets is a list of Secrets in the same namespace as the Alertmanager object, which shall be mounted into the Alertmanager Pods. The Secrets are mounted into /etc/alertmanager/secrets/<secret-name>.
    :param securityContext: SecurityContext holds pod-level security attributes and common container settings. This defaults to the default PodSecurityContext.
    :param serviceAccountName: ServiceAccountName is the name of the ServiceAccount to use to run the Prometheus Pods.
    :param sha: SHA of Alertmanager container image to be deployed. Defaults to the value of `version`. Similar to a tag, but the SHA explicitly deploys an immutable container image. Version and Tag are ignored if SHA is set.
    :param storage: Storage is the definition of how storage will be used by the Alertmanager instances.
    :param tag: Tag of Alertmanager container image to be deployed. Defaults to the value of `version`. Version is ignored if Tag is set.
    :param tolerations: If specified, the pod's tolerations.
    :param version: Version the cluster should be on.
    :param volumeMounts: VolumeMounts allows configuration of additional VolumeMounts on the output StatefulSet definition. VolumeMounts specified will be appended to other VolumeMounts in the alertmanager container, that are generated as a result of StorageSpec objects.
    :param volumes: Volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects.
    """
    additionalPeers: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'additionalPeers'})
    affinity: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'affinity'})
    baseImage: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'baseImage'})
    configMaps: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'configMaps'})
    configSecret: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'configSecret'})
    containers: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'containers'})
    externalUrl: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'externalUrl'})
    image: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'image'})
    imagePullSecrets: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'imagePullSecrets'})
    initContainers: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'initContainers'})
    listenLocal: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'listenLocal'})
    logFormat: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'logFormat'})
    logLevel: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'logLevel'})
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    paused: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'paused'})
    podMetadata: Optional[Mapping[str, Any]] = attr.ib(default=None,
        metadata={'yaml_name': 'podMetadata'})
    portName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'portName'})
    priorityClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'priorityClassName'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    resources: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecResources,
        kdsl.monitoring.v1.AlertmanagerSpecResourcesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resources'})
    retention: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'retention'})
    routePrefix: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'routePrefix'})
    secrets: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'secrets'})
    securityContext: Optional[Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContext,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'securityContext'})
    serviceAccountName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceAccountName'})
    sha: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'sha'})
    storage: Optional[Union[kdsl.monitoring.v1.AlertmanagerSpecStorage,
        kdsl.monitoring.v1.AlertmanagerSpecStorageTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'storage'})
    tag: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'tag'})
    tolerations: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'tolerations'})
    version: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'version'})
    volumeMounts: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'volumeMounts'})
    volumes: Optional[Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'volumes'})


@attr.s(kw_only=True)
class Alertmanager(K8sResourceBase):
    """
    | Alertmanager describes an Alertmanager cluster.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Specification of the desired behavior of the Alertmanager cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'monitoring.coreos.com/v1'
    kind: ClassVar[str] = 'Alertmanager'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.monitoring.v1.AlertmanagerSpec,
        kdsl.monitoring.v1.AlertmanagerSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


class ThanosRulerSpecAlertmanagersConfigOptionalTypedDict(TypedDict, total=
    (False)):
    name: str
    optional: bool


class ThanosRulerSpecAlertmanagersConfigTypedDict(
    ThanosRulerSpecAlertmanagersConfigOptionalTypedDict, total=(True)):
    key: str


class ThanosRulerSpecArrayArrayValueFromConfigMapKeyRefOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class ThanosRulerSpecArrayArrayValueFromConfigMapKeyRefTypedDict(
    ThanosRulerSpecArrayArrayValueFromConfigMapKeyRefOptionalTypedDict,
    total=(True)):
    key: str


class ThanosRulerSpecArrayArrayValueFromFieldRefOptionalTypedDict(TypedDict,
    total=(False)):
    apiVersion: str


class ThanosRulerSpecArrayArrayValueFromFieldRefTypedDict(
    ThanosRulerSpecArrayArrayValueFromFieldRefOptionalTypedDict, total=(True)):
    fieldPath: str


class ThanosRulerSpecArrayArrayValueFromResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class ThanosRulerSpecArrayArrayValueFromResourceFieldRefTypedDict(
    ThanosRulerSpecArrayArrayValueFromResourceFieldRefOptionalTypedDict,
    total=(True)):
    resource: str


class ThanosRulerSpecArrayArrayValueFromSecretKeyRefOptionalTypedDict(TypedDict
    , total=(False)):
    name: str
    optional: bool


class ThanosRulerSpecArrayArrayValueFromSecretKeyRefTypedDict(
    ThanosRulerSpecArrayArrayValueFromSecretKeyRefOptionalTypedDict, total=
    (True)):
    key: str


class ThanosRulerSpecArrayArrayValueFromTypedDict(TypedDict, total=(False)):
    configMapKeyRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromConfigMapKeyRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromConfigMapKeyRefTypedDict
        ]
    fieldRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromFieldRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromFieldRefTypedDict]
    resourceFieldRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromResourceFieldRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromResourceFieldRefTypedDict
        ]
    secretKeyRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromSecretKeyRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayArrayValueFromSecretKeyRefTypedDict
        ]


class ThanosRulerSpecArrayArrayOptionalTypedDict(TypedDict, total=(False)):
    mountPropagation: str
    readOnly: bool
    subPath: str
    subPathExpr: str


class ThanosRulerSpecArrayArrayTypedDict(
    ThanosRulerSpecArrayArrayOptionalTypedDict, total=(True)):
    mountPath: str
    name: str


class ThanosRulerSpecArrayArrayConfigMapRefTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class ThanosRulerSpecArrayArraySecretRefTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class ThanosRulerSpecArrayLifecyclePostStartExecTypedDict(TypedDict, total=
    (False)):
    command: Sequence[str]


class ThanosRulerSpecArrayLifecyclePostStartHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class ThanosRulerSpecArrayLifecyclePostStartHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class ThanosRulerSpecArrayLifecyclePostStartHttpGetTypedDict(
    ThanosRulerSpecArrayLifecyclePostStartHttpGetOptionalTypedDict, total=(
    True)):
    port: Any


class ThanosRulerSpecArrayLifecyclePostStartTcpSocketOptionalTypedDict(
    TypedDict, total=(False)):
    host: str


class ThanosRulerSpecArrayLifecyclePostStartTcpSocketTypedDict(
    ThanosRulerSpecArrayLifecyclePostStartTcpSocketOptionalTypedDict, total
    =(True)):
    port: Any


class ThanosRulerSpecArrayLifecyclePostStartTypedDict(TypedDict, total=(False)
    ):
    exec: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartExecTypedDict]
    httpGet: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartHttpGetTypedDict
        ]
    tcpSocket: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartTcpSocketTypedDict
        ]


class ThanosRulerSpecArrayLifecyclePreStopExecTypedDict(TypedDict, total=(
    False)):
    command: Sequence[str]


class ThanosRulerSpecArrayLifecyclePreStopHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class ThanosRulerSpecArrayLifecyclePreStopHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class ThanosRulerSpecArrayLifecyclePreStopHttpGetTypedDict(
    ThanosRulerSpecArrayLifecyclePreStopHttpGetOptionalTypedDict, total=(True)
    ):
    port: Any


class ThanosRulerSpecArrayLifecyclePreStopTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class ThanosRulerSpecArrayLifecyclePreStopTcpSocketTypedDict(
    ThanosRulerSpecArrayLifecyclePreStopTcpSocketOptionalTypedDict, total=(
    True)):
    port: Any


class ThanosRulerSpecArrayLifecyclePreStopTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopExecTypedDict]
    httpGet: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopHttpGetTypedDict
        ]
    tcpSocket: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopTcpSocketTypedDict
        ]


class ThanosRulerSpecArrayLifecycleTypedDict(TypedDict, total=(False)):
    postStart: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStart,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePostStartTypedDict]
    preStop: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStop,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLifecyclePreStopTypedDict]


class ThanosRulerSpecArrayLivenessProbeExecTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class ThanosRulerSpecArrayLivenessProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class ThanosRulerSpecArrayLivenessProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class ThanosRulerSpecArrayLivenessProbeHttpGetTypedDict(
    ThanosRulerSpecArrayLivenessProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class ThanosRulerSpecArrayLivenessProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class ThanosRulerSpecArrayLivenessProbeTcpSocketTypedDict(
    ThanosRulerSpecArrayLivenessProbeTcpSocketOptionalTypedDict, total=(True)):
    port: Any


class ThanosRulerSpecArrayLivenessProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayLivenessProbeTcpSocketTypedDict]
    timeoutSeconds: int


class ThanosRulerSpecArrayReadinessProbeExecTypedDict(TypedDict, total=(False)
    ):
    command: Sequence[str]


class ThanosRulerSpecArrayReadinessProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class ThanosRulerSpecArrayReadinessProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class ThanosRulerSpecArrayReadinessProbeHttpGetTypedDict(
    ThanosRulerSpecArrayReadinessProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class ThanosRulerSpecArrayReadinessProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class ThanosRulerSpecArrayReadinessProbeTcpSocketTypedDict(
    ThanosRulerSpecArrayReadinessProbeTcpSocketOptionalTypedDict, total=(True)
    ):
    port: Any


class ThanosRulerSpecArrayReadinessProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayReadinessProbeTcpSocketTypedDict
        ]
    timeoutSeconds: int


class ThanosRulerSpecArrayResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class ThanosRulerSpecArraySecurityContextCapabilitiesTypedDict(TypedDict,
    total=(False)):
    add: Sequence[str]
    drop: Sequence[str]


class ThanosRulerSpecArraySecurityContextSeLinuxOptionsTypedDict(TypedDict,
    total=(False)):
    level: str
    role: str
    type: str
    user: str


class ThanosRulerSpecArraySecurityContextWindowsOptionsTypedDict(TypedDict,
    total=(False)):
    gmsaCredentialSpec: str
    gmsaCredentialSpecName: str
    runAsUserName: str


class ThanosRulerSpecArraySecurityContextTypedDict(TypedDict, total=(False)):
    allowPrivilegeEscalation: bool
    capabilities: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextCapabilities,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextCapabilitiesTypedDict
        ]
    privileged: bool
    procMount: str
    readOnlyRootFilesystem: bool
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextSeLinuxOptionsTypedDict
        ]
    windowsOptions: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextWindowsOptions,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecurityContextWindowsOptionsTypedDict
        ]


class ThanosRulerSpecArrayStartupProbeExecTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class ThanosRulerSpecArrayStartupProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class ThanosRulerSpecArrayStartupProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGetArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class ThanosRulerSpecArrayStartupProbeHttpGetTypedDict(
    ThanosRulerSpecArrayStartupProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class ThanosRulerSpecArrayStartupProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class ThanosRulerSpecArrayStartupProbeTcpSocketTypedDict(
    ThanosRulerSpecArrayStartupProbeTcpSocketOptionalTypedDict, total=(True)):
    port: Any


class ThanosRulerSpecArrayStartupProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeExec,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGet,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeTcpSocket,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStartupProbeTcpSocketTypedDict]
    timeoutSeconds: int


class ThanosRulerSpecArrayOptionalTypedDict(TypedDict, total=(False)):
    awsElasticBlockStore: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayAwsElasticBlockStore,
        kdsl.monitoring.v1.ThanosRulerSpecArrayAwsElasticBlockStoreTypedDict]
    azureDisk: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayAzureDisk,
        kdsl.monitoring.v1.ThanosRulerSpecArrayAzureDiskTypedDict]
    azureFile: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayAzureFile,
        kdsl.monitoring.v1.ThanosRulerSpecArrayAzureFileTypedDict]
    cephfs: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCephfs,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCephfsTypedDict]
    cinder: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCinder,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCinderTypedDict]
    configMap: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMap,
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMapTypedDict]
    csi: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCsi,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCsiTypedDict]
    downwardAPI: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPI,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPITypedDict]
    emptyDir: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayEmptyDir,
        kdsl.monitoring.v1.ThanosRulerSpecArrayEmptyDirTypedDict]
    fc: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayFc,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFcTypedDict]
    flexVolume: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolume,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolumeTypedDict]
    flocker: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayFlocker,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlockerTypedDict]
    gcePersistentDisk: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayGcePersistentDisk,
        kdsl.monitoring.v1.ThanosRulerSpecArrayGcePersistentDiskTypedDict]
    gitRepo: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayGitRepo,
        kdsl.monitoring.v1.ThanosRulerSpecArrayGitRepoTypedDict]
    glusterfs: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayGlusterfs,
        kdsl.monitoring.v1.ThanosRulerSpecArrayGlusterfsTypedDict]
    hostPath: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayHostPath,
        kdsl.monitoring.v1.ThanosRulerSpecArrayHostPathTypedDict]
    iscsi: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayIscsi,
        kdsl.monitoring.v1.ThanosRulerSpecArrayIscsiTypedDict]
    nfs: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayNfs,
        kdsl.monitoring.v1.ThanosRulerSpecArrayNfsTypedDict]
    persistentVolumeClaim: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayPersistentVolumeClaim,
        kdsl.monitoring.v1.ThanosRulerSpecArrayPersistentVolumeClaimTypedDict]
    photonPersistentDisk: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayPhotonPersistentDisk,
        kdsl.monitoring.v1.ThanosRulerSpecArrayPhotonPersistentDiskTypedDict]
    portworxVolume: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayPortworxVolume,
        kdsl.monitoring.v1.ThanosRulerSpecArrayPortworxVolumeTypedDict]
    projected: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayProjected,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedTypedDict]
    quobyte: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayQuobyte,
        kdsl.monitoring.v1.ThanosRulerSpecArrayQuobyteTypedDict]
    rbd: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayRbd,
        kdsl.monitoring.v1.ThanosRulerSpecArrayRbdTypedDict]
    scaleIO: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIO,
        kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIOTypedDict]
    secret: Union[kdsl.monitoring.v1.ThanosRulerSpecArraySecret,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecretTypedDict]
    storageos: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayStorageos,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageosTypedDict]
    vsphereVolume: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayVsphereVolume,
        kdsl.monitoring.v1.ThanosRulerSpecArrayVsphereVolumeTypedDict]


class ThanosRulerSpecArrayTypedDict(ThanosRulerSpecArrayOptionalTypedDict,
    total=(True)):
    name: str


class ThanosRulerSpecObjectStorageConfigOptionalTypedDict(TypedDict, total=
    (False)):
    name: str
    optional: bool


class ThanosRulerSpecObjectStorageConfigTypedDict(
    ThanosRulerSpecObjectStorageConfigOptionalTypedDict, total=(True)):
    key: str


class ThanosRulerSpecResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class ThanosRulerSpecRuleNamespaceSelectorArrayOptionalTypedDict(TypedDict,
    total=(False)):
    values: Sequence[str]


class ThanosRulerSpecRuleNamespaceSelectorArrayTypedDict(
    ThanosRulerSpecRuleNamespaceSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class ThanosRulerSpecRuleNamespaceSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelectorArray,
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class ThanosRulerSpecRuleSelectorArrayOptionalTypedDict(TypedDict, total=(
    False)):
    values: Sequence[str]


class ThanosRulerSpecRuleSelectorArrayTypedDict(
    ThanosRulerSpecRuleSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class ThanosRulerSpecRuleSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelectorArray,
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class ThanosRulerSpecStorageEmptyDirTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSourceOptionalTypedDict(
    TypedDict, total=(False)):
    apiGroup: str


class ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict(
    ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSourceOptionalTypedDict,
    total=(True)):
    kind: str
    name: str


class ThanosRulerSpecStorageVolumeClaimTemplateSpecResourcesTypedDict(TypedDict
    , total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict(
    ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArray
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ThanosRulerSpecStorageVolumeClaimTemplateSpecTypedDict(TypedDict,
    total=(False)):
    accessModes: Sequence[str]
    dataSource: Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSource
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict
        ]
    resources: Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecResources
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecResourcesTypedDict
        ]
    selector: Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelector
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecSelectorTypedDict
        ]
    storageClassName: str
    volumeMode: str
    volumeName: str


class ThanosRulerSpecStorageVolumeClaimTemplateStatusArrayOptionalTypedDict(
    TypedDict, total=(False)):
    lastProbeTime: str
    lastTransitionTime: str
    message: str
    reason: str


class ThanosRulerSpecStorageVolumeClaimTemplateStatusArrayTypedDict(
    ThanosRulerSpecStorageVolumeClaimTemplateStatusArrayOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class ThanosRulerSpecStorageVolumeClaimTemplateStatusTypedDict(TypedDict,
    total=(False)):
    accessModes: Sequence[str]
    capacity: Mapping[str, str]
    conditions: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatusArray
        ,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatusArrayTypedDict
        ]]
    phase: str


class ThanosRulerSpecStorageVolumeClaimTemplateTypedDict(TypedDict, total=(
    False)):
    apiVersion: str
    kind: str
    metadata: Mapping[str, Any]
    spec: Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpec,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateSpecTypedDict
        ]
    status: Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatus,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateStatusTypedDict
        ]


class ThanosRulerSpecStorageTypedDict(TypedDict, total=(False)):
    emptyDir: Union[kdsl.monitoring.v1.ThanosRulerSpecStorageEmptyDir,
        kdsl.monitoring.v1.ThanosRulerSpecStorageEmptyDirTypedDict]
    volumeClaimTemplate: Union[
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplate,
        kdsl.monitoring.v1.ThanosRulerSpecStorageVolumeClaimTemplateTypedDict]


class ThanosRulerSpecTracingConfigOptionalTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class ThanosRulerSpecTracingConfigTypedDict(
    ThanosRulerSpecTracingConfigOptionalTypedDict, total=(True)):
    key: str


class ThanosRulerSpecArrayAwsElasticBlockStoreOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class ThanosRulerSpecArrayAwsElasticBlockStoreTypedDict(
    ThanosRulerSpecArrayAwsElasticBlockStoreOptionalTypedDict, total=(True)):
    volumeID: str


class ThanosRulerSpecArrayAzureDiskOptionalTypedDict(TypedDict, total=(False)):
    cachingMode: str
    fsType: str
    kind: str
    readOnly: bool


class ThanosRulerSpecArrayAzureDiskTypedDict(
    ThanosRulerSpecArrayAzureDiskOptionalTypedDict, total=(True)):
    diskName: str
    diskURI: str


class ThanosRulerSpecArrayAzureFileOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class ThanosRulerSpecArrayAzureFileTypedDict(
    ThanosRulerSpecArrayAzureFileOptionalTypedDict, total=(True)):
    secretName: str
    shareName: str


class ThanosRulerSpecArrayCephfsSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class ThanosRulerSpecArrayCephfsOptionalTypedDict(TypedDict, total=(False)):
    path: str
    readOnly: bool
    secretFile: str
    secretRef: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCephfsSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCephfsSecretRefTypedDict]
    user: str


class ThanosRulerSpecArrayCephfsTypedDict(
    ThanosRulerSpecArrayCephfsOptionalTypedDict, total=(True)):
    monitors: Sequence[str]


class ThanosRulerSpecArrayCinderSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class ThanosRulerSpecArrayCinderOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayCinderSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCinderSecretRefTypedDict]


class ThanosRulerSpecArrayCinderTypedDict(
    ThanosRulerSpecArrayCinderOptionalTypedDict, total=(True)):
    volumeID: str


class ThanosRulerSpecArrayConfigMapArrayOptionalTypedDict(TypedDict, total=
    (False)):
    mode: int


class ThanosRulerSpecArrayConfigMapArrayTypedDict(
    ThanosRulerSpecArrayConfigMapArrayOptionalTypedDict, total=(True)):
    key: str
    path: str


class ThanosRulerSpecArrayConfigMapTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMapArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayConfigMapArrayTypedDict]]
    name: str
    optional: bool


class ThanosRulerSpecArrayCsiNodePublishSecretRefTypedDict(TypedDict, total
    =(False)):
    name: str


class ThanosRulerSpecArrayCsiOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    nodePublishSecretRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayCsiNodePublishSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayCsiNodePublishSecretRefTypedDict
        ]
    readOnly: bool
    volumeAttributes: Mapping[str, str]


class ThanosRulerSpecArrayCsiTypedDict(ThanosRulerSpecArrayCsiOptionalTypedDict
    , total=(True)):
    driver: str


class ThanosRulerSpecArrayDownwardAPIArrayFieldRefOptionalTypedDict(TypedDict,
    total=(False)):
    apiVersion: str


class ThanosRulerSpecArrayDownwardAPIArrayFieldRefTypedDict(
    ThanosRulerSpecArrayDownwardAPIArrayFieldRefOptionalTypedDict, total=(True)
    ):
    fieldPath: str


class ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRefTypedDict(
    ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict,
    total=(True)):
    resource: str


class ThanosRulerSpecArrayDownwardAPIArrayOptionalTypedDict(TypedDict,
    total=(False)):
    fieldRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayFieldRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayFieldRefTypedDict
        ]
    mode: int
    resourceFieldRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]


class ThanosRulerSpecArrayDownwardAPIArrayTypedDict(
    ThanosRulerSpecArrayDownwardAPIArrayOptionalTypedDict, total=(True)):
    path: str


class ThanosRulerSpecArrayDownwardAPITypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayDownwardAPIArrayTypedDict]]


class ThanosRulerSpecArrayEmptyDirTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class ThanosRulerSpecArrayFcTypedDict(TypedDict, total=(False)):
    fsType: str
    lun: int
    readOnly: bool
    targetWWNs: Sequence[str]
    wwids: Sequence[str]


class ThanosRulerSpecArrayFlexVolumeSecretRefTypedDict(TypedDict, total=(False)
    ):
    name: str


class ThanosRulerSpecArrayFlexVolumeOptionalTypedDict(TypedDict, total=(False)
    ):
    fsType: str
    options: Mapping[str, str]
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolumeSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayFlexVolumeSecretRefTypedDict]


class ThanosRulerSpecArrayFlexVolumeTypedDict(
    ThanosRulerSpecArrayFlexVolumeOptionalTypedDict, total=(True)):
    driver: str


class ThanosRulerSpecArrayFlockerTypedDict(TypedDict, total=(False)):
    datasetName: str
    datasetUUID: str


class ThanosRulerSpecArrayGcePersistentDiskOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class ThanosRulerSpecArrayGcePersistentDiskTypedDict(
    ThanosRulerSpecArrayGcePersistentDiskOptionalTypedDict, total=(True)):
    pdName: str


class ThanosRulerSpecArrayGitRepoOptionalTypedDict(TypedDict, total=(False)):
    directory: str
    revision: str


class ThanosRulerSpecArrayGitRepoTypedDict(
    ThanosRulerSpecArrayGitRepoOptionalTypedDict, total=(True)):
    repository: str


class ThanosRulerSpecArrayGlusterfsOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class ThanosRulerSpecArrayGlusterfsTypedDict(
    ThanosRulerSpecArrayGlusterfsOptionalTypedDict, total=(True)):
    endpoints: str
    path: str


class ThanosRulerSpecArrayHostPathOptionalTypedDict(TypedDict, total=(False)):
    type: str


class ThanosRulerSpecArrayHostPathTypedDict(
    ThanosRulerSpecArrayHostPathOptionalTypedDict, total=(True)):
    path: str


class ThanosRulerSpecArrayIscsiSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class ThanosRulerSpecArrayIscsiOptionalTypedDict(TypedDict, total=(False)):
    chapAuthDiscovery: bool
    chapAuthSession: bool
    fsType: str
    initiatorName: str
    iscsiInterface: str
    portals: Sequence[str]
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayIscsiSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayIscsiSecretRefTypedDict]


class ThanosRulerSpecArrayIscsiTypedDict(
    ThanosRulerSpecArrayIscsiOptionalTypedDict, total=(True)):
    iqn: str
    lun: int
    targetPortal: str


class ThanosRulerSpecArrayNfsOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class ThanosRulerSpecArrayNfsTypedDict(ThanosRulerSpecArrayNfsOptionalTypedDict
    , total=(True)):
    path: str
    server: str


class ThanosRulerSpecArrayPersistentVolumeClaimOptionalTypedDict(TypedDict,
    total=(False)):
    readOnly: bool


class ThanosRulerSpecArrayPersistentVolumeClaimTypedDict(
    ThanosRulerSpecArrayPersistentVolumeClaimOptionalTypedDict, total=(True)):
    claimName: str


class ThanosRulerSpecArrayPhotonPersistentDiskOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str


class ThanosRulerSpecArrayPhotonPersistentDiskTypedDict(
    ThanosRulerSpecArrayPhotonPersistentDiskOptionalTypedDict, total=(True)):
    pdID: str


class ThanosRulerSpecArrayPortworxVolumeOptionalTypedDict(TypedDict, total=
    (False)):
    fsType: str
    readOnly: bool


class ThanosRulerSpecArrayPortworxVolumeTypedDict(
    ThanosRulerSpecArrayPortworxVolumeOptionalTypedDict, total=(True)):
    volumeID: str


class ThanosRulerSpecArrayProjectedArrayConfigMapArrayOptionalTypedDict(
    TypedDict, total=(False)):
    mode: int


class ThanosRulerSpecArrayProjectedArrayConfigMapArrayTypedDict(
    ThanosRulerSpecArrayProjectedArrayConfigMapArrayOptionalTypedDict,
    total=(True)):
    key: str
    path: str


class ThanosRulerSpecArrayProjectedArrayConfigMapTypedDict(TypedDict, total
    =(False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMapArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMapArrayTypedDict
        ]]
    name: str
    optional: bool


class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    apiVersion: str


class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict(
    ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRefOptionalTypedDict
    , total=(True)):
    fieldPath: str


class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict(
    ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict
    , total=(True)):
    resource: str


class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayOptionalTypedDict(
    TypedDict, total=(False)):
    fieldRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRef
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict
        ]
    mode: int
    resourceFieldRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]


class ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayTypedDict(
    ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayOptionalTypedDict,
    total=(True)):
    path: str


class ThanosRulerSpecArrayProjectedArrayDownwardAPITypedDict(TypedDict,
    total=(False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPIArrayTypedDict
        ]]


class ThanosRulerSpecArrayProjectedArraySecretArrayOptionalTypedDict(TypedDict,
    total=(False)):
    mode: int


class ThanosRulerSpecArrayProjectedArraySecretArrayTypedDict(
    ThanosRulerSpecArrayProjectedArraySecretArrayOptionalTypedDict, total=(
    True)):
    key: str
    path: str


class ThanosRulerSpecArrayProjectedArraySecretTypedDict(TypedDict, total=(
    False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecretArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecretArrayTypedDict
        ]]
    name: str
    optional: bool


class ThanosRulerSpecArrayProjectedArrayServiceAccountTokenOptionalTypedDict(
    TypedDict, total=(False)):
    audience: str
    expirationSeconds: int


class ThanosRulerSpecArrayProjectedArrayServiceAccountTokenTypedDict(
    ThanosRulerSpecArrayProjectedArrayServiceAccountTokenOptionalTypedDict,
    total=(True)):
    path: str


class ThanosRulerSpecArrayProjectedArrayTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMap,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayConfigMapTypedDict
        ]
    downwardAPI: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPI,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayDownwardAPITypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecret,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArraySecretTypedDict]
    serviceAccountToken: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayServiceAccountToken
        ,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayServiceAccountTokenTypedDict
        ]


class ThanosRulerSpecArrayProjectedOptionalTypedDict(TypedDict, total=(False)):
    defaultMode: int


class ThanosRulerSpecArrayProjectedTypedDict(
    ThanosRulerSpecArrayProjectedOptionalTypedDict, total=(True)):
    sources: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayProjectedArrayTypedDict]]


class ThanosRulerSpecArrayQuobyteOptionalTypedDict(TypedDict, total=(False)):
    group: str
    readOnly: bool
    tenant: str
    user: str


class ThanosRulerSpecArrayQuobyteTypedDict(
    ThanosRulerSpecArrayQuobyteOptionalTypedDict, total=(True)):
    registry: str
    volume: str


class ThanosRulerSpecArrayRbdSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class ThanosRulerSpecArrayRbdOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    keyring: str
    pool: str
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.ThanosRulerSpecArrayRbdSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayRbdSecretRefTypedDict]
    user: str


class ThanosRulerSpecArrayRbdTypedDict(ThanosRulerSpecArrayRbdOptionalTypedDict
    , total=(True)):
    image: str
    monitors: Sequence[str]


class ThanosRulerSpecArrayScaleIOSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class ThanosRulerSpecArrayScaleIOOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    protectionDomain: str
    readOnly: bool
    sslEnabled: bool
    storageMode: str
    storagePool: str
    volumeName: str


class ThanosRulerSpecArrayScaleIOTypedDict(
    ThanosRulerSpecArrayScaleIOOptionalTypedDict, total=(True)):
    gateway: str
    secretRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIOSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayScaleIOSecretRefTypedDict]
    system: str


class ThanosRulerSpecArraySecretArrayOptionalTypedDict(TypedDict, total=(False)
    ):
    mode: int


class ThanosRulerSpecArraySecretArrayTypedDict(
    ThanosRulerSpecArraySecretArrayOptionalTypedDict, total=(True)):
    key: str
    path: str


class ThanosRulerSpecArraySecretTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArraySecretArray,
        kdsl.monitoring.v1.ThanosRulerSpecArraySecretArrayTypedDict]]
    optional: bool
    secretName: str


class ThanosRulerSpecArrayStorageosSecretRefTypedDict(TypedDict, total=(False)
    ):
    name: str


class ThanosRulerSpecArrayStorageosTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageosSecretRef,
        kdsl.monitoring.v1.ThanosRulerSpecArrayStorageosSecretRefTypedDict]
    volumeName: str
    volumeNamespace: str


class ThanosRulerSpecArrayVsphereVolumeOptionalTypedDict(TypedDict, total=(
    False)):
    fsType: str
    storagePolicyID: str
    storagePolicyName: str


class ThanosRulerSpecArrayVsphereVolumeTypedDict(
    ThanosRulerSpecArrayVsphereVolumeOptionalTypedDict, total=(True)):
    volumePath: str


class ThanosRulerSpecOptionalTypedDict(TypedDict, total=(False)):
    alertDropLabels: Sequence[str]
    alertmanagersConfig: Union[
        kdsl.monitoring.v1.ThanosRulerSpecAlertmanagersConfig,
        kdsl.monitoring.v1.ThanosRulerSpecAlertmanagersConfigTypedDict]
    alertmanagersUrl: str
    containers: Sequence[Union[kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]
    enforcedNamespaceLabel: str
    evaluationInterval: str
    image: str
    imagePullSecrets: Sequence[Union[
        kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]
    initContainers: Sequence[Union[kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]
    labels: Mapping[str, str]
    listenLocal: bool
    logFormat: str
    logLevel: str
    objectStorageConfig: Union[
        kdsl.monitoring.v1.ThanosRulerSpecObjectStorageConfig,
        kdsl.monitoring.v1.ThanosRulerSpecObjectStorageConfigTypedDict]
    paused: bool
    podMetadata: Mapping[str, Any]
    portName: str
    replicas: int
    resources: Union[kdsl.monitoring.v1.ThanosRulerSpecResources,
        kdsl.monitoring.v1.ThanosRulerSpecResourcesTypedDict]
    retention: str
    ruleNamespaceSelector: Union[
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelector,
        kdsl.monitoring.v1.ThanosRulerSpecRuleNamespaceSelectorTypedDict]
    ruleSelector: Union[kdsl.monitoring.v1.ThanosRulerSpecRuleSelector,
        kdsl.monitoring.v1.ThanosRulerSpecRuleSelectorTypedDict]
    storage: Union[kdsl.monitoring.v1.ThanosRulerSpecStorage,
        kdsl.monitoring.v1.ThanosRulerSpecStorageTypedDict]
    tracingConfig: Union[kdsl.monitoring.v1.ThanosRulerSpecTracingConfig,
        kdsl.monitoring.v1.ThanosRulerSpecTracingConfigTypedDict]
    volumes: Sequence[Union[kdsl.monitoring.v1.ThanosRulerSpecArray,
        kdsl.monitoring.v1.ThanosRulerSpecArrayTypedDict]]


class ThanosRulerSpecTypedDict(ThanosRulerSpecOptionalTypedDict, total=(True)):
    queryEndpoints: Sequence[str]


class ThanosRulerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class ThanosRulerTypedDict(ThanosRulerOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.monitoring.v1.ThanosRulerSpec,
        kdsl.monitoring.v1.ThanosRulerSpecTypedDict]


class ServiceMonitorSpecArrayBasicAuthPasswordOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayBasicAuthPasswordTypedDict(
    ServiceMonitorSpecArrayBasicAuthPasswordOptionalTypedDict, total=(True)):
    key: str


class ServiceMonitorSpecArrayBasicAuthUsernameOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayBasicAuthUsernameTypedDict(
    ServiceMonitorSpecArrayBasicAuthUsernameOptionalTypedDict, total=(True)):
    key: str


class ServiceMonitorSpecArrayBasicAuthTypedDict(TypedDict, total=(False)):
    password: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthPassword,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthPasswordTypedDict]
    username: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthUsername,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthUsernameTypedDict]


class ServiceMonitorSpecArrayBearerTokenSecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayBearerTokenSecretTypedDict(
    ServiceMonitorSpecArrayBearerTokenSecretOptionalTypedDict, total=(True)):
    key: str


class ServiceMonitorSpecArrayArrayTypedDict(TypedDict, total=(False)):
    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    sourceLabels: Sequence[str]
    targetLabel: str


class ServiceMonitorSpecArrayTlsConfigCaConfigMapOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayTlsConfigCaConfigMapTypedDict(
    ServiceMonitorSpecArrayTlsConfigCaConfigMapOptionalTypedDict, total=(True)
    ):
    key: str


class ServiceMonitorSpecArrayTlsConfigCaSecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayTlsConfigCaSecretTypedDict(
    ServiceMonitorSpecArrayTlsConfigCaSecretOptionalTypedDict, total=(True)):
    key: str


class ServiceMonitorSpecArrayTlsConfigCaTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaConfigMap,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaConfigMapTypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaSecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaSecretTypedDict]


class ServiceMonitorSpecArrayTlsConfigCertConfigMapOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayTlsConfigCertConfigMapTypedDict(
    ServiceMonitorSpecArrayTlsConfigCertConfigMapOptionalTypedDict, total=(
    True)):
    key: str


class ServiceMonitorSpecArrayTlsConfigCertSecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayTlsConfigCertSecretTypedDict(
    ServiceMonitorSpecArrayTlsConfigCertSecretOptionalTypedDict, total=(True)):
    key: str


class ServiceMonitorSpecArrayTlsConfigCertTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertConfigMap,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertConfigMapTypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertSecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertSecretTypedDict]


class ServiceMonitorSpecArrayTlsConfigKeySecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class ServiceMonitorSpecArrayTlsConfigKeySecretTypedDict(
    ServiceMonitorSpecArrayTlsConfigKeySecretOptionalTypedDict, total=(True)):
    key: str


class ServiceMonitorSpecArrayTlsConfigTypedDict(TypedDict, total=(False)):
    ca: Union[kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCa,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCaTypedDict]
    caFile: str
    cert: Union[kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCert,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigCertTypedDict]
    certFile: str
    insecureSkipVerify: bool
    keyFile: str
    keySecret: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigKeySecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigKeySecretTypedDict]
    serverName: str


class ServiceMonitorSpecArrayTypedDict(TypedDict, total=(False)):
    basicAuth: Union[kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuth,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBasicAuthTypedDict]
    bearerTokenFile: str
    bearerTokenSecret: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBearerTokenSecret,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayBearerTokenSecretTypedDict]
    honorLabels: bool
    honorTimestamps: bool
    interval: str
    metricRelabelings: Sequence[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArray,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArrayTypedDict]]
    params: Mapping[str, Sequence[str]]
    path: str
    port: str
    proxyUrl: str
    relabelings: Sequence[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArray,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayArrayTypedDict]]
    scheme: str
    scrapeTimeout: str
    targetPort: Any
    tlsConfig: Union[kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfig,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTlsConfigTypedDict]


class ServiceMonitorSpecNamespaceSelectorTypedDict(TypedDict, total=(False)):
    any: bool
    matchNames: Sequence[str]


class ServiceMonitorSpecSelectorArrayOptionalTypedDict(TypedDict, total=(False)
    ):
    values: Sequence[str]


class ServiceMonitorSpecSelectorArrayTypedDict(
    ServiceMonitorSpecSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class ServiceMonitorSpecSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.ServiceMonitorSpecSelectorArray,
        kdsl.monitoring.v1.ServiceMonitorSpecSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class ServiceMonitorSpecOptionalTypedDict(TypedDict, total=(False)):
    jobLabel: str
    namespaceSelector: Union[
        kdsl.monitoring.v1.ServiceMonitorSpecNamespaceSelector,
        kdsl.monitoring.v1.ServiceMonitorSpecNamespaceSelectorTypedDict]
    podTargetLabels: Sequence[str]
    sampleLimit: int
    targetLabels: Sequence[str]


class ServiceMonitorSpecTypedDict(ServiceMonitorSpecOptionalTypedDict,
    total=(True)):
    endpoints: Sequence[Union[kdsl.monitoring.v1.ServiceMonitorSpecArray,
        kdsl.monitoring.v1.ServiceMonitorSpecArrayTypedDict]]
    selector: Union[kdsl.monitoring.v1.ServiceMonitorSpecSelector,
        kdsl.monitoring.v1.ServiceMonitorSpecSelectorTypedDict]


class ServiceMonitorOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class ServiceMonitorTypedDict(ServiceMonitorOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.monitoring.v1.ServiceMonitorSpec,
        kdsl.monitoring.v1.ServiceMonitorSpecTypedDict]


class PrometheusRuleSpecArrayArrayOptionalTypedDict(TypedDict, total=(False)):
    alert: str
    annotations: Mapping[str, str]
    for_: str
    labels: Mapping[str, str]
    record: str


class PrometheusRuleSpecArrayArrayTypedDict(
    PrometheusRuleSpecArrayArrayOptionalTypedDict, total=(True)):
    expr: Any


class PrometheusRuleSpecArrayOptionalTypedDict(TypedDict, total=(False)):
    interval: str
    partial_response_strategy: str


class PrometheusRuleSpecArrayTypedDict(PrometheusRuleSpecArrayOptionalTypedDict
    , total=(True)):
    name: str
    rules: Sequence[Union[kdsl.monitoring.v1.PrometheusRuleSpecArrayArray,
        kdsl.monitoring.v1.PrometheusRuleSpecArrayArrayTypedDict]]


class PrometheusRuleSpecTypedDict(TypedDict, total=(False)):
    groups: Sequence[Union[kdsl.monitoring.v1.PrometheusRuleSpecArray,
        kdsl.monitoring.v1.PrometheusRuleSpecArrayTypedDict]]


class PrometheusRuleOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class PrometheusRuleTypedDict(PrometheusRuleOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.monitoring.v1.PrometheusRuleSpec,
        kdsl.monitoring.v1.PrometheusRuleSpecTypedDict]


class PrometheusSpecAdditionalAlertManagerConfigsOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecAdditionalAlertManagerConfigsTypedDict(
    PrometheusSpecAdditionalAlertManagerConfigsOptionalTypedDict, total=(True)
    ):
    key: str


class PrometheusSpecAdditionalAlertRelabelConfigsOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecAdditionalAlertRelabelConfigsTypedDict(
    PrometheusSpecAdditionalAlertRelabelConfigsOptionalTypedDict, total=(True)
    ):
    key: str


class PrometheusSpecAdditionalScrapeConfigsOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecAdditionalScrapeConfigsTypedDict(
    PrometheusSpecAdditionalScrapeConfigsOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict(
    PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict,
    total=(True)):
    key: str
    operator: str


class PrometheusSpecAffinityNodeAffinityArrayPreferenceTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]


class PrometheusSpecAffinityNodeAffinityArrayTypedDict(TypedDict, total=(True)
    ):
    preference: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreference,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ]
    weight: int


class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict(
    PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]


class PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict(
    TypedDict, total=(True)):
    nodeSelectorTerms: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]]


class PrometheusSpecAffinityNodeAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityArrayTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]


class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class PrometheusSpecAffinityPodAffinityArrayPodAffinityTermTypedDict(
    PrometheusSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict,
    total=(True)):
    topologyKey: str


class PrometheusSpecAffinityPodAffinityArrayOptionalTypedDict(TypedDict,
    total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelector,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class PrometheusSpecAffinityPodAffinityArrayTypedDict(
    PrometheusSpecAffinityPodAffinityArrayOptionalTypedDict, total=(True)):
    topologyKey: str


class PrometheusSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict(
    PrometheusSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict,
    total=(True)):
    key: str
    operator: str


class PrometheusSpecAffinityPodAffinityArrayLabelSelectorTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecAffinityPodAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityArrayTypedDict]]


class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermTypedDict(
    PrometheusSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict,
    total=(True)):
    topologyKey: str


class PrometheusSpecAffinityPodAntiAffinityArrayOptionalTypedDict(TypedDict,
    total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class PrometheusSpecAffinityPodAntiAffinityArrayTypedDict(
    PrometheusSpecAffinityPodAntiAffinityArrayOptionalTypedDict, total=(True)):
    topologyKey: str


class PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict(
    PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecAffinityPodAntiAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayTypedDict]
        ]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityArrayTypedDict]
        ]


class PrometheusSpecAffinityTypedDict(TypedDict, total=(False)):
    nodeAffinity: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityNodeAffinityTypedDict]
    podAffinity: Union[kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAffinityTypedDict]
    podAntiAffinity: Union[
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityPodAntiAffinityTypedDict]


class PrometheusSpecAlertingArrayTlsConfigCaConfigMapOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecAlertingArrayTlsConfigCaConfigMapTypedDict(
    PrometheusSpecAlertingArrayTlsConfigCaConfigMapOptionalTypedDict, total
    =(True)):
    key: str


class PrometheusSpecAlertingArrayTlsConfigCaSecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecAlertingArrayTlsConfigCaSecretTypedDict(
    PrometheusSpecAlertingArrayTlsConfigCaSecretOptionalTypedDict, total=(True)
    ):
    key: str


class PrometheusSpecAlertingArrayTlsConfigCaTypedDict(TypedDict, total=(False)
    ):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaConfigMap,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaConfigMapTypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaSecret,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaSecretTypedDict
        ]


class PrometheusSpecAlertingArrayTlsConfigCertConfigMapOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecAlertingArrayTlsConfigCertConfigMapTypedDict(
    PrometheusSpecAlertingArrayTlsConfigCertConfigMapOptionalTypedDict,
    total=(True)):
    key: str


class PrometheusSpecAlertingArrayTlsConfigCertSecretOptionalTypedDict(TypedDict
    , total=(False)):
    name: str
    optional: bool


class PrometheusSpecAlertingArrayTlsConfigCertSecretTypedDict(
    PrometheusSpecAlertingArrayTlsConfigCertSecretOptionalTypedDict, total=
    (True)):
    key: str


class PrometheusSpecAlertingArrayTlsConfigCertTypedDict(TypedDict, total=(
    False)):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertConfigMap,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertConfigMapTypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertSecret,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertSecretTypedDict
        ]


class PrometheusSpecAlertingArrayTlsConfigKeySecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecAlertingArrayTlsConfigKeySecretTypedDict(
    PrometheusSpecAlertingArrayTlsConfigKeySecretOptionalTypedDict, total=(
    True)):
    key: str


class PrometheusSpecAlertingArrayTlsConfigTypedDict(TypedDict, total=(False)):
    ca: Union[kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCa,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCaTypedDict]
    caFile: str
    cert: Union[kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCert,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigCertTypedDict]
    certFile: str
    insecureSkipVerify: bool
    keyFile: str
    keySecret: Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigKeySecret,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigKeySecretTypedDict
        ]
    serverName: str


class PrometheusSpecAlertingArrayOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    bearerTokenFile: str
    pathPrefix: str
    scheme: str
    tlsConfig: Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfig,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTlsConfigTypedDict]


class PrometheusSpecAlertingArrayTypedDict(
    PrometheusSpecAlertingArrayOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    port: Any


class PrometheusSpecAlertingTypedDict(TypedDict, total=(True)):
    alertmanagers: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecAlertingArray,
        kdsl.monitoring.v1.PrometheusSpecAlertingArrayTypedDict]]


class PrometheusSpecApiserverConfigBasicAuthPasswordOptionalTypedDict(TypedDict
    , total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigBasicAuthPasswordTypedDict(
    PrometheusSpecApiserverConfigBasicAuthPasswordOptionalTypedDict, total=
    (True)):
    key: str


class PrometheusSpecApiserverConfigBasicAuthUsernameOptionalTypedDict(TypedDict
    , total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigBasicAuthUsernameTypedDict(
    PrometheusSpecApiserverConfigBasicAuthUsernameOptionalTypedDict, total=
    (True)):
    key: str


class PrometheusSpecApiserverConfigBasicAuthTypedDict(TypedDict, total=(False)
    ):
    password: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthPassword,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthPasswordTypedDict
        ]
    username: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthUsername,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthUsernameTypedDict
        ]


class PrometheusSpecApiserverConfigTlsConfigCaConfigMapOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigTlsConfigCaConfigMapTypedDict(
    PrometheusSpecApiserverConfigTlsConfigCaConfigMapOptionalTypedDict,
    total=(True)):
    key: str


class PrometheusSpecApiserverConfigTlsConfigCaSecretOptionalTypedDict(TypedDict
    , total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigTlsConfigCaSecretTypedDict(
    PrometheusSpecApiserverConfigTlsConfigCaSecretOptionalTypedDict, total=
    (True)):
    key: str


class PrometheusSpecApiserverConfigTlsConfigCaTypedDict(TypedDict, total=(
    False)):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaConfigMap,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaConfigMapTypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaSecret,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaSecretTypedDict
        ]


class PrometheusSpecApiserverConfigTlsConfigCertConfigMapOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigTlsConfigCertConfigMapTypedDict(
    PrometheusSpecApiserverConfigTlsConfigCertConfigMapOptionalTypedDict,
    total=(True)):
    key: str


class PrometheusSpecApiserverConfigTlsConfigCertSecretOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigTlsConfigCertSecretTypedDict(
    PrometheusSpecApiserverConfigTlsConfigCertSecretOptionalTypedDict,
    total=(True)):
    key: str


class PrometheusSpecApiserverConfigTlsConfigCertTypedDict(TypedDict, total=
    (False)):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertConfigMap,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertConfigMapTypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertSecret,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertSecretTypedDict
        ]


class PrometheusSpecApiserverConfigTlsConfigKeySecretOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecApiserverConfigTlsConfigKeySecretTypedDict(
    PrometheusSpecApiserverConfigTlsConfigKeySecretOptionalTypedDict, total
    =(True)):
    key: str


class PrometheusSpecApiserverConfigTlsConfigTypedDict(TypedDict, total=(False)
    ):
    ca: Union[kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCa,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCaTypedDict]
    caFile: str
    cert: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCert,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigCertTypedDict]
    certFile: str
    insecureSkipVerify: bool
    keyFile: str
    keySecret: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigKeySecret,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigKeySecretTypedDict
        ]
    serverName: str


class PrometheusSpecApiserverConfigOptionalTypedDict(TypedDict, total=(False)):
    basicAuth: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuth,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigBasicAuthTypedDict]
    bearerToken: str
    bearerTokenFile: str
    tlsConfig: Union[
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfig,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTlsConfigTypedDict]


class PrometheusSpecApiserverConfigTypedDict(
    PrometheusSpecApiserverConfigOptionalTypedDict, total=(True)):
    host: str


class PrometheusSpecArbitraryFSAccessThroughSMsTypedDict(TypedDict, total=(
    False)):
    deny: bool


class PrometheusSpecArrayArrayValueFromConfigMapKeyRefOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayArrayValueFromConfigMapKeyRefTypedDict(
    PrometheusSpecArrayArrayValueFromConfigMapKeyRefOptionalTypedDict,
    total=(True)):
    key: str


class PrometheusSpecArrayArrayValueFromFieldRefOptionalTypedDict(TypedDict,
    total=(False)):
    apiVersion: str


class PrometheusSpecArrayArrayValueFromFieldRefTypedDict(
    PrometheusSpecArrayArrayValueFromFieldRefOptionalTypedDict, total=(True)):
    fieldPath: str


class PrometheusSpecArrayArrayValueFromResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class PrometheusSpecArrayArrayValueFromResourceFieldRefTypedDict(
    PrometheusSpecArrayArrayValueFromResourceFieldRefOptionalTypedDict,
    total=(True)):
    resource: str


class PrometheusSpecArrayArrayValueFromSecretKeyRefOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayArrayValueFromSecretKeyRefTypedDict(
    PrometheusSpecArrayArrayValueFromSecretKeyRefOptionalTypedDict, total=(
    True)):
    key: str


class PrometheusSpecArrayArrayValueFromTypedDict(TypedDict, total=(False)):
    configMapKeyRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromConfigMapKeyRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromConfigMapKeyRefTypedDict
        ]
    fieldRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromFieldRefTypedDict]
    resourceFieldRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromResourceFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromResourceFieldRefTypedDict
        ]
    secretKeyRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromSecretKeyRef,
        kdsl.monitoring.v1.PrometheusSpecArrayArrayValueFromSecretKeyRefTypedDict
        ]


class PrometheusSpecArrayArrayTypedDict(TypedDict, total=(False)):
    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    sourceLabels: Sequence[str]
    targetLabel: str


class PrometheusSpecArrayArrayConfigMapRefTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayArraySecretRefTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayLifecyclePostStartExecTypedDict(TypedDict, total=(
    False)):
    command: Sequence[str]


class PrometheusSpecArrayLifecyclePostStartHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class PrometheusSpecArrayLifecyclePostStartHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class PrometheusSpecArrayLifecyclePostStartHttpGetTypedDict(
    PrometheusSpecArrayLifecyclePostStartHttpGetOptionalTypedDict, total=(True)
    ):
    port: Any


class PrometheusSpecArrayLifecyclePostStartTcpSocketOptionalTypedDict(TypedDict
    , total=(False)):
    host: str


class PrometheusSpecArrayLifecyclePostStartTcpSocketTypedDict(
    PrometheusSpecArrayLifecyclePostStartTcpSocketOptionalTypedDict, total=
    (True)):
    port: Any


class PrometheusSpecArrayLifecyclePostStartTypedDict(TypedDict, total=(False)):
    exec: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartExec,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartExecTypedDict]
    httpGet: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartHttpGetTypedDict
        ]
    tcpSocket: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartTcpSocketTypedDict
        ]


class PrometheusSpecArrayLifecyclePreStopExecTypedDict(TypedDict, total=(False)
    ):
    command: Sequence[str]


class PrometheusSpecArrayLifecyclePreStopHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class PrometheusSpecArrayLifecyclePreStopHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class PrometheusSpecArrayLifecyclePreStopHttpGetTypedDict(
    PrometheusSpecArrayLifecyclePreStopHttpGetOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayLifecyclePreStopTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class PrometheusSpecArrayLifecyclePreStopTcpSocketTypedDict(
    PrometheusSpecArrayLifecyclePreStopTcpSocketOptionalTypedDict, total=(True)
    ):
    port: Any


class PrometheusSpecArrayLifecyclePreStopTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopExec,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopExecTypedDict]
    httpGet: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopHttpGetTypedDict]
    tcpSocket: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopTcpSocketTypedDict
        ]


class PrometheusSpecArrayLifecycleTypedDict(TypedDict, total=(False)):
    postStart: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStart,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePostStartTypedDict]
    preStop: Union[kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStop,
        kdsl.monitoring.v1.PrometheusSpecArrayLifecyclePreStopTypedDict]


class PrometheusSpecArrayLivenessProbeExecTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class PrometheusSpecArrayLivenessProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class PrometheusSpecArrayLivenessProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class PrometheusSpecArrayLivenessProbeHttpGetTypedDict(
    PrometheusSpecArrayLivenessProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayLivenessProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class PrometheusSpecArrayLivenessProbeTcpSocketTypedDict(
    PrometheusSpecArrayLivenessProbeTcpSocketOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayLivenessProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeExec,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayLivenessProbeTcpSocketTypedDict]
    timeoutSeconds: int


class PrometheusSpecArrayReadinessProbeExecTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class PrometheusSpecArrayReadinessProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class PrometheusSpecArrayReadinessProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class PrometheusSpecArrayReadinessProbeHttpGetTypedDict(
    PrometheusSpecArrayReadinessProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayReadinessProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class PrometheusSpecArrayReadinessProbeTcpSocketTypedDict(
    PrometheusSpecArrayReadinessProbeTcpSocketOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayReadinessProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeExec,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayReadinessProbeTcpSocketTypedDict]
    timeoutSeconds: int


class PrometheusSpecArrayResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class PrometheusSpecArraySecurityContextCapabilitiesTypedDict(TypedDict,
    total=(False)):
    add: Sequence[str]
    drop: Sequence[str]


class PrometheusSpecArraySecurityContextSeLinuxOptionsTypedDict(TypedDict,
    total=(False)):
    level: str
    role: str
    type: str
    user: str


class PrometheusSpecArraySecurityContextWindowsOptionsTypedDict(TypedDict,
    total=(False)):
    gmsaCredentialSpec: str
    gmsaCredentialSpecName: str
    runAsUserName: str


class PrometheusSpecArraySecurityContextTypedDict(TypedDict, total=(False)):
    allowPrivilegeEscalation: bool
    capabilities: Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextCapabilities,
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextCapabilitiesTypedDict
        ]
    privileged: bool
    procMount: str
    readOnlyRootFilesystem: bool
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextSeLinuxOptionsTypedDict
        ]
    windowsOptions: Union[
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextWindowsOptions,
        kdsl.monitoring.v1.PrometheusSpecArraySecurityContextWindowsOptionsTypedDict
        ]


class PrometheusSpecArrayStartupProbeExecTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class PrometheusSpecArrayStartupProbeHttpGetArrayTypedDict(TypedDict, total
    =(True)):
    name: str
    value: str


class PrometheusSpecArrayStartupProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGetArray,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class PrometheusSpecArrayStartupProbeHttpGetTypedDict(
    PrometheusSpecArrayStartupProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayStartupProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class PrometheusSpecArrayStartupProbeTcpSocketTypedDict(
    PrometheusSpecArrayStartupProbeTcpSocketOptionalTypedDict, total=(True)):
    port: Any


class PrometheusSpecArrayStartupProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeExec,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGet,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeTcpSocket,
        kdsl.monitoring.v1.PrometheusSpecArrayStartupProbeTcpSocketTypedDict]
    timeoutSeconds: int


class PrometheusSpecArrayOptionalTypedDict(TypedDict, total=(False)):
    awsElasticBlockStore: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayAwsElasticBlockStore,
        kdsl.monitoring.v1.PrometheusSpecArrayAwsElasticBlockStoreTypedDict]
    azureDisk: Union[kdsl.monitoring.v1.PrometheusSpecArrayAzureDisk,
        kdsl.monitoring.v1.PrometheusSpecArrayAzureDiskTypedDict]
    azureFile: Union[kdsl.monitoring.v1.PrometheusSpecArrayAzureFile,
        kdsl.monitoring.v1.PrometheusSpecArrayAzureFileTypedDict]
    cephfs: Union[kdsl.monitoring.v1.PrometheusSpecArrayCephfs,
        kdsl.monitoring.v1.PrometheusSpecArrayCephfsTypedDict]
    cinder: Union[kdsl.monitoring.v1.PrometheusSpecArrayCinder,
        kdsl.monitoring.v1.PrometheusSpecArrayCinderTypedDict]
    configMap: Union[kdsl.monitoring.v1.PrometheusSpecArrayConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMapTypedDict]
    csi: Union[kdsl.monitoring.v1.PrometheusSpecArrayCsi,
        kdsl.monitoring.v1.PrometheusSpecArrayCsiTypedDict]
    downwardAPI: Union[kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPI,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPITypedDict]
    emptyDir: Union[kdsl.monitoring.v1.PrometheusSpecArrayEmptyDir,
        kdsl.monitoring.v1.PrometheusSpecArrayEmptyDirTypedDict]
    fc: Union[kdsl.monitoring.v1.PrometheusSpecArrayFc,
        kdsl.monitoring.v1.PrometheusSpecArrayFcTypedDict]
    flexVolume: Union[kdsl.monitoring.v1.PrometheusSpecArrayFlexVolume,
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolumeTypedDict]
    flocker: Union[kdsl.monitoring.v1.PrometheusSpecArrayFlocker,
        kdsl.monitoring.v1.PrometheusSpecArrayFlockerTypedDict]
    gcePersistentDisk: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayGcePersistentDisk,
        kdsl.monitoring.v1.PrometheusSpecArrayGcePersistentDiskTypedDict]
    gitRepo: Union[kdsl.monitoring.v1.PrometheusSpecArrayGitRepo,
        kdsl.monitoring.v1.PrometheusSpecArrayGitRepoTypedDict]
    glusterfs: Union[kdsl.monitoring.v1.PrometheusSpecArrayGlusterfs,
        kdsl.monitoring.v1.PrometheusSpecArrayGlusterfsTypedDict]
    hostPath: Union[kdsl.monitoring.v1.PrometheusSpecArrayHostPath,
        kdsl.monitoring.v1.PrometheusSpecArrayHostPathTypedDict]
    iscsi: Union[kdsl.monitoring.v1.PrometheusSpecArrayIscsi,
        kdsl.monitoring.v1.PrometheusSpecArrayIscsiTypedDict]
    nfs: Union[kdsl.monitoring.v1.PrometheusSpecArrayNfs,
        kdsl.monitoring.v1.PrometheusSpecArrayNfsTypedDict]
    persistentVolumeClaim: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayPersistentVolumeClaim,
        kdsl.monitoring.v1.PrometheusSpecArrayPersistentVolumeClaimTypedDict]
    photonPersistentDisk: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayPhotonPersistentDisk,
        kdsl.monitoring.v1.PrometheusSpecArrayPhotonPersistentDiskTypedDict]
    portworxVolume: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayPortworxVolume,
        kdsl.monitoring.v1.PrometheusSpecArrayPortworxVolumeTypedDict]
    projected: Union[kdsl.monitoring.v1.PrometheusSpecArrayProjected,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedTypedDict]
    quobyte: Union[kdsl.monitoring.v1.PrometheusSpecArrayQuobyte,
        kdsl.monitoring.v1.PrometheusSpecArrayQuobyteTypedDict]
    rbd: Union[kdsl.monitoring.v1.PrometheusSpecArrayRbd,
        kdsl.monitoring.v1.PrometheusSpecArrayRbdTypedDict]
    scaleIO: Union[kdsl.monitoring.v1.PrometheusSpecArrayScaleIO,
        kdsl.monitoring.v1.PrometheusSpecArrayScaleIOTypedDict]
    secret: Union[kdsl.monitoring.v1.PrometheusSpecArraySecret,
        kdsl.monitoring.v1.PrometheusSpecArraySecretTypedDict]
    storageos: Union[kdsl.monitoring.v1.PrometheusSpecArrayStorageos,
        kdsl.monitoring.v1.PrometheusSpecArrayStorageosTypedDict]
    vsphereVolume: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayVsphereVolume,
        kdsl.monitoring.v1.PrometheusSpecArrayVsphereVolumeTypedDict]


class PrometheusSpecArrayTypedDict(PrometheusSpecArrayOptionalTypedDict,
    total=(True)):
    name: str


class PrometheusSpecPodMonitorNamespaceSelectorArrayOptionalTypedDict(TypedDict
    , total=(False)):
    values: Sequence[str]


class PrometheusSpecPodMonitorNamespaceSelectorArrayTypedDict(
    PrometheusSpecPodMonitorNamespaceSelectorArrayOptionalTypedDict, total=
    (True)):
    key: str
    operator: str


class PrometheusSpecPodMonitorNamespaceSelectorTypedDict(TypedDict, total=(
    False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecPodMonitorSelectorArrayOptionalTypedDict(TypedDict,
    total=(False)):
    values: Sequence[str]


class PrometheusSpecPodMonitorSelectorArrayTypedDict(
    PrometheusSpecPodMonitorSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class PrometheusSpecPodMonitorSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class PrometheusSpecQueryTypedDict(TypedDict, total=(False)):
    lookbackDelta: str
    maxConcurrency: int
    maxSamples: int
    timeout: str


class PrometheusSpecArrayBasicAuthPasswordOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayBasicAuthPasswordTypedDict(
    PrometheusSpecArrayBasicAuthPasswordOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayBasicAuthUsernameOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayBasicAuthUsernameTypedDict(
    PrometheusSpecArrayBasicAuthUsernameOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayBasicAuthTypedDict(TypedDict, total=(False)):
    password: Union[kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthPassword,
        kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthPasswordTypedDict]
    username: Union[kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthUsername,
        kdsl.monitoring.v1.PrometheusSpecArrayBasicAuthUsernameTypedDict]


class PrometheusSpecArrayTlsConfigCaConfigMapOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayTlsConfigCaConfigMapTypedDict(
    PrometheusSpecArrayTlsConfigCaConfigMapOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayTlsConfigCaSecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayTlsConfigCaSecretTypedDict(
    PrometheusSpecArrayTlsConfigCaSecretOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayTlsConfigCaTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaConfigMapTypedDict]
    secret: Union[kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaSecret,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaSecretTypedDict]


class PrometheusSpecArrayTlsConfigCertConfigMapOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayTlsConfigCertConfigMapTypedDict(
    PrometheusSpecArrayTlsConfigCertConfigMapOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayTlsConfigCertSecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayTlsConfigCertSecretTypedDict(
    PrometheusSpecArrayTlsConfigCertSecretOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayTlsConfigCertTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertConfigMapTypedDict]
    secret: Union[kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertSecret,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertSecretTypedDict]


class PrometheusSpecArrayTlsConfigKeySecretOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecArrayTlsConfigKeySecretTypedDict(
    PrometheusSpecArrayTlsConfigKeySecretOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecArrayTlsConfigTypedDict(TypedDict, total=(False)):
    ca: Union[kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCa,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCaTypedDict]
    caFile: str
    cert: Union[kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCert,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigCertTypedDict]
    certFile: str
    insecureSkipVerify: bool
    keyFile: str
    keySecret: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigKeySecret,
        kdsl.monitoring.v1.PrometheusSpecArrayTlsConfigKeySecretTypedDict]
    serverName: str


class PrometheusSpecArrayQueueConfigTypedDict(TypedDict, total=(False)):
    batchSendDeadline: str
    capacity: int
    maxBackoff: str
    maxRetries: int
    maxSamplesPerSend: int
    maxShards: int
    minBackoff: str
    minShards: int


class PrometheusSpecResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class PrometheusSpecRuleNamespaceSelectorArrayOptionalTypedDict(TypedDict,
    total=(False)):
    values: Sequence[str]


class PrometheusSpecRuleNamespaceSelectorArrayTypedDict(
    PrometheusSpecRuleNamespaceSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class PrometheusSpecRuleNamespaceSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class PrometheusSpecRuleSelectorArrayOptionalTypedDict(TypedDict, total=(False)
    ):
    values: Sequence[str]


class PrometheusSpecRuleSelectorArrayTypedDict(
    PrometheusSpecRuleSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class PrometheusSpecRuleSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecRuleSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecRuleSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class PrometheusSpecRulesAlertTypedDict(TypedDict, total=(False)):
    forGracePeriod: str
    forOutageTolerance: str
    resendDelay: str


class PrometheusSpecRulesTypedDict(TypedDict, total=(False)):
    alert: Union[kdsl.monitoring.v1.PrometheusSpecRulesAlert,
        kdsl.monitoring.v1.PrometheusSpecRulesAlertTypedDict]


class PrometheusSpecSecurityContextSeLinuxOptionsTypedDict(TypedDict, total
    =(False)):
    level: str
    role: str
    type: str
    user: str


class PrometheusSpecSecurityContextArrayTypedDict(TypedDict, total=(True)):
    name: str
    value: str


class PrometheusSpecSecurityContextWindowsOptionsTypedDict(TypedDict, total
    =(False)):
    gmsaCredentialSpec: str
    gmsaCredentialSpecName: str
    runAsUserName: str


class PrometheusSpecSecurityContextTypedDict(TypedDict, total=(False)):
    fsGroup: int
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextSeLinuxOptionsTypedDict
        ]
    supplementalGroups: Sequence[int]
    sysctls: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContextArray,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextArrayTypedDict]]
    windowsOptions: Union[
        kdsl.monitoring.v1.PrometheusSpecSecurityContextWindowsOptions,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextWindowsOptionsTypedDict
        ]


class PrometheusSpecServiceMonitorNamespaceSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecServiceMonitorNamespaceSelectorArrayTypedDict(
    PrometheusSpecServiceMonitorNamespaceSelectorArrayOptionalTypedDict,
    total=(True)):
    key: str
    operator: str


class PrometheusSpecServiceMonitorNamespaceSelectorTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecServiceMonitorSelectorArrayOptionalTypedDict(TypedDict,
    total=(False)):
    values: Sequence[str]


class PrometheusSpecServiceMonitorSelectorArrayTypedDict(
    PrometheusSpecServiceMonitorSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class PrometheusSpecServiceMonitorSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelectorArray,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class PrometheusSpecStorageEmptyDirTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class PrometheusSpecStorageVolumeClaimTemplateSpecDataSourceOptionalTypedDict(
    TypedDict, total=(False)):
    apiGroup: str


class PrometheusSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict(
    PrometheusSpecStorageVolumeClaimTemplateSpecDataSourceOptionalTypedDict,
    total=(True)):
    kind: str
    name: str


class PrometheusSpecStorageVolumeClaimTemplateSpecResourcesTypedDict(TypedDict,
    total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict(
    PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArrayOptionalTypedDict,
    total=(True)):
    key: str
    operator: str


class PrometheusSpecStorageVolumeClaimTemplateSpecSelectorTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArray
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class PrometheusSpecStorageVolumeClaimTemplateSpecTypedDict(TypedDict,
    total=(False)):
    accessModes: Sequence[str]
    dataSource: Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecDataSource
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict
        ]
    resources: Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecResources
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecResourcesTypedDict
        ]
    selector: Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelector
        ,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecSelectorTypedDict
        ]
    storageClassName: str
    volumeMode: str
    volumeName: str


class PrometheusSpecStorageVolumeClaimTemplateStatusArrayOptionalTypedDict(
    TypedDict, total=(False)):
    lastProbeTime: str
    lastTransitionTime: str
    message: str
    reason: str


class PrometheusSpecStorageVolumeClaimTemplateStatusArrayTypedDict(
    PrometheusSpecStorageVolumeClaimTemplateStatusArrayOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class PrometheusSpecStorageVolumeClaimTemplateStatusTypedDict(TypedDict,
    total=(False)):
    accessModes: Sequence[str]
    capacity: Mapping[str, str]
    conditions: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatusArray,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatusArrayTypedDict
        ]]
    phase: str


class PrometheusSpecStorageVolumeClaimTemplateTypedDict(TypedDict, total=(
    False)):
    apiVersion: str
    kind: str
    metadata: Mapping[str, Any]
    spec: Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpec,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateSpecTypedDict
        ]
    status: Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatus,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateStatusTypedDict
        ]


class PrometheusSpecStorageTypedDict(TypedDict, total=(False)):
    emptyDir: Union[kdsl.monitoring.v1.PrometheusSpecStorageEmptyDir,
        kdsl.monitoring.v1.PrometheusSpecStorageEmptyDirTypedDict]
    volumeClaimTemplate: Union[
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplate,
        kdsl.monitoring.v1.PrometheusSpecStorageVolumeClaimTemplateTypedDict]


class PrometheusSpecThanosObjectStorageConfigOptionalTypedDict(TypedDict,
    total=(False)):
    name: str
    optional: bool


class PrometheusSpecThanosObjectStorageConfigTypedDict(
    PrometheusSpecThanosObjectStorageConfigOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecThanosResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class PrometheusSpecThanosTracingConfigOptionalTypedDict(TypedDict, total=(
    False)):
    name: str
    optional: bool


class PrometheusSpecThanosTracingConfigTypedDict(
    PrometheusSpecThanosTracingConfigOptionalTypedDict, total=(True)):
    key: str


class PrometheusSpecThanosTypedDict(TypedDict, total=(False)):
    baseImage: str
    image: str
    listenLocal: bool
    objectStorageConfig: Union[
        kdsl.monitoring.v1.PrometheusSpecThanosObjectStorageConfig,
        kdsl.monitoring.v1.PrometheusSpecThanosObjectStorageConfigTypedDict]
    resources: Union[kdsl.monitoring.v1.PrometheusSpecThanosResources,
        kdsl.monitoring.v1.PrometheusSpecThanosResourcesTypedDict]
    sha: str
    tag: str
    tracingConfig: Union[
        kdsl.monitoring.v1.PrometheusSpecThanosTracingConfig,
        kdsl.monitoring.v1.PrometheusSpecThanosTracingConfigTypedDict]
    version: str


class PrometheusSpecArrayAwsElasticBlockStoreOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class PrometheusSpecArrayAwsElasticBlockStoreTypedDict(
    PrometheusSpecArrayAwsElasticBlockStoreOptionalTypedDict, total=(True)):
    volumeID: str


class PrometheusSpecArrayAzureDiskOptionalTypedDict(TypedDict, total=(False)):
    cachingMode: str
    fsType: str
    kind: str
    readOnly: bool


class PrometheusSpecArrayAzureDiskTypedDict(
    PrometheusSpecArrayAzureDiskOptionalTypedDict, total=(True)):
    diskName: str
    diskURI: str


class PrometheusSpecArrayAzureFileOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class PrometheusSpecArrayAzureFileTypedDict(
    PrometheusSpecArrayAzureFileOptionalTypedDict, total=(True)):
    secretName: str
    shareName: str


class PrometheusSpecArrayCephfsSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class PrometheusSpecArrayCephfsOptionalTypedDict(TypedDict, total=(False)):
    path: str
    readOnly: bool
    secretFile: str
    secretRef: Union[kdsl.monitoring.v1.PrometheusSpecArrayCephfsSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayCephfsSecretRefTypedDict]
    user: str


class PrometheusSpecArrayCephfsTypedDict(
    PrometheusSpecArrayCephfsOptionalTypedDict, total=(True)):
    monitors: Sequence[str]


class PrometheusSpecArrayCinderSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class PrometheusSpecArrayCinderOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.PrometheusSpecArrayCinderSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayCinderSecretRefTypedDict]


class PrometheusSpecArrayCinderTypedDict(
    PrometheusSpecArrayCinderOptionalTypedDict, total=(True)):
    volumeID: str


class PrometheusSpecArrayConfigMapArrayOptionalTypedDict(TypedDict, total=(
    False)):
    mode: int


class PrometheusSpecArrayConfigMapArrayTypedDict(
    PrometheusSpecArrayConfigMapArrayOptionalTypedDict, total=(True)):
    key: str
    path: str


class PrometheusSpecArrayConfigMapTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMapArray,
        kdsl.monitoring.v1.PrometheusSpecArrayConfigMapArrayTypedDict]]
    name: str
    optional: bool


class PrometheusSpecArrayCsiNodePublishSecretRefTypedDict(TypedDict, total=
    (False)):
    name: str


class PrometheusSpecArrayCsiOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    nodePublishSecretRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayCsiNodePublishSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayCsiNodePublishSecretRefTypedDict]
    readOnly: bool
    volumeAttributes: Mapping[str, str]


class PrometheusSpecArrayCsiTypedDict(PrometheusSpecArrayCsiOptionalTypedDict,
    total=(True)):
    driver: str


class PrometheusSpecArrayDownwardAPIArrayFieldRefOptionalTypedDict(TypedDict,
    total=(False)):
    apiVersion: str


class PrometheusSpecArrayDownwardAPIArrayFieldRefTypedDict(
    PrometheusSpecArrayDownwardAPIArrayFieldRefOptionalTypedDict, total=(True)
    ):
    fieldPath: str


class PrometheusSpecArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class PrometheusSpecArrayDownwardAPIArrayResourceFieldRefTypedDict(
    PrometheusSpecArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict,
    total=(True)):
    resource: str


class PrometheusSpecArrayDownwardAPIArrayOptionalTypedDict(TypedDict, total
    =(False)):
    fieldRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayFieldRefTypedDict
        ]
    mode: int
    resourceFieldRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayResourceFieldRef,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]


class PrometheusSpecArrayDownwardAPIArrayTypedDict(
    PrometheusSpecArrayDownwardAPIArrayOptionalTypedDict, total=(True)):
    path: str


class PrometheusSpecArrayDownwardAPITypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArray,
        kdsl.monitoring.v1.PrometheusSpecArrayDownwardAPIArrayTypedDict]]


class PrometheusSpecArrayEmptyDirTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class PrometheusSpecArrayFcTypedDict(TypedDict, total=(False)):
    fsType: str
    lun: int
    readOnly: bool
    targetWWNs: Sequence[str]
    wwids: Sequence[str]


class PrometheusSpecArrayFlexVolumeSecretRefTypedDict(TypedDict, total=(False)
    ):
    name: str


class PrometheusSpecArrayFlexVolumeOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    options: Mapping[str, str]
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolumeSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayFlexVolumeSecretRefTypedDict]


class PrometheusSpecArrayFlexVolumeTypedDict(
    PrometheusSpecArrayFlexVolumeOptionalTypedDict, total=(True)):
    driver: str


class PrometheusSpecArrayFlockerTypedDict(TypedDict, total=(False)):
    datasetName: str
    datasetUUID: str


class PrometheusSpecArrayGcePersistentDiskOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class PrometheusSpecArrayGcePersistentDiskTypedDict(
    PrometheusSpecArrayGcePersistentDiskOptionalTypedDict, total=(True)):
    pdName: str


class PrometheusSpecArrayGitRepoOptionalTypedDict(TypedDict, total=(False)):
    directory: str
    revision: str


class PrometheusSpecArrayGitRepoTypedDict(
    PrometheusSpecArrayGitRepoOptionalTypedDict, total=(True)):
    repository: str


class PrometheusSpecArrayGlusterfsOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class PrometheusSpecArrayGlusterfsTypedDict(
    PrometheusSpecArrayGlusterfsOptionalTypedDict, total=(True)):
    endpoints: str
    path: str


class PrometheusSpecArrayHostPathOptionalTypedDict(TypedDict, total=(False)):
    type: str


class PrometheusSpecArrayHostPathTypedDict(
    PrometheusSpecArrayHostPathOptionalTypedDict, total=(True)):
    path: str


class PrometheusSpecArrayIscsiSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class PrometheusSpecArrayIscsiOptionalTypedDict(TypedDict, total=(False)):
    chapAuthDiscovery: bool
    chapAuthSession: bool
    fsType: str
    initiatorName: str
    iscsiInterface: str
    portals: Sequence[str]
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.PrometheusSpecArrayIscsiSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayIscsiSecretRefTypedDict]


class PrometheusSpecArrayIscsiTypedDict(
    PrometheusSpecArrayIscsiOptionalTypedDict, total=(True)):
    iqn: str
    lun: int
    targetPortal: str


class PrometheusSpecArrayNfsOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class PrometheusSpecArrayNfsTypedDict(PrometheusSpecArrayNfsOptionalTypedDict,
    total=(True)):
    path: str
    server: str


class PrometheusSpecArrayPersistentVolumeClaimOptionalTypedDict(TypedDict,
    total=(False)):
    readOnly: bool


class PrometheusSpecArrayPersistentVolumeClaimTypedDict(
    PrometheusSpecArrayPersistentVolumeClaimOptionalTypedDict, total=(True)):
    claimName: str


class PrometheusSpecArrayPhotonPersistentDiskOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str


class PrometheusSpecArrayPhotonPersistentDiskTypedDict(
    PrometheusSpecArrayPhotonPersistentDiskOptionalTypedDict, total=(True)):
    pdID: str


class PrometheusSpecArrayPortworxVolumeOptionalTypedDict(TypedDict, total=(
    False)):
    fsType: str
    readOnly: bool


class PrometheusSpecArrayPortworxVolumeTypedDict(
    PrometheusSpecArrayPortworxVolumeOptionalTypedDict, total=(True)):
    volumeID: str


class PrometheusSpecArrayProjectedArrayConfigMapArrayOptionalTypedDict(
    TypedDict, total=(False)):
    mode: int


class PrometheusSpecArrayProjectedArrayConfigMapArrayTypedDict(
    PrometheusSpecArrayProjectedArrayConfigMapArrayOptionalTypedDict, total
    =(True)):
    key: str
    path: str


class PrometheusSpecArrayProjectedArrayConfigMapTypedDict(TypedDict, total=
    (False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMapArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMapArrayTypedDict
        ]]
    name: str
    optional: bool


class PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    apiVersion: str


class PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict(
    PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRefOptionalTypedDict,
    total=(True)):
    fieldPath: str


class PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict(
    PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict
    , total=(True)):
    resource: str


class PrometheusSpecArrayProjectedArrayDownwardAPIArrayOptionalTypedDict(
    TypedDict, total=(False)):
    fieldRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRef
        ,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict
        ]
    mode: int
    resourceFieldRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]


class PrometheusSpecArrayProjectedArrayDownwardAPIArrayTypedDict(
    PrometheusSpecArrayProjectedArrayDownwardAPIArrayOptionalTypedDict,
    total=(True)):
    path: str


class PrometheusSpecArrayProjectedArrayDownwardAPITypedDict(TypedDict,
    total=(False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPIArrayTypedDict
        ]]


class PrometheusSpecArrayProjectedArraySecretArrayOptionalTypedDict(TypedDict,
    total=(False)):
    mode: int


class PrometheusSpecArrayProjectedArraySecretArrayTypedDict(
    PrometheusSpecArrayProjectedArraySecretArrayOptionalTypedDict, total=(True)
    ):
    key: str
    path: str


class PrometheusSpecArrayProjectedArraySecretTypedDict(TypedDict, total=(False)
    ):
    items: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecretArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecretArrayTypedDict
        ]]
    name: str
    optional: bool


class PrometheusSpecArrayProjectedArrayServiceAccountTokenOptionalTypedDict(
    TypedDict, total=(False)):
    audience: str
    expirationSeconds: int


class PrometheusSpecArrayProjectedArrayServiceAccountTokenTypedDict(
    PrometheusSpecArrayProjectedArrayServiceAccountTokenOptionalTypedDict,
    total=(True)):
    path: str


class PrometheusSpecArrayProjectedArrayTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMap,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayConfigMapTypedDict]
    downwardAPI: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPI,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayDownwardAPITypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecret,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArraySecretTypedDict]
    serviceAccountToken: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayServiceAccountToken
        ,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayServiceAccountTokenTypedDict
        ]


class PrometheusSpecArrayProjectedOptionalTypedDict(TypedDict, total=(False)):
    defaultMode: int


class PrometheusSpecArrayProjectedTypedDict(
    PrometheusSpecArrayProjectedOptionalTypedDict, total=(True)):
    sources: Sequence[Union[
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArray,
        kdsl.monitoring.v1.PrometheusSpecArrayProjectedArrayTypedDict]]


class PrometheusSpecArrayQuobyteOptionalTypedDict(TypedDict, total=(False)):
    group: str
    readOnly: bool
    tenant: str
    user: str


class PrometheusSpecArrayQuobyteTypedDict(
    PrometheusSpecArrayQuobyteOptionalTypedDict, total=(True)):
    registry: str
    volume: str


class PrometheusSpecArrayRbdSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class PrometheusSpecArrayRbdOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    keyring: str
    pool: str
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.PrometheusSpecArrayRbdSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayRbdSecretRefTypedDict]
    user: str


class PrometheusSpecArrayRbdTypedDict(PrometheusSpecArrayRbdOptionalTypedDict,
    total=(True)):
    image: str
    monitors: Sequence[str]


class PrometheusSpecArrayScaleIOSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class PrometheusSpecArrayScaleIOOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    protectionDomain: str
    readOnly: bool
    sslEnabled: bool
    storageMode: str
    storagePool: str
    volumeName: str


class PrometheusSpecArrayScaleIOTypedDict(
    PrometheusSpecArrayScaleIOOptionalTypedDict, total=(True)):
    gateway: str
    secretRef: Union[kdsl.monitoring.v1.PrometheusSpecArrayScaleIOSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayScaleIOSecretRefTypedDict]
    system: str


class PrometheusSpecArraySecretArrayOptionalTypedDict(TypedDict, total=(False)
    ):
    mode: int


class PrometheusSpecArraySecretArrayTypedDict(
    PrometheusSpecArraySecretArrayOptionalTypedDict, total=(True)):
    key: str
    path: str


class PrometheusSpecArraySecretTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArraySecretArray,
        kdsl.monitoring.v1.PrometheusSpecArraySecretArrayTypedDict]]
    optional: bool
    secretName: str


class PrometheusSpecArrayStorageosSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class PrometheusSpecArrayStorageosTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.PrometheusSpecArrayStorageosSecretRef,
        kdsl.monitoring.v1.PrometheusSpecArrayStorageosSecretRefTypedDict]
    volumeName: str
    volumeNamespace: str


class PrometheusSpecArrayVsphereVolumeOptionalTypedDict(TypedDict, total=(
    False)):
    fsType: str
    storagePolicyID: str
    storagePolicyName: str


class PrometheusSpecArrayVsphereVolumeTypedDict(
    PrometheusSpecArrayVsphereVolumeOptionalTypedDict, total=(True)):
    volumePath: str


class PrometheusSpecTypedDict(TypedDict, total=(False)):
    additionalAlertManagerConfigs: Union[
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertManagerConfigs,
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertManagerConfigsTypedDict
        ]
    additionalAlertRelabelConfigs: Union[
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertRelabelConfigs,
        kdsl.monitoring.v1.PrometheusSpecAdditionalAlertRelabelConfigsTypedDict
        ]
    additionalScrapeConfigs: Union[
        kdsl.monitoring.v1.PrometheusSpecAdditionalScrapeConfigs,
        kdsl.monitoring.v1.PrometheusSpecAdditionalScrapeConfigsTypedDict]
    affinity: Union[kdsl.monitoring.v1.PrometheusSpecAffinity,
        kdsl.monitoring.v1.PrometheusSpecAffinityTypedDict]
    alerting: Union[kdsl.monitoring.v1.PrometheusSpecAlerting,
        kdsl.monitoring.v1.PrometheusSpecAlertingTypedDict]
    apiserverConfig: Union[kdsl.monitoring.v1.PrometheusSpecApiserverConfig,
        kdsl.monitoring.v1.PrometheusSpecApiserverConfigTypedDict]
    arbitraryFSAccessThroughSMs: Union[
        kdsl.monitoring.v1.PrometheusSpecArbitraryFSAccessThroughSMs,
        kdsl.monitoring.v1.PrometheusSpecArbitraryFSAccessThroughSMsTypedDict]
    baseImage: str
    configMaps: Sequence[str]
    containers: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    disableCompaction: bool
    enableAdminAPI: bool
    enforcedNamespaceLabel: str
    evaluationInterval: str
    externalLabels: Mapping[str, str]
    externalUrl: str
    ignoreNamespaceSelectors: bool
    image: str
    imagePullSecrets: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    initContainers: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    listenLocal: bool
    logFormat: str
    logLevel: str
    nodeSelector: Mapping[str, str]
    overrideHonorLabels: bool
    overrideHonorTimestamps: bool
    paused: bool
    podMetadata: Mapping[str, Any]
    podMonitorNamespaceSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelector,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorNamespaceSelectorTypedDict]
    podMonitorSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelector,
        kdsl.monitoring.v1.PrometheusSpecPodMonitorSelectorTypedDict]
    portName: str
    priorityClassName: str
    prometheusExternalLabelName: str
    query: Union[kdsl.monitoring.v1.PrometheusSpecQuery,
        kdsl.monitoring.v1.PrometheusSpecQueryTypedDict]
    remoteRead: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    remoteWrite: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    replicaExternalLabelName: str
    replicas: int
    resources: Union[kdsl.monitoring.v1.PrometheusSpecResources,
        kdsl.monitoring.v1.PrometheusSpecResourcesTypedDict]
    retention: str
    retentionSize: str
    routePrefix: str
    ruleNamespaceSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelector,
        kdsl.monitoring.v1.PrometheusSpecRuleNamespaceSelectorTypedDict]
    ruleSelector: Union[kdsl.monitoring.v1.PrometheusSpecRuleSelector,
        kdsl.monitoring.v1.PrometheusSpecRuleSelectorTypedDict]
    rules: Union[kdsl.monitoring.v1.PrometheusSpecRules,
        kdsl.monitoring.v1.PrometheusSpecRulesTypedDict]
    scrapeInterval: str
    secrets: Sequence[str]
    securityContext: Union[kdsl.monitoring.v1.PrometheusSpecSecurityContext,
        kdsl.monitoring.v1.PrometheusSpecSecurityContextTypedDict]
    serviceAccountName: str
    serviceMonitorNamespaceSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelector,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorNamespaceSelectorTypedDict
        ]
    serviceMonitorSelector: Union[
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelector,
        kdsl.monitoring.v1.PrometheusSpecServiceMonitorSelectorTypedDict]
    sha: str
    storage: Union[kdsl.monitoring.v1.PrometheusSpecStorage,
        kdsl.monitoring.v1.PrometheusSpecStorageTypedDict]
    tag: str
    thanos: Union[kdsl.monitoring.v1.PrometheusSpecThanos,
        kdsl.monitoring.v1.PrometheusSpecThanosTypedDict]
    tolerations: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    version: str
    volumes: Sequence[Union[kdsl.monitoring.v1.PrometheusSpecArray,
        kdsl.monitoring.v1.PrometheusSpecArrayTypedDict]]
    walCompression: bool


class PrometheusOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class PrometheusTypedDict(PrometheusOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.monitoring.v1.PrometheusSpec,
        kdsl.monitoring.v1.PrometheusSpecTypedDict]


class PodMonitorSpecNamespaceSelectorTypedDict(TypedDict, total=(False)):
    any: bool
    matchNames: Sequence[str]


class PodMonitorSpecArrayArrayTypedDict(TypedDict, total=(False)):
    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    sourceLabels: Sequence[str]
    targetLabel: str


class PodMonitorSpecArrayTypedDict(TypedDict, total=(False)):
    honorLabels: bool
    honorTimestamps: bool
    interval: str
    metricRelabelings: Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecArrayArray,
        kdsl.monitoring.v1.PodMonitorSpecArrayArrayTypedDict]]
    params: Mapping[str, Sequence[str]]
    path: str
    port: str
    proxyUrl: str
    relabelings: Sequence[Union[kdsl.monitoring.v1.PodMonitorSpecArrayArray,
        kdsl.monitoring.v1.PodMonitorSpecArrayArrayTypedDict]]
    scheme: str
    scrapeTimeout: str
    targetPort: Any


class PodMonitorSpecSelectorArrayOptionalTypedDict(TypedDict, total=(False)):
    values: Sequence[str]


class PodMonitorSpecSelectorArrayTypedDict(
    PodMonitorSpecSelectorArrayOptionalTypedDict, total=(True)):
    key: str
    operator: str


class PodMonitorSpecSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecSelectorArray,
        kdsl.monitoring.v1.PodMonitorSpecSelectorArrayTypedDict]]
    matchLabels: Mapping[str, str]


class PodMonitorSpecOptionalTypedDict(TypedDict, total=(False)):
    jobLabel: str
    namespaceSelector: Union[
        kdsl.monitoring.v1.PodMonitorSpecNamespaceSelector,
        kdsl.monitoring.v1.PodMonitorSpecNamespaceSelectorTypedDict]
    podTargetLabels: Sequence[str]
    sampleLimit: int


class PodMonitorSpecTypedDict(PodMonitorSpecOptionalTypedDict, total=(True)):
    podMetricsEndpoints: Sequence[Union[
        kdsl.monitoring.v1.PodMonitorSpecArray,
        kdsl.monitoring.v1.PodMonitorSpecArrayTypedDict]]
    selector: Union[kdsl.monitoring.v1.PodMonitorSpecSelector,
        kdsl.monitoring.v1.PodMonitorSpecSelectorTypedDict]


class PodMonitorOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class PodMonitorTypedDict(PodMonitorOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.monitoring.v1.PodMonitorSpec,
        kdsl.monitoring.v1.PodMonitorSpecTypedDict]


class AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict(
    AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict,
    total=(True)):
    key: str
    operator: str


class AlertmanagerSpecAffinityNodeAffinityArrayPreferenceTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]


class AlertmanagerSpecAffinityNodeAffinityArrayTypedDict(TypedDict, total=(
    True)):
    preference: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreference,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ]
    weight: int


class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict(
    AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]


class AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict(
    TypedDict, total=(True)):
    nodeSelectorTerms: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]]


class AlertmanagerSpecAffinityNodeAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityArrayTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]


class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermTypedDict(
    AlertmanagerSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict,
    total=(True)):
    topologyKey: str


class AlertmanagerSpecAffinityPodAffinityArrayOptionalTypedDict(TypedDict,
    total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class AlertmanagerSpecAffinityPodAffinityArrayTypedDict(
    AlertmanagerSpecAffinityPodAffinityArrayOptionalTypedDict, total=(True)):
    topologyKey: str


class AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict(
    AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorTypedDict(TypedDict,
    total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class AlertmanagerSpecAffinityPodAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityArrayTypedDict]]


class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermTypedDict(
    AlertmanagerSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class AlertmanagerSpecAffinityPodAntiAffinityArrayOptionalTypedDict(TypedDict,
    total=(False)):
    labelSelector: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class AlertmanagerSpecAffinityPodAntiAffinityArrayTypedDict(
    AlertmanagerSpecAffinityPodAntiAffinityArrayOptionalTypedDict, total=(True)
    ):
    topologyKey: str


class AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict(
    AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class AlertmanagerSpecAffinityPodAntiAffinityTypedDict(TypedDict, total=(False)
    ):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArray,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityArrayTypedDict
        ]]


class AlertmanagerSpecAffinityTypedDict(TypedDict, total=(False)):
    nodeAffinity: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityNodeAffinityTypedDict]
    podAffinity: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAffinityTypedDict]
    podAntiAffinity: Union[
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityPodAntiAffinityTypedDict]


class AlertmanagerSpecArrayArrayValueFromConfigMapKeyRefOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class AlertmanagerSpecArrayArrayValueFromConfigMapKeyRefTypedDict(
    AlertmanagerSpecArrayArrayValueFromConfigMapKeyRefOptionalTypedDict,
    total=(True)):
    key: str


class AlertmanagerSpecArrayArrayValueFromFieldRefOptionalTypedDict(TypedDict,
    total=(False)):
    apiVersion: str


class AlertmanagerSpecArrayArrayValueFromFieldRefTypedDict(
    AlertmanagerSpecArrayArrayValueFromFieldRefOptionalTypedDict, total=(True)
    ):
    fieldPath: str


class AlertmanagerSpecArrayArrayValueFromResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class AlertmanagerSpecArrayArrayValueFromResourceFieldRefTypedDict(
    AlertmanagerSpecArrayArrayValueFromResourceFieldRefOptionalTypedDict,
    total=(True)):
    resource: str


class AlertmanagerSpecArrayArrayValueFromSecretKeyRefOptionalTypedDict(
    TypedDict, total=(False)):
    name: str
    optional: bool


class AlertmanagerSpecArrayArrayValueFromSecretKeyRefTypedDict(
    AlertmanagerSpecArrayArrayValueFromSecretKeyRefOptionalTypedDict, total
    =(True)):
    key: str


class AlertmanagerSpecArrayArrayValueFromTypedDict(TypedDict, total=(False)):
    configMapKeyRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromConfigMapKeyRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromConfigMapKeyRefTypedDict
        ]
    fieldRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromFieldRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromFieldRefTypedDict
        ]
    resourceFieldRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromResourceFieldRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromResourceFieldRefTypedDict
        ]
    secretKeyRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromSecretKeyRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayArrayValueFromSecretKeyRefTypedDict
        ]


class AlertmanagerSpecArrayArrayOptionalTypedDict(TypedDict, total=(False)):
    mountPropagation: str
    readOnly: bool
    subPath: str
    subPathExpr: str


class AlertmanagerSpecArrayArrayTypedDict(
    AlertmanagerSpecArrayArrayOptionalTypedDict, total=(True)):
    mountPath: str
    name: str


class AlertmanagerSpecArrayArrayConfigMapRefTypedDict(TypedDict, total=(False)
    ):
    name: str
    optional: bool


class AlertmanagerSpecArrayArraySecretRefTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class AlertmanagerSpecArrayLifecyclePostStartExecTypedDict(TypedDict, total
    =(False)):
    command: Sequence[str]


class AlertmanagerSpecArrayLifecyclePostStartHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class AlertmanagerSpecArrayLifecyclePostStartHttpGetOptionalTypedDict(TypedDict
    , total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class AlertmanagerSpecArrayLifecyclePostStartHttpGetTypedDict(
    AlertmanagerSpecArrayLifecyclePostStartHttpGetOptionalTypedDict, total=
    (True)):
    port: Any


class AlertmanagerSpecArrayLifecyclePostStartTcpSocketOptionalTypedDict(
    TypedDict, total=(False)):
    host: str


class AlertmanagerSpecArrayLifecyclePostStartTcpSocketTypedDict(
    AlertmanagerSpecArrayLifecyclePostStartTcpSocketOptionalTypedDict,
    total=(True)):
    port: Any


class AlertmanagerSpecArrayLifecyclePostStartTypedDict(TypedDict, total=(False)
    ):
    exec: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartExecTypedDict
        ]
    httpGet: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartHttpGetTypedDict
        ]
    tcpSocket: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartTcpSocketTypedDict
        ]


class AlertmanagerSpecArrayLifecyclePreStopExecTypedDict(TypedDict, total=(
    False)):
    command: Sequence[str]


class AlertmanagerSpecArrayLifecyclePreStopHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class AlertmanagerSpecArrayLifecyclePreStopHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class AlertmanagerSpecArrayLifecyclePreStopHttpGetTypedDict(
    AlertmanagerSpecArrayLifecyclePreStopHttpGetOptionalTypedDict, total=(True)
    ):
    port: Any


class AlertmanagerSpecArrayLifecyclePreStopTcpSocketOptionalTypedDict(TypedDict
    , total=(False)):
    host: str


class AlertmanagerSpecArrayLifecyclePreStopTcpSocketTypedDict(
    AlertmanagerSpecArrayLifecyclePreStopTcpSocketOptionalTypedDict, total=
    (True)):
    port: Any


class AlertmanagerSpecArrayLifecyclePreStopTypedDict(TypedDict, total=(False)):
    exec: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopExecTypedDict]
    httpGet: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopHttpGetTypedDict
        ]
    tcpSocket: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopTcpSocketTypedDict
        ]


class AlertmanagerSpecArrayLifecycleTypedDict(TypedDict, total=(False)):
    postStart: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStart,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePostStartTypedDict]
    preStop: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStop,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLifecyclePreStopTypedDict]


class AlertmanagerSpecArrayLivenessProbeExecTypedDict(TypedDict, total=(False)
    ):
    command: Sequence[str]


class AlertmanagerSpecArrayLivenessProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class AlertmanagerSpecArrayLivenessProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class AlertmanagerSpecArrayLivenessProbeHttpGetTypedDict(
    AlertmanagerSpecArrayLivenessProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class AlertmanagerSpecArrayLivenessProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class AlertmanagerSpecArrayLivenessProbeTcpSocketTypedDict(
    AlertmanagerSpecArrayLivenessProbeTcpSocketOptionalTypedDict, total=(True)
    ):
    port: Any


class AlertmanagerSpecArrayLivenessProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayLivenessProbeTcpSocketTypedDict
        ]
    timeoutSeconds: int


class AlertmanagerSpecArrayReadinessProbeExecTypedDict(TypedDict, total=(False)
    ):
    command: Sequence[str]


class AlertmanagerSpecArrayReadinessProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class AlertmanagerSpecArrayReadinessProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class AlertmanagerSpecArrayReadinessProbeHttpGetTypedDict(
    AlertmanagerSpecArrayReadinessProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class AlertmanagerSpecArrayReadinessProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class AlertmanagerSpecArrayReadinessProbeTcpSocketTypedDict(
    AlertmanagerSpecArrayReadinessProbeTcpSocketOptionalTypedDict, total=(True)
    ):
    port: Any


class AlertmanagerSpecArrayReadinessProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayReadinessProbeTcpSocketTypedDict
        ]
    timeoutSeconds: int


class AlertmanagerSpecArrayResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class AlertmanagerSpecArraySecurityContextCapabilitiesTypedDict(TypedDict,
    total=(False)):
    add: Sequence[str]
    drop: Sequence[str]


class AlertmanagerSpecArraySecurityContextSeLinuxOptionsTypedDict(TypedDict,
    total=(False)):
    level: str
    role: str
    type: str
    user: str


class AlertmanagerSpecArraySecurityContextWindowsOptionsTypedDict(TypedDict,
    total=(False)):
    gmsaCredentialSpec: str
    gmsaCredentialSpecName: str
    runAsUserName: str


class AlertmanagerSpecArraySecurityContextTypedDict(TypedDict, total=(False)):
    allowPrivilegeEscalation: bool
    capabilities: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextCapabilities,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextCapabilitiesTypedDict
        ]
    privileged: bool
    procMount: str
    readOnlyRootFilesystem: bool
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextSeLinuxOptionsTypedDict
        ]
    windowsOptions: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextWindowsOptions,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecurityContextWindowsOptionsTypedDict
        ]


class AlertmanagerSpecArrayStartupProbeExecTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class AlertmanagerSpecArrayStartupProbeHttpGetArrayTypedDict(TypedDict,
    total=(True)):
    name: str
    value: str


class AlertmanagerSpecArrayStartupProbeHttpGetOptionalTypedDict(TypedDict,
    total=(False)):
    host: str
    httpHeaders: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGetArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGetArrayTypedDict
        ]]
    path: str
    scheme: str


class AlertmanagerSpecArrayStartupProbeHttpGetTypedDict(
    AlertmanagerSpecArrayStartupProbeHttpGetOptionalTypedDict, total=(True)):
    port: Any


class AlertmanagerSpecArrayStartupProbeTcpSocketOptionalTypedDict(TypedDict,
    total=(False)):
    host: str


class AlertmanagerSpecArrayStartupProbeTcpSocketTypedDict(
    AlertmanagerSpecArrayStartupProbeTcpSocketOptionalTypedDict, total=(True)):
    port: Any


class AlertmanagerSpecArrayStartupProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeExec,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeExecTypedDict]
    failureThreshold: int
    httpGet: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGet,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeHttpGetTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeTcpSocket,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStartupProbeTcpSocketTypedDict]
    timeoutSeconds: int


class AlertmanagerSpecArrayOptionalTypedDict(TypedDict, total=(False)):
    awsElasticBlockStore: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayAwsElasticBlockStore,
        kdsl.monitoring.v1.AlertmanagerSpecArrayAwsElasticBlockStoreTypedDict]
    azureDisk: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayAzureDisk,
        kdsl.monitoring.v1.AlertmanagerSpecArrayAzureDiskTypedDict]
    azureFile: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayAzureFile,
        kdsl.monitoring.v1.AlertmanagerSpecArrayAzureFileTypedDict]
    cephfs: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayCephfs,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCephfsTypedDict]
    cinder: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayCinder,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCinderTypedDict]
    configMap: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMap,
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMapTypedDict]
    csi: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayCsi,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCsiTypedDict]
    downwardAPI: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPI,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPITypedDict]
    emptyDir: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayEmptyDir,
        kdsl.monitoring.v1.AlertmanagerSpecArrayEmptyDirTypedDict]
    fc: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayFc,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFcTypedDict]
    flexVolume: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolume,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolumeTypedDict]
    flocker: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayFlocker,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlockerTypedDict]
    gcePersistentDisk: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayGcePersistentDisk,
        kdsl.monitoring.v1.AlertmanagerSpecArrayGcePersistentDiskTypedDict]
    gitRepo: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayGitRepo,
        kdsl.monitoring.v1.AlertmanagerSpecArrayGitRepoTypedDict]
    glusterfs: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayGlusterfs,
        kdsl.monitoring.v1.AlertmanagerSpecArrayGlusterfsTypedDict]
    hostPath: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayHostPath,
        kdsl.monitoring.v1.AlertmanagerSpecArrayHostPathTypedDict]
    iscsi: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayIscsi,
        kdsl.monitoring.v1.AlertmanagerSpecArrayIscsiTypedDict]
    nfs: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayNfs,
        kdsl.monitoring.v1.AlertmanagerSpecArrayNfsTypedDict]
    persistentVolumeClaim: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayPersistentVolumeClaim,
        kdsl.monitoring.v1.AlertmanagerSpecArrayPersistentVolumeClaimTypedDict]
    photonPersistentDisk: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayPhotonPersistentDisk,
        kdsl.monitoring.v1.AlertmanagerSpecArrayPhotonPersistentDiskTypedDict]
    portworxVolume: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayPortworxVolume,
        kdsl.monitoring.v1.AlertmanagerSpecArrayPortworxVolumeTypedDict]
    projected: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayProjected,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedTypedDict]
    quobyte: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayQuobyte,
        kdsl.monitoring.v1.AlertmanagerSpecArrayQuobyteTypedDict]
    rbd: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayRbd,
        kdsl.monitoring.v1.AlertmanagerSpecArrayRbdTypedDict]
    scaleIO: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIO,
        kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIOTypedDict]
    secret: Union[kdsl.monitoring.v1.AlertmanagerSpecArraySecret,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecretTypedDict]
    storageos: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayStorageos,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageosTypedDict]
    vsphereVolume: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayVsphereVolume,
        kdsl.monitoring.v1.AlertmanagerSpecArrayVsphereVolumeTypedDict]


class AlertmanagerSpecArrayTypedDict(AlertmanagerSpecArrayOptionalTypedDict,
    total=(True)):
    name: str


class AlertmanagerSpecResourcesTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class AlertmanagerSpecSecurityContextSeLinuxOptionsTypedDict(TypedDict,
    total=(False)):
    level: str
    role: str
    type: str
    user: str


class AlertmanagerSpecSecurityContextArrayTypedDict(TypedDict, total=(True)):
    name: str
    value: str


class AlertmanagerSpecSecurityContextWindowsOptionsTypedDict(TypedDict,
    total=(False)):
    gmsaCredentialSpec: str
    gmsaCredentialSpecName: str
    runAsUserName: str


class AlertmanagerSpecSecurityContextTypedDict(TypedDict, total=(False)):
    fsGroup: int
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextSeLinuxOptions,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextSeLinuxOptionsTypedDict
        ]
    supplementalGroups: Sequence[int]
    sysctls: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextArray,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextArrayTypedDict]]
    windowsOptions: Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextWindowsOptions,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextWindowsOptionsTypedDict
        ]


class AlertmanagerSpecStorageEmptyDirTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSourceOptionalTypedDict(
    TypedDict, total=(False)):
    apiGroup: str


class AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict(
    AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSourceOptionalTypedDict,
    total=(True)):
    kind: str
    name: str


class AlertmanagerSpecStorageVolumeClaimTemplateSpecResourcesTypedDict(
    TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict(
    AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorTypedDict(TypedDict
    , total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class AlertmanagerSpecStorageVolumeClaimTemplateSpecTypedDict(TypedDict,
    total=(False)):
    accessModes: Sequence[str]
    dataSource: Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSource
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecDataSourceTypedDict
        ]
    resources: Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecResources
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecResourcesTypedDict
        ]
    selector: Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelector
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecSelectorTypedDict
        ]
    storageClassName: str
    volumeMode: str
    volumeName: str


class AlertmanagerSpecStorageVolumeClaimTemplateStatusArrayOptionalTypedDict(
    TypedDict, total=(False)):
    lastProbeTime: str
    lastTransitionTime: str
    message: str
    reason: str


class AlertmanagerSpecStorageVolumeClaimTemplateStatusArrayTypedDict(
    AlertmanagerSpecStorageVolumeClaimTemplateStatusArrayOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class AlertmanagerSpecStorageVolumeClaimTemplateStatusTypedDict(TypedDict,
    total=(False)):
    accessModes: Sequence[str]
    capacity: Mapping[str, str]
    conditions: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatusArray
        ,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatusArrayTypedDict
        ]]
    phase: str


class AlertmanagerSpecStorageVolumeClaimTemplateTypedDict(TypedDict, total=
    (False)):
    apiVersion: str
    kind: str
    metadata: Mapping[str, Any]
    spec: Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpec,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateSpecTypedDict
        ]
    status: Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatus,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateStatusTypedDict
        ]


class AlertmanagerSpecStorageTypedDict(TypedDict, total=(False)):
    emptyDir: Union[kdsl.monitoring.v1.AlertmanagerSpecStorageEmptyDir,
        kdsl.monitoring.v1.AlertmanagerSpecStorageEmptyDirTypedDict]
    volumeClaimTemplate: Union[
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplate,
        kdsl.monitoring.v1.AlertmanagerSpecStorageVolumeClaimTemplateTypedDict]


class AlertmanagerSpecArrayAwsElasticBlockStoreOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class AlertmanagerSpecArrayAwsElasticBlockStoreTypedDict(
    AlertmanagerSpecArrayAwsElasticBlockStoreOptionalTypedDict, total=(True)):
    volumeID: str


class AlertmanagerSpecArrayAzureDiskOptionalTypedDict(TypedDict, total=(False)
    ):
    cachingMode: str
    fsType: str
    kind: str
    readOnly: bool


class AlertmanagerSpecArrayAzureDiskTypedDict(
    AlertmanagerSpecArrayAzureDiskOptionalTypedDict, total=(True)):
    diskName: str
    diskURI: str


class AlertmanagerSpecArrayAzureFileOptionalTypedDict(TypedDict, total=(False)
    ):
    readOnly: bool


class AlertmanagerSpecArrayAzureFileTypedDict(
    AlertmanagerSpecArrayAzureFileOptionalTypedDict, total=(True)):
    secretName: str
    shareName: str


class AlertmanagerSpecArrayCephfsSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class AlertmanagerSpecArrayCephfsOptionalTypedDict(TypedDict, total=(False)):
    path: str
    readOnly: bool
    secretFile: str
    secretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayCephfsSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCephfsSecretRefTypedDict]
    user: str


class AlertmanagerSpecArrayCephfsTypedDict(
    AlertmanagerSpecArrayCephfsOptionalTypedDict, total=(True)):
    monitors: Sequence[str]


class AlertmanagerSpecArrayCinderSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class AlertmanagerSpecArrayCinderOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayCinderSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCinderSecretRefTypedDict]


class AlertmanagerSpecArrayCinderTypedDict(
    AlertmanagerSpecArrayCinderOptionalTypedDict, total=(True)):
    volumeID: str


class AlertmanagerSpecArrayConfigMapArrayOptionalTypedDict(TypedDict, total
    =(False)):
    mode: int


class AlertmanagerSpecArrayConfigMapArrayTypedDict(
    AlertmanagerSpecArrayConfigMapArrayOptionalTypedDict, total=(True)):
    key: str
    path: str


class AlertmanagerSpecArrayConfigMapTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMapArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayConfigMapArrayTypedDict]]
    name: str
    optional: bool


class AlertmanagerSpecArrayCsiNodePublishSecretRefTypedDict(TypedDict,
    total=(False)):
    name: str


class AlertmanagerSpecArrayCsiOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    nodePublishSecretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayCsiNodePublishSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayCsiNodePublishSecretRefTypedDict
        ]
    readOnly: bool
    volumeAttributes: Mapping[str, str]


class AlertmanagerSpecArrayCsiTypedDict(
    AlertmanagerSpecArrayCsiOptionalTypedDict, total=(True)):
    driver: str


class AlertmanagerSpecArrayDownwardAPIArrayFieldRefOptionalTypedDict(TypedDict,
    total=(False)):
    apiVersion: str


class AlertmanagerSpecArrayDownwardAPIArrayFieldRefTypedDict(
    AlertmanagerSpecArrayDownwardAPIArrayFieldRefOptionalTypedDict, total=(
    True)):
    fieldPath: str


class AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRefTypedDict(
    AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict,
    total=(True)):
    resource: str


class AlertmanagerSpecArrayDownwardAPIArrayOptionalTypedDict(TypedDict,
    total=(False)):
    fieldRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayFieldRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayFieldRefTypedDict
        ]
    mode: int
    resourceFieldRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]


class AlertmanagerSpecArrayDownwardAPIArrayTypedDict(
    AlertmanagerSpecArrayDownwardAPIArrayOptionalTypedDict, total=(True)):
    path: str


class AlertmanagerSpecArrayDownwardAPITypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayDownwardAPIArrayTypedDict]]


class AlertmanagerSpecArrayEmptyDirTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class AlertmanagerSpecArrayFcTypedDict(TypedDict, total=(False)):
    fsType: str
    lun: int
    readOnly: bool
    targetWWNs: Sequence[str]
    wwids: Sequence[str]


class AlertmanagerSpecArrayFlexVolumeSecretRefTypedDict(TypedDict, total=(
    False)):
    name: str


class AlertmanagerSpecArrayFlexVolumeOptionalTypedDict(TypedDict, total=(False)
    ):
    fsType: str
    options: Mapping[str, str]
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolumeSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayFlexVolumeSecretRefTypedDict]


class AlertmanagerSpecArrayFlexVolumeTypedDict(
    AlertmanagerSpecArrayFlexVolumeOptionalTypedDict, total=(True)):
    driver: str


class AlertmanagerSpecArrayFlockerTypedDict(TypedDict, total=(False)):
    datasetName: str
    datasetUUID: str


class AlertmanagerSpecArrayGcePersistentDiskOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class AlertmanagerSpecArrayGcePersistentDiskTypedDict(
    AlertmanagerSpecArrayGcePersistentDiskOptionalTypedDict, total=(True)):
    pdName: str


class AlertmanagerSpecArrayGitRepoOptionalTypedDict(TypedDict, total=(False)):
    directory: str
    revision: str


class AlertmanagerSpecArrayGitRepoTypedDict(
    AlertmanagerSpecArrayGitRepoOptionalTypedDict, total=(True)):
    repository: str


class AlertmanagerSpecArrayGlusterfsOptionalTypedDict(TypedDict, total=(False)
    ):
    readOnly: bool


class AlertmanagerSpecArrayGlusterfsTypedDict(
    AlertmanagerSpecArrayGlusterfsOptionalTypedDict, total=(True)):
    endpoints: str
    path: str


class AlertmanagerSpecArrayHostPathOptionalTypedDict(TypedDict, total=(False)):
    type: str


class AlertmanagerSpecArrayHostPathTypedDict(
    AlertmanagerSpecArrayHostPathOptionalTypedDict, total=(True)):
    path: str


class AlertmanagerSpecArrayIscsiSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class AlertmanagerSpecArrayIscsiOptionalTypedDict(TypedDict, total=(False)):
    chapAuthDiscovery: bool
    chapAuthSession: bool
    fsType: str
    initiatorName: str
    iscsiInterface: str
    portals: Sequence[str]
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayIscsiSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayIscsiSecretRefTypedDict]


class AlertmanagerSpecArrayIscsiTypedDict(
    AlertmanagerSpecArrayIscsiOptionalTypedDict, total=(True)):
    iqn: str
    lun: int
    targetPortal: str


class AlertmanagerSpecArrayNfsOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class AlertmanagerSpecArrayNfsTypedDict(
    AlertmanagerSpecArrayNfsOptionalTypedDict, total=(True)):
    path: str
    server: str


class AlertmanagerSpecArrayPersistentVolumeClaimOptionalTypedDict(TypedDict,
    total=(False)):
    readOnly: bool


class AlertmanagerSpecArrayPersistentVolumeClaimTypedDict(
    AlertmanagerSpecArrayPersistentVolumeClaimOptionalTypedDict, total=(True)):
    claimName: str


class AlertmanagerSpecArrayPhotonPersistentDiskOptionalTypedDict(TypedDict,
    total=(False)):
    fsType: str


class AlertmanagerSpecArrayPhotonPersistentDiskTypedDict(
    AlertmanagerSpecArrayPhotonPersistentDiskOptionalTypedDict, total=(True)):
    pdID: str


class AlertmanagerSpecArrayPortworxVolumeOptionalTypedDict(TypedDict, total
    =(False)):
    fsType: str
    readOnly: bool


class AlertmanagerSpecArrayPortworxVolumeTypedDict(
    AlertmanagerSpecArrayPortworxVolumeOptionalTypedDict, total=(True)):
    volumeID: str


class AlertmanagerSpecArrayProjectedArrayConfigMapArrayOptionalTypedDict(
    TypedDict, total=(False)):
    mode: int


class AlertmanagerSpecArrayProjectedArrayConfigMapArrayTypedDict(
    AlertmanagerSpecArrayProjectedArrayConfigMapArrayOptionalTypedDict,
    total=(True)):
    key: str
    path: str


class AlertmanagerSpecArrayProjectedArrayConfigMapTypedDict(TypedDict,
    total=(False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMapArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMapArrayTypedDict
        ]]
    name: str
    optional: bool


class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    apiVersion: str


class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict(
    AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRefOptionalTypedDict
    , total=(True)):
    fieldPath: str


class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict(
    TypedDict, total=(False)):
    containerName: str
    divisor: str


class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict(
    AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefOptionalTypedDict
    , total=(True)):
    resource: str


class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayOptionalTypedDict(
    TypedDict, total=(False)):
    fieldRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRef
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayFieldRefTypedDict
        ]
    mode: int
    resourceFieldRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRef
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayResourceFieldRefTypedDict
        ]


class AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayTypedDict(
    AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayOptionalTypedDict,
    total=(True)):
    path: str


class AlertmanagerSpecArrayProjectedArrayDownwardAPITypedDict(TypedDict,
    total=(False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPIArrayTypedDict
        ]]


class AlertmanagerSpecArrayProjectedArraySecretArrayOptionalTypedDict(TypedDict
    , total=(False)):
    mode: int


class AlertmanagerSpecArrayProjectedArraySecretArrayTypedDict(
    AlertmanagerSpecArrayProjectedArraySecretArrayOptionalTypedDict, total=
    (True)):
    key: str
    path: str


class AlertmanagerSpecArrayProjectedArraySecretTypedDict(TypedDict, total=(
    False)):
    items: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecretArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecretArrayTypedDict
        ]]
    name: str
    optional: bool


class AlertmanagerSpecArrayProjectedArrayServiceAccountTokenOptionalTypedDict(
    TypedDict, total=(False)):
    audience: str
    expirationSeconds: int


class AlertmanagerSpecArrayProjectedArrayServiceAccountTokenTypedDict(
    AlertmanagerSpecArrayProjectedArrayServiceAccountTokenOptionalTypedDict,
    total=(True)):
    path: str


class AlertmanagerSpecArrayProjectedArrayTypedDict(TypedDict, total=(False)):
    configMap: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMap,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayConfigMapTypedDict
        ]
    downwardAPI: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPI,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayDownwardAPITypedDict
        ]
    secret: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecret,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArraySecretTypedDict]
    serviceAccountToken: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayServiceAccountToken
        ,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayServiceAccountTokenTypedDict
        ]


class AlertmanagerSpecArrayProjectedOptionalTypedDict(TypedDict, total=(False)
    ):
    defaultMode: int


class AlertmanagerSpecArrayProjectedTypedDict(
    AlertmanagerSpecArrayProjectedOptionalTypedDict, total=(True)):
    sources: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayProjectedArrayTypedDict]]


class AlertmanagerSpecArrayQuobyteOptionalTypedDict(TypedDict, total=(False)):
    group: str
    readOnly: bool
    tenant: str
    user: str


class AlertmanagerSpecArrayQuobyteTypedDict(
    AlertmanagerSpecArrayQuobyteOptionalTypedDict, total=(True)):
    registry: str
    volume: str


class AlertmanagerSpecArrayRbdSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class AlertmanagerSpecArrayRbdOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    keyring: str
    pool: str
    readOnly: bool
    secretRef: Union[kdsl.monitoring.v1.AlertmanagerSpecArrayRbdSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayRbdSecretRefTypedDict]
    user: str


class AlertmanagerSpecArrayRbdTypedDict(
    AlertmanagerSpecArrayRbdOptionalTypedDict, total=(True)):
    image: str
    monitors: Sequence[str]


class AlertmanagerSpecArrayScaleIOSecretRefTypedDict(TypedDict, total=(False)):
    name: str


class AlertmanagerSpecArrayScaleIOOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    protectionDomain: str
    readOnly: bool
    sslEnabled: bool
    storageMode: str
    storagePool: str
    volumeName: str


class AlertmanagerSpecArrayScaleIOTypedDict(
    AlertmanagerSpecArrayScaleIOOptionalTypedDict, total=(True)):
    gateway: str
    secretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIOSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayScaleIOSecretRefTypedDict]
    system: str


class AlertmanagerSpecArraySecretArrayOptionalTypedDict(TypedDict, total=(
    False)):
    mode: int


class AlertmanagerSpecArraySecretArrayTypedDict(
    AlertmanagerSpecArraySecretArrayOptionalTypedDict, total=(True)):
    key: str
    path: str


class AlertmanagerSpecArraySecretTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArraySecretArray,
        kdsl.monitoring.v1.AlertmanagerSpecArraySecretArrayTypedDict]]
    optional: bool
    secretName: str


class AlertmanagerSpecArrayStorageosSecretRefTypedDict(TypedDict, total=(False)
    ):
    name: str


class AlertmanagerSpecArrayStorageosTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageosSecretRef,
        kdsl.monitoring.v1.AlertmanagerSpecArrayStorageosSecretRefTypedDict]
    volumeName: str
    volumeNamespace: str


class AlertmanagerSpecArrayVsphereVolumeOptionalTypedDict(TypedDict, total=
    (False)):
    fsType: str
    storagePolicyID: str
    storagePolicyName: str


class AlertmanagerSpecArrayVsphereVolumeTypedDict(
    AlertmanagerSpecArrayVsphereVolumeOptionalTypedDict, total=(True)):
    volumePath: str


class AlertmanagerSpecTypedDict(TypedDict, total=(False)):
    additionalPeers: Sequence[str]
    affinity: Union[kdsl.monitoring.v1.AlertmanagerSpecAffinity,
        kdsl.monitoring.v1.AlertmanagerSpecAffinityTypedDict]
    baseImage: str
    configMaps: Sequence[str]
    configSecret: str
    containers: Sequence[Union[kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]
    externalUrl: str
    image: str
    imagePullSecrets: Sequence[Union[
        kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]
    initContainers: Sequence[Union[kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]
    listenLocal: bool
    logFormat: str
    logLevel: str
    nodeSelector: Mapping[str, str]
    paused: bool
    podMetadata: Mapping[str, Any]
    portName: str
    priorityClassName: str
    replicas: int
    resources: Union[kdsl.monitoring.v1.AlertmanagerSpecResources,
        kdsl.monitoring.v1.AlertmanagerSpecResourcesTypedDict]
    retention: str
    routePrefix: str
    secrets: Sequence[str]
    securityContext: Union[
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContext,
        kdsl.monitoring.v1.AlertmanagerSpecSecurityContextTypedDict]
    serviceAccountName: str
    sha: str
    storage: Union[kdsl.monitoring.v1.AlertmanagerSpecStorage,
        kdsl.monitoring.v1.AlertmanagerSpecStorageTypedDict]
    tag: str
    tolerations: Sequence[Union[kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]
    version: str
    volumeMounts: Sequence[Union[kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]
    volumes: Sequence[Union[kdsl.monitoring.v1.AlertmanagerSpecArray,
        kdsl.monitoring.v1.AlertmanagerSpecArrayTypedDict]]


class AlertmanagerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class AlertmanagerTypedDict(AlertmanagerOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.monitoring.v1.AlertmanagerSpec,
        kdsl.monitoring.v1.AlertmanagerSpecTypedDict]
