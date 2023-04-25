# generated by datamodel-codegen:
#   filename:  ConnectorRegistrySourceDefinition.yaml

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, Field
from typing_extensions import Literal


class ReleaseStage(BaseModel):
    __root__: Literal["alpha", "beta", "generally_available", "custom"] = Field(
        ...,
        description="enum that describes a connector's release stage",
        title="ReleaseStage",
    )


class ResourceRequirements(BaseModel):
    class Config:
        extra = Extra.forbid

    cpu_request: Optional[str] = None
    cpu_limit: Optional[str] = None
    memory_request: Optional[str] = None
    memory_limit: Optional[str] = None


class JobType(BaseModel):
    __root__: Literal[
        "get_spec",
        "check_connection",
        "discover_schema",
        "sync",
        "reset_connection",
        "connection_updater",
        "replicate",
    ] = Field(
        ...,
        description="enum that describes the different types of jobs that the platform runs.",
        title="JobType",
    )


class AllowedHosts(BaseModel):
    class Config:
        extra = Extra.allow

    hosts: Optional[List[str]] = Field(
        None,
        description="An array of hosts that this connector can connect to.  AllowedHosts not being present for the source or destination means that access to all hosts is allowed.  An empty list here means that no network access is granted.",
    )


class SuggestedStreams(BaseModel):
    class Config:
        extra = Extra.allow

    streams: Optional[List[str]] = Field(
        None,
        description="An array of streams that this connector suggests the average user will want.  SuggestedStreams not being present for the source means that all streams are suggested.  An empty list here means that no streams are suggested.",
    )


class JobTypeResourceLimit(BaseModel):
    class Config:
        extra = Extra.forbid

    jobType: JobType
    resourceRequirements: ResourceRequirements


class ActorDefinitionResourceRequirements(BaseModel):
    class Config:
        extra = Extra.forbid

    default: Optional[ResourceRequirements] = Field(
        None,
        description="if set, these are the requirements that should be set for ALL jobs run for this actor definition.",
    )
    jobSpecific: Optional[List[JobTypeResourceLimit]] = None


class ConnectorRegistrySourceDefinition(BaseModel):
    class Config:
        extra = Extra.allow

    sourceDefinitionId: UUID
    name: str
    dockerRepository: str
    dockerImageTag: str
    documentationUrl: str
    icon: Optional[str] = None
    sourceType: Optional[Literal["api", "file", "database", "custom"]] = None
    spec: Dict[str, Any]
    tombstone: Optional[bool] = Field(
        False,
        description="if false, the configuration is active. if true, then this configuration is permanently off.",
    )
    public: Optional[bool] = Field(
        False,
        description="true if this connector definition is available to all workspaces",
    )
    custom: Optional[bool] = Field(
        False, description="whether this is a custom connector definition"
    )
    releaseStage: Optional[ReleaseStage] = None
    releaseDate: Optional[date] = Field(
        None,
        description="The date when this connector was first released, in yyyy-mm-dd format.",
    )
    resourceRequirements: Optional[ActorDefinitionResourceRequirements] = None
    protocolVersion: Optional[str] = Field(
        None, description="the Airbyte Protocol version supported by the connector"
    )
    allowedHosts: Optional[AllowedHosts] = None
    suggestedStreams: Optional[SuggestedStreams] = None
    maxSecondsBetweenMessages: Optional[int] = Field(
        None,
        description="Number of seconds allowed between 2 airbyte protocol messages. The source will timeout if this delay is reach",
    )
