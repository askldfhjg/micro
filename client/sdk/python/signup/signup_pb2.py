# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signup/signup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='signup/signup.proto',
  package='go.micro.service.signup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13signup/signup.proto\x12\x17go.micro.service.signup\"-\n\x1cSendVerificationEmailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\x1f\n\x1dSendVerificationEmailResponse\"-\n\rVerifyRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"\xad\x01\n\x0eVerifyResponse\x12\x35\n\tauthToken\x18\x01 \x01(\x0b\x32\".go.micro.service.signup.AuthToken\x12\x12\n\ncustomerID\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x18\n\x10payment_required\x18\x05 \x01(\x08\x12\x12\n\nnamespaces\x18\x06 \x03(\t\"@\n\x17SetPaymentMethodRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x16\n\x0epayment_method\x18\x02 \x01(\t\"\x1a\n\x18SetPaymentMethodResponse\"(\n\x17HasPaymentMethodRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\'\n\x18HasPaymentMethodResponse\x12\x0b\n\x03has\x18\x01 \x01(\x08\"q\n\x15\x43ompleteSignupRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x17\n\x0fpaymentMethodID\x18\x03 \x01(\t\x12\x0e\n\x06secret\x18\x04 \x01(\t\x12\x11\n\tnamespace\x18\x05 \x01(\t\"b\n\x16\x43ompleteSignupResponse\x12\x35\n\tauthToken\x18\x01 \x01(\x0b\x32\".go.micro.service.signup.AuthToken\x12\x11\n\tnamespace\x18\x02 \x01(\t\"Y\n\tAuthToken\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x0f\n\x07\x63reated\x18\x03 \x01(\x03\x12\x0e\n\x06\x65xpiry\x18\x04 \x01(\x03\"\x1f\n\x0eRecoverRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\x11\n\x0fRecoverResponse2\xaf\x05\n\x06Signup\x12\x86\x01\n\x15SendVerificationEmail\x12\x35.go.micro.service.signup.SendVerificationEmailRequest\x1a\x36.go.micro.service.signup.SendVerificationEmailResponse\x12Y\n\x06Verify\x12&.go.micro.service.signup.VerifyRequest\x1a\'.go.micro.service.signup.VerifyResponse\x12w\n\x10SetPaymentMethod\x12\x30.go.micro.service.signup.SetPaymentMethodRequest\x1a\x31.go.micro.service.signup.SetPaymentMethodResponse\x12w\n\x10HasPaymentMethod\x12\x30.go.micro.service.signup.HasPaymentMethodRequest\x1a\x31.go.micro.service.signup.HasPaymentMethodResponse\x12q\n\x0e\x43ompleteSignup\x12..go.micro.service.signup.CompleteSignupRequest\x1a/.go.micro.service.signup.CompleteSignupResponse\x12\\\n\x07Recover\x12\'.go.micro.service.signup.RecoverRequest\x1a(.go.micro.service.signup.RecoverResponseb\x06proto3'
)




_SENDVERIFICATIONEMAILREQUEST = _descriptor.Descriptor(
  name='SendVerificationEmailRequest',
  full_name='go.micro.service.signup.SendVerificationEmailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='go.micro.service.signup.SendVerificationEmailRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=93,
)


_SENDVERIFICATIONEMAILRESPONSE = _descriptor.Descriptor(
  name='SendVerificationEmailResponse',
  full_name='go.micro.service.signup.SendVerificationEmailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=126,
)


_VERIFYREQUEST = _descriptor.Descriptor(
  name='VerifyRequest',
  full_name='go.micro.service.signup.VerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='go.micro.service.signup.VerifyRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='go.micro.service.signup.VerifyRequest.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=173,
)


_VERIFYRESPONSE = _descriptor.Descriptor(
  name='VerifyResponse',
  full_name='go.micro.service.signup.VerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authToken', full_name='go.micro.service.signup.VerifyResponse.authToken', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customerID', full_name='go.micro.service.signup.VerifyResponse.customerID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='go.micro.service.signup.VerifyResponse.namespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='go.micro.service.signup.VerifyResponse.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payment_required', full_name='go.micro.service.signup.VerifyResponse.payment_required', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='go.micro.service.signup.VerifyResponse.namespaces', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=349,
)


_SETPAYMENTMETHODREQUEST = _descriptor.Descriptor(
  name='SetPaymentMethodRequest',
  full_name='go.micro.service.signup.SetPaymentMethodRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='go.micro.service.signup.SetPaymentMethodRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payment_method', full_name='go.micro.service.signup.SetPaymentMethodRequest.payment_method', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=415,
)


_SETPAYMENTMETHODRESPONSE = _descriptor.Descriptor(
  name='SetPaymentMethodResponse',
  full_name='go.micro.service.signup.SetPaymentMethodResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=443,
)


_HASPAYMENTMETHODREQUEST = _descriptor.Descriptor(
  name='HasPaymentMethodRequest',
  full_name='go.micro.service.signup.HasPaymentMethodRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='go.micro.service.signup.HasPaymentMethodRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=445,
  serialized_end=485,
)


_HASPAYMENTMETHODRESPONSE = _descriptor.Descriptor(
  name='HasPaymentMethodResponse',
  full_name='go.micro.service.signup.HasPaymentMethodResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='has', full_name='go.micro.service.signup.HasPaymentMethodResponse.has', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=526,
)


_COMPLETESIGNUPREQUEST = _descriptor.Descriptor(
  name='CompleteSignupRequest',
  full_name='go.micro.service.signup.CompleteSignupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='go.micro.service.signup.CompleteSignupRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='go.micro.service.signup.CompleteSignupRequest.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paymentMethodID', full_name='go.micro.service.signup.CompleteSignupRequest.paymentMethodID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='go.micro.service.signup.CompleteSignupRequest.secret', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='go.micro.service.signup.CompleteSignupRequest.namespace', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=641,
)


_COMPLETESIGNUPRESPONSE = _descriptor.Descriptor(
  name='CompleteSignupResponse',
  full_name='go.micro.service.signup.CompleteSignupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authToken', full_name='go.micro.service.signup.CompleteSignupResponse.authToken', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='go.micro.service.signup.CompleteSignupResponse.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=643,
  serialized_end=741,
)


_AUTHTOKEN = _descriptor.Descriptor(
  name='AuthToken',
  full_name='go.micro.service.signup.AuthToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='go.micro.service.signup.AuthToken.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='go.micro.service.signup.AuthToken.refresh_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='go.micro.service.signup.AuthToken.created', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='go.micro.service.signup.AuthToken.expiry', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=832,
)


_RECOVERREQUEST = _descriptor.Descriptor(
  name='RecoverRequest',
  full_name='go.micro.service.signup.RecoverRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='go.micro.service.signup.RecoverRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=865,
)


_RECOVERRESPONSE = _descriptor.Descriptor(
  name='RecoverResponse',
  full_name='go.micro.service.signup.RecoverResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=884,
)

_VERIFYRESPONSE.fields_by_name['authToken'].message_type = _AUTHTOKEN
_COMPLETESIGNUPRESPONSE.fields_by_name['authToken'].message_type = _AUTHTOKEN
DESCRIPTOR.message_types_by_name['SendVerificationEmailRequest'] = _SENDVERIFICATIONEMAILREQUEST
DESCRIPTOR.message_types_by_name['SendVerificationEmailResponse'] = _SENDVERIFICATIONEMAILRESPONSE
DESCRIPTOR.message_types_by_name['VerifyRequest'] = _VERIFYREQUEST
DESCRIPTOR.message_types_by_name['VerifyResponse'] = _VERIFYRESPONSE
DESCRIPTOR.message_types_by_name['SetPaymentMethodRequest'] = _SETPAYMENTMETHODREQUEST
DESCRIPTOR.message_types_by_name['SetPaymentMethodResponse'] = _SETPAYMENTMETHODRESPONSE
DESCRIPTOR.message_types_by_name['HasPaymentMethodRequest'] = _HASPAYMENTMETHODREQUEST
DESCRIPTOR.message_types_by_name['HasPaymentMethodResponse'] = _HASPAYMENTMETHODRESPONSE
DESCRIPTOR.message_types_by_name['CompleteSignupRequest'] = _COMPLETESIGNUPREQUEST
DESCRIPTOR.message_types_by_name['CompleteSignupResponse'] = _COMPLETESIGNUPRESPONSE
DESCRIPTOR.message_types_by_name['AuthToken'] = _AUTHTOKEN
DESCRIPTOR.message_types_by_name['RecoverRequest'] = _RECOVERREQUEST
DESCRIPTOR.message_types_by_name['RecoverResponse'] = _RECOVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendVerificationEmailRequest = _reflection.GeneratedProtocolMessageType('SendVerificationEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDVERIFICATIONEMAILREQUEST,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.SendVerificationEmailRequest)
  })
_sym_db.RegisterMessage(SendVerificationEmailRequest)

SendVerificationEmailResponse = _reflection.GeneratedProtocolMessageType('SendVerificationEmailResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDVERIFICATIONEMAILRESPONSE,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.SendVerificationEmailResponse)
  })
_sym_db.RegisterMessage(SendVerificationEmailResponse)

VerifyRequest = _reflection.GeneratedProtocolMessageType('VerifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYREQUEST,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.VerifyRequest)
  })
_sym_db.RegisterMessage(VerifyRequest)

VerifyResponse = _reflection.GeneratedProtocolMessageType('VerifyResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYRESPONSE,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.VerifyResponse)
  })
_sym_db.RegisterMessage(VerifyResponse)

SetPaymentMethodRequest = _reflection.GeneratedProtocolMessageType('SetPaymentMethodRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPAYMENTMETHODREQUEST,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.SetPaymentMethodRequest)
  })
_sym_db.RegisterMessage(SetPaymentMethodRequest)

SetPaymentMethodResponse = _reflection.GeneratedProtocolMessageType('SetPaymentMethodResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPAYMENTMETHODRESPONSE,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.SetPaymentMethodResponse)
  })
_sym_db.RegisterMessage(SetPaymentMethodResponse)

HasPaymentMethodRequest = _reflection.GeneratedProtocolMessageType('HasPaymentMethodRequest', (_message.Message,), {
  'DESCRIPTOR' : _HASPAYMENTMETHODREQUEST,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.HasPaymentMethodRequest)
  })
_sym_db.RegisterMessage(HasPaymentMethodRequest)

HasPaymentMethodResponse = _reflection.GeneratedProtocolMessageType('HasPaymentMethodResponse', (_message.Message,), {
  'DESCRIPTOR' : _HASPAYMENTMETHODRESPONSE,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.HasPaymentMethodResponse)
  })
_sym_db.RegisterMessage(HasPaymentMethodResponse)

CompleteSignupRequest = _reflection.GeneratedProtocolMessageType('CompleteSignupRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETESIGNUPREQUEST,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.CompleteSignupRequest)
  })
_sym_db.RegisterMessage(CompleteSignupRequest)

CompleteSignupResponse = _reflection.GeneratedProtocolMessageType('CompleteSignupResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETESIGNUPRESPONSE,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.CompleteSignupResponse)
  })
_sym_db.RegisterMessage(CompleteSignupResponse)

AuthToken = _reflection.GeneratedProtocolMessageType('AuthToken', (_message.Message,), {
  'DESCRIPTOR' : _AUTHTOKEN,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.AuthToken)
  })
_sym_db.RegisterMessage(AuthToken)

RecoverRequest = _reflection.GeneratedProtocolMessageType('RecoverRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOVERREQUEST,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.RecoverRequest)
  })
_sym_db.RegisterMessage(RecoverRequest)

RecoverResponse = _reflection.GeneratedProtocolMessageType('RecoverResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOVERRESPONSE,
  '__module__' : 'signup.signup_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.service.signup.RecoverResponse)
  })
_sym_db.RegisterMessage(RecoverResponse)



_SIGNUP = _descriptor.ServiceDescriptor(
  name='Signup',
  full_name='go.micro.service.signup.Signup',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=887,
  serialized_end=1574,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendVerificationEmail',
    full_name='go.micro.service.signup.Signup.SendVerificationEmail',
    index=0,
    containing_service=None,
    input_type=_SENDVERIFICATIONEMAILREQUEST,
    output_type=_SENDVERIFICATIONEMAILRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Verify',
    full_name='go.micro.service.signup.Signup.Verify',
    index=1,
    containing_service=None,
    input_type=_VERIFYREQUEST,
    output_type=_VERIFYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetPaymentMethod',
    full_name='go.micro.service.signup.Signup.SetPaymentMethod',
    index=2,
    containing_service=None,
    input_type=_SETPAYMENTMETHODREQUEST,
    output_type=_SETPAYMENTMETHODRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HasPaymentMethod',
    full_name='go.micro.service.signup.Signup.HasPaymentMethod',
    index=3,
    containing_service=None,
    input_type=_HASPAYMENTMETHODREQUEST,
    output_type=_HASPAYMENTMETHODRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CompleteSignup',
    full_name='go.micro.service.signup.Signup.CompleteSignup',
    index=4,
    containing_service=None,
    input_type=_COMPLETESIGNUPREQUEST,
    output_type=_COMPLETESIGNUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Recover',
    full_name='go.micro.service.signup.Signup.Recover',
    index=5,
    containing_service=None,
    input_type=_RECOVERREQUEST,
    output_type=_RECOVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIGNUP)

DESCRIPTOR.services_by_name['Signup'] = _SIGNUP

# @@protoc_insertion_point(module_scope)