# poplib

## poplib.POP3(host, port=110, timeout=<object object at 0x7fc8a19208c0>)

Arguments can be strings or integers (where appropriate) (e.g.: retr(1) and retr('1') both work equally well.

Minimal Command Set:
        USER name               user(name)
        PASS string             pass_(string)
        STAT                    stat()
        LIST [msg]              list(msg = None)
        RETR msg                retr(msg)
        DELE msg                dele(msg)
        NOOP                    noop()
        RSET                    rset()
        QUIT                    quit()

Optional Commands (some servers support these):
        RPOP name               rpop(name)
        APOP name digest        apop(name, digest)
        TOP msg n               top(msg, n)
        UIDL [msg]              uidl(msg = None)
        CAPA                    capa()
        STLS                    stls()
        UTF8                    utf8()

Raises one exception: 'error_proto'.

Instantiate with:
        POP3(hostname, port=110)

NB:     the POP protocol locks the mailbox from user
        authorization until QUIT, so be sure to get in, suck
        the messages, and quit, each time you access the
        mailbox.

POP is a line-based protocol, which means large mail
        messages consume lots of python cycles reading them
        line-by-line.

If it's available on your mail server, use IMAP4
        instead, it doesn't suffer from the two problems
        above.

## poplib.POP3.apop(self, user, password)

Authorisation - only possible if server has supplied a timestamp in initial greeting.

Args:
        user     - mailbox user;
        password - mailbox password.

NB: mailbox is locked by server from here to 'quit()'

## poplib.POP3.capa(self)

Return server capabilities (RFC 2449) as a dictionary >>> c=poplib.POP3('localhost') >>> c.capa() {'IMPLEMENTATION': ['Cyrus', 'POP3', 'server', 'v2.2.12'], 'TOP': [], 'LOGIN-DELAY': ['0'], 'AUTH-RESP-CODE': [], 'EXPIRE': ['NEVER'], 'USER': [], 'STLS': [], 'PIPELINING': [], 'UIDL': [], 'RESP-CODES': []} >>> Really, according to RFC 2449, the cyrus folks should avoid
having the implementation split into multiple arguments...

## poplib.POP3.close(self)

Close the connection without assuming anything about it.

## poplib.POP3.dele(self, which)

Delete message number 'which'. Result is 'response'.

## poplib.POP3.list(self, which=None)

Request listing, return result. Result without a message number argument is in form
['response', ['mesg_num octets', ...], octets].

Result when a message number argument is given is a
single response: the "scan listing" for that message.

## poplib.POP3.noop(self)

Does nothing. One supposes the response indicates the server is alive.

## poplib.POP3.pass_(self, pswd)

Send password, return response (response includes message count, mailbox size).

NB: mailbox is locked by server from here to 'quit()'

## poplib.POP3.quit(self)

Signoff: commit changes on server, unlock mailbox, close connection.

## poplib.POP3.retr(self, which)

Retrieve whole message number 'which'. Result is in form ['response', ['line', ...], octets].

## poplib.POP3.rpop(self, user)

Send RPOP command to access the mailbox with an alternate user.

## poplib.POP3.rset(self)

Unmark all messages marked for deletion.

## poplib.POP3.stat(self)

Get mailbox status. Result is tuple of 2 ints (message count, mailbox size)

## poplib.POP3.stls(self, context=None)

Start a TLS session on the active connection as specified in RFC 2595. context - a ssl.SSLContext

## poplib.POP3.top(self, which, howmuch)

Retrieve message header of message number 'which' and first 'howmuch' lines of message body. Result is in form ['response', ['line', ...], octets].

## poplib.POP3.uidl(self, which=None)

If 'which', result contains unique id for that message
in the form 'response mesgnum uid', otherwise result is
the list ['response', ['mesgnum uid', ...], octets]

## poplib.POP3.user(self, user)

Send user name, return response (should indicate password required).

## poplib.POP3.utf8(self)

Try to enter UTF-8 mode (see RFC 6856). Returns server response.

## poplib.POP3_SSL(host, port=995, *, timeout=<object object at 0x7fc8a19208c0>, context=None)

Instantiate with: POP3_SSL(hostname, port=995, context=None)

hostname - the hostname of the pop3 over ssl server
       port - port number
       context - a ssl.SSLContext

See the methods of the parent class POP3 for more documentation.

## poplib.POP3_SSL.stls(self, context=None)

The method unconditionally raises an exception since the STLS command doesn't make any sense on an already established SSL/TLS session.
