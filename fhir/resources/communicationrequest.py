# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class CommunicationRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A request for information to be sent to a receiver.
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """

    resource_type = Field("CommunicationRequest", const=True)

    about: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="about",
        title="Resources that pertain to this communication request",
        description=(
            "Other resources that pertain to this communication request and to "
            "which this communication request should be associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="When request transitioned to being actionable",
        description=(
            "For draft requests, indicates the date of initial creation.  For "
            "requests with other statuses, indicates the date of activation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfills plan or proposal",
        description=(
            "A plan or proposal that is fulfilled in whole or in part by this "
            "request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Message category",
        description=(
            "The type of message to be sent such as alert, notification, reminder, "
            "instruction, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="True if request is prohibiting action",
        description=(
            "If true indicates that the CommunicationRequest is asking for the "
            "specified action to *not* occur."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this CommunicationRequest was created or to"
            " which the creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Composite request this is part of",
        description=(
            "A shared identifier common to all requests that were authorized more "
            "or less simultaneously by a single author, representing the identifier"
            " of the requisition, prescription or similar form."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Business identifiers assigned to this communication request by the "
            "performer or other systems which remain constant as the resource is "
            "updated and propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    medium: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="medium",
        title="A channel of communication",
        description="A channel that was used for this communication (e.g. email, fax).",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about communication request",
        description=(
            "Comments made about the request by the requester, sender, recipient, "
            "subject or other participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When scheduled",
        description="The time when this communication is to occur.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When scheduled",
        description="The time when this communication is to occur.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    payload: typing.List[fhirtypes.CommunicationRequestPayloadType] = Field(
        None,
        alias="payload",
        title="Message payload",
        description=(
            "Text, attachment(s), or resource(s) to be communicated to the "
            "recipient."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Characterizes how quickly the proposed act must be initiated. Includes"
            " concepts such as stat, urgent, routine."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why is communication needed?",
        description="Describes why the request is being made in coded or textual form.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why is communication needed?",
        description="Indicates another resource whose existence justifies this request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    recipient: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="Message recipient",
        description=(
            "The entity (e.g. person, organization, clinical information system, "
            "device, group, or care team) which is the intended target of the "
            "communication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Group",
            "CareTeam",
            "HealthcareService",
        ],
    )

    replaces: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="Request(s) replaced by this request",
        description=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CommunicationRequest"],
    )

    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title="Who/what is requesting service",
        description=(
            "The device, individual, or organization who initiated the request and "
            "has responsibility for its activation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "RelatedPerson",
            "Device",
        ],
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title="Message sender",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which is to be the source of the communication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "HealthcareService",
        ],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
        description="The status of the proposal or order.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "active",
            "on-hold",
            "revoked",
            "completed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the CommunicationRequest.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Focus of message",
        description="The patient or group that is the focus of this communication request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CommunicationRequest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "basedOn",
            "replaces",
            "groupIdentifier",
            "status",
            "statusReason",
            "category",
            "priority",
            "doNotPerform",
            "medium",
            "subject",
            "about",
            "encounter",
            "payload",
            "occurrenceDateTime",
            "occurrencePeriod",
            "authoredOn",
            "requester",
            "recipient",
            "sender",
            "reasonCode",
            "reasonReference",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2294(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2294(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrencePeriod"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class CommunicationRequestPayload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message payload.
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """

    resource_type = Field("CommunicationRequestPayload", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Message part content",
        description=(
            "The communicated content (or for multi-part communications, one "
            "portion of the communication)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Message part content",
        description=(
            "The communicated content (or for multi-part communications, one "
            "portion of the communication)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Message part content",
        description=(
            "The communicated content (or for multi-part communications, one "
            "portion of the communication)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )
    contentString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentString", title="Extension field for ``contentString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CommunicationRequestPayload`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "contentString",
            "contentAttachment",
            "contentReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2992(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "content": ["contentAttachment", "contentReference", "contentString"]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
