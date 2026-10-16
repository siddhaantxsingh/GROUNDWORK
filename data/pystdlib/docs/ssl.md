# ssl

## ssl.AlertDescription(*values)

An enumeration.

## ssl.CertificateError(...)

A certificate could not be verified.

## ssl.DER_cert_to_PEM_cert(der_cert_bytes)

Takes a certificate in binary DER format and returns the PEM version of it as a string.

## ssl.DefaultVerifyPaths(cafile, capath, openssl_cafile_env, openssl_cafile, openssl_capath_env, openssl_capath)

DefaultVerifyPaths(cafile, capath, openssl_cafile_env, openssl_cafile, openssl_capath_env, openssl_capath)

## ssl.Options(*values)

An enumeration.

## ssl.PEM_cert_to_DER_cert(pem_cert_string)

Takes a certificate in ASCII PEM format and returns the DER-encoded version of it as a byte sequence

## ssl.Purpose(*values)

SSLContext purpose flags with X509v3 Extended Key Usage objects

## ssl.SSLCertVerificationError(...)

A certificate could not be verified.

## ssl.SSLContext(protocol=None, *args, **kwargs)

An SSLContext holds various SSL-related configuration options and data, such as certificates and possibly a private key.

## ssl.SSLEOFError(...)

SSL/TLS connection terminated abruptly.

## ssl.SSLError(...)

An error occurred in the SSL implementation.

## ssl.SSLErrorNumber(*values)

An enumeration.

## ssl.SSLObject(*args, **kwargs)

This object captures the state of an SSL connection but does not provide any network IO itself. IO needs to be performed through separate "BIO" objects which are OpenSSL's IO abstraction layer.

This class does not have a public constructor. Instances are returned by
``SSLContext.wrap_bio``. This class is typically used by framework authors
that want to implement asynchronous IO for SSL through memory buffers.

When compared to ``SSLSocket``, this object lacks the following features:

* Any form of network IO, including methods such as ``recv`` and ``send``.
 * The ``do_handshake_on_connect`` and ``suppress_ragged_eofs`` machinery.

## ssl.SSLObject.cipher(self)

Return the currently selected cipher as a 3-tuple ``(name, ssl_version, secret_bits)``.

## ssl.SSLObject.compression(self)

Return the current compression algorithm in use, or ``None`` if compression was not negotiated or not supported by one of the peers.

## ssl.SSLObject.do_handshake(self)

Start the SSL/TLS handshake.

## ssl.SSLObject.get_channel_binding(self, cb_type='tls-unique')

Get channel binding data for current connection. Raise ValueError if the requested `cb_type` is not supported. Return bytes of the data or None if the data is not available (e.g. before the handshake).

## ssl.SSLObject.get_unverified_chain(self)

Returns raw certificate chain provided by the other end of the SSL channel as a list of DER-encoded bytes.

## ssl.SSLObject.get_verified_chain(self)

Returns verified certificate chain provided by the other end of the SSL channel as a list of DER-encoded bytes. If certificate verification was disabled method acts the same as
``SSLSocket.get_unverified_chain``.

## ssl.SSLObject.getpeercert(self, binary_form=False)

Returns a formatted version of the data in the certificate provided by the other end of the SSL channel. Return None if no certificate was provided, {} if a certificate was
provided, but not validated.

## ssl.SSLObject.pending(self)

Return the number of bytes that can be read immediately.

## ssl.SSLObject.read(self, len=1024, buffer=None)

Read up to 'len' bytes from the SSL object and return them. If 'buffer' is provided, read into this buffer and return the number of
bytes read.

## ssl.SSLObject.selected_alpn_protocol(self)

Return the currently selected ALPN protocol as a string, or ``None`` if a next protocol was not negotiated or if ALPN is not supported by one of the peers.

## ssl.SSLObject.selected_npn_protocol(self)

Return the currently selected NPN protocol as a string, or ``None`` if a next protocol was not negotiated or if NPN is not supported by one of the peers.

## ssl.SSLObject.shared_ciphers(self)

Return a list of ciphers shared by the client during the handshake or None if this is not a valid server connection.

## ssl.SSLObject.unwrap(self)

Start the SSL shutdown handshake.

## ssl.SSLObject.version(self)

Return a string identifying the protocol version used by the current SSL channel.

## ssl.SSLObject.write(self, data)

Write 'data' to the SSL object and return the number of bytes written. The 'data' argument must support the buffer interface.

## ssl.SSLSocket(*args, **kwargs)

This class implements a subtype of socket.socket that wraps the underlying OS socket in an SSL context when necessary, and provides read and write methods over that channel.

## ssl.SSLSocket.accept(self)

Accepts a new connection from a remote client, and returns a tuple containing that new connection wrapped with a server-side SSL channel, and the address of the remote client.

## ssl.SSLSocket.cipher(self)

Return the currently selected cipher as a 3-tuple ``(name, ssl_version, secret_bits)``.

## ssl.SSLSocket.compression(self)

Return the current compression algorithm in use, or ``None`` if compression was not negotiated or not supported by one of the peers.

## ssl.SSLSocket.connect(self, addr)

Connects to remote ADDR, and then wraps the connection in an SSL channel.

## ssl.SSLSocket.connect_ex(self, addr)

Connects to remote ADDR, and then wraps the connection in an SSL channel.

## ssl.SSLSocket.do_handshake(self, block=False)

Start the SSL/TLS handshake.

## ssl.SSLSocket.get_channel_binding(self, cb_type='tls-unique')

Get channel binding data for current connection. Raise ValueError if the requested `cb_type` is not supported. Return bytes of the data or None if the data is not available (e.g. before the handshake).

## ssl.SSLSocket.get_unverified_chain(self)

Returns raw certificate chain provided by the other end of the SSL channel as a list of DER-encoded bytes.

## ssl.SSLSocket.get_verified_chain(self)

Returns verified certificate chain provided by the other end of the SSL channel as a list of DER-encoded bytes. If certificate verification was disabled method acts the same as
``SSLSocket.get_unverified_chain``.

## ssl.SSLSocket.getpeercert(self, binary_form=False)

Returns a formatted version of the data in the certificate provided by the other end of the SSL channel. Return None if no certificate was provided, {} if a certificate was
provided, but not validated.

## ssl.SSLSocket.pending(self)

Return the number of bytes that can be read immediately.

## ssl.SSLSocket.read(self, len=1024, buffer=None)

Read up to LEN bytes and return them. Return zero-length string on EOF.

## ssl.SSLSocket.selected_alpn_protocol(self)

Return the currently selected ALPN protocol as a string, or ``None`` if a next protocol was not negotiated or if ALPN is not supported by one of the peers.

## ssl.SSLSocket.selected_npn_protocol(self)

Return the currently selected NPN protocol as a string, or ``None`` if a next protocol was not negotiated or if NPN is not supported by one of the peers.

## ssl.SSLSocket.sendfile(self, file, offset=0, count=None)

Send a file, possibly by using os.sendfile() if this is a clear-text socket. Return the total number of bytes sent.

## ssl.SSLSocket.shared_ciphers(self)

Return a list of ciphers shared by the client during the handshake or None if this is not a valid server connection.

## ssl.SSLSocket.unwrap(self)

Start the SSL shutdown handshake.

## ssl.SSLSocket.version(self)

Return a string identifying the protocol version used by the current SSL channel.

## ssl.SSLSocket.write(self, data)

Write DATA to the underlying SSL channel. Returns number of bytes of DATA actually transmitted.

## ssl.SSLSyscallError(...)

System error when attempting SSL operation.

## ssl.SSLWantReadError(...)

Non-blocking SSL socket needs to read more data before the requested operation can be completed.

## ssl.SSLWantWriteError(...)

Non-blocking SSL socket needs to write more data before the requested operation can be completed.

## ssl.SSLZeroReturnError(...)

SSL/TLS session closed cleanly.

## ssl.TLSVersion(*values)

An enumeration.

## ssl.VerifyFlags(*values)

An enumeration.

## ssl.VerifyMode(*values)

An enumeration.

## ssl.cert_time_to_seconds(cert_time)

"notBefore" or "notAfter" dates must use UTC (RFC 5280).

Month is one of: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
UTC should be specified as GMT (see ASN1_TIME_print())

## ssl.create_default_context(purpose=<Purpose.SERVER_AUTH: _ASN1Object(nid=129, shortname='serverAuth', longname='TLS Web Server Authentication', oid='1.3.6.1.5.5.7.3.1')>, *, cafile=None, capath=None, cadata=None)

Create a SSLContext object with default settings. NOTE: The protocol and settings may change anytime without prior
      deprecation. The values represent a fair balance between maximum
      compatibility and security.

## ssl.get_default_verify_paths()

Return paths to default cafile and capath.

## ssl.get_server_certificate(addr, ssl_version=<_SSLMethod.PROTOCOL_TLS_CLIENT: 16>, ca_certs=None, timeout=<object object at 0x7fc8a19208c0>)

If 'ca_certs' is specified, validate the server cert against it. If 'ssl_version' is specified, use it in the connection attempt. If 'timeout' is specified, use it in the connection attempt.
