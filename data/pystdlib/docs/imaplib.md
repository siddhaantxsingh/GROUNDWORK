# imaplib

## imaplib.IMAP4(host='', port=143, timeout=None)

IMAP4 client class. Instantiate with: IMAP4([host[, port[, timeout=None]]])

host - host's name (default: localhost);
        port - port number (default: standard IMAP4 port).
        timeout - socket timeout (default: None)
                  If timeout is not given or is None,
                  the global default socket timeout is used

All IMAP4rev1 commands are supported by methods of the same
name (in lowercase).

All arguments to commands are converted to strings, except for
AUTHENTICATE, and the last argument to APPEND which is passed as
an IMAP4 literal.  If necessary (the string contains any
non-printing characters or white-space and isn't enclosed with
either parentheses or double quotes) each string is quoted.
However, the 'password' argument to the LOGIN command is always
quoted.  If you want to avoid having an argument string quoted
(eg: the 'flags' argument to STORE) then enclose the string in
parentheses (eg: "(\Deleted)").

Each command returns a tuple: (type, [data, ...]) where 'type'
is usually 'OK' or 'NO', and 'data' is either the text from the
tagged response, or untagged results from command. Each 'data'
is either a string, or a tuple. If a tuple, then the first part
is the header of the response, and the second part contains
the data (ie: 'literal' value).

Errors raise the exception class <instance>.error("<reason>").
IMAP4 server errors raise <instance>.abort("<reason>"),
which is a sub-class of 'error'. Mailbox status changes
from READ-WRITE to READ-ONLY raise the exception class
<instance>.readonly("<reason>"), which is a sub-class of 'abort'.

"error" exceptions imply a program error.
"abort" exceptions imply the connection should be reset, and
        the command re-tried.
"readonly" exceptions imply the command should be re-tried.

Note: to use this module, you must read the RFCs pertaining to the
IMAP4 protocol, as the semantics of the arguments to each IMAP4
command are left to the invoker, not to mention the results. Also,
most IMAP servers implement a sub-set of the commands available here.

## imaplib.IMAP4.append(self, mailbox, flags, date_time, message)

Append message to named mailbox. (typ, [data]) = <instance>.append(mailbox, flags, date_time, message)

All args except `message' can be None.

## imaplib.IMAP4.authenticate(self, mechanism, authobject)

'mechanism' specifies which authentication mechanism is to
be used - it must appear in <instance>.capabilities in the
form AUTH=<mechanism>.

'authobject' must be a callable object:

data = authobject(response)

It will be called to process server continuation responses; the
response argument it is passed will be a bytes.  It should return bytes
data that will be base64 encoded and sent to the server.  It should
return None if the client abort response '*' should be sent instead.

## imaplib.IMAP4.capability(self)

(typ, [data]) = <instance>.capability() Fetch capabilities list from server.

## imaplib.IMAP4.check(self)

Checkpoint mailbox on server. (typ, [data]) = <instance>.check()

## imaplib.IMAP4.close(self)

Close currently selected mailbox. Deleted messages are removed from writable mailbox.
This is the recommended command before 'LOGOUT'.

(typ, [data]) = <instance>.close()

## imaplib.IMAP4.copy(self, message_set, new_mailbox)

Copy 'message_set' messages onto end of 'new_mailbox'. (typ, [data]) = <instance>.copy(message_set, new_mailbox)

## imaplib.IMAP4.create(self, mailbox)

Create new mailbox. (typ, [data]) = <instance>.create(mailbox)

## imaplib.IMAP4.delete(self, mailbox)

Delete old mailbox. (typ, [data]) = <instance>.delete(mailbox)

## imaplib.IMAP4.deleteacl(self, mailbox, who)

Delete the ACLs (remove any rights) set for who on mailbox. (typ, [data]) = <instance>.deleteacl(mailbox, who)

## imaplib.IMAP4.enable(self, capability)

Send an RFC5161 enable string to the server. (typ, [data]) = <instance>.enable(capability)

## imaplib.IMAP4.expunge(self)

Permanently remove deleted items from selected mailbox. Generates 'EXPUNGE' response for each deleted message.

(typ, [data]) = <instance>.expunge()

'data' is list of 'EXPUNGE'd message numbers in order received.

## imaplib.IMAP4.fetch(self, message_set, message_parts)

Fetch (parts of) messages. (typ, [data, ...]) = <instance>.fetch(message_set, message_parts)

'message_parts' should be a string of selected parts
enclosed in parentheses, eg: "(UID BODY[TEXT])".

'data' are tuples of message part envelope and data.

## imaplib.IMAP4.getacl(self, mailbox)

Get the ACLs for a mailbox. (typ, [data]) = <instance>.getacl(mailbox)

## imaplib.IMAP4.getannotation(self, mailbox, entry, attribute)

(typ, [data]) = <instance>.getannotation(mailbox, entry, attribute) Retrieve ANNOTATIONs.

## imaplib.IMAP4.getquota(self, root)

Get the quota root's resource usage and limits. Part of the IMAP4 QUOTA extension defined in rfc2087.

(typ, [data]) = <instance>.getquota(root)

## imaplib.IMAP4.getquotaroot(self, mailbox)

Get the list of quota roots for the named mailbox. (typ, [[QUOTAROOT responses...], [QUOTA responses]]) = <instance>.getquotaroot(mailbox)

## imaplib.IMAP4.list(self, directory='', pattern='*')

List mailbox names in directory matching pattern. (typ, [data]) = <instance>.list(directory='', pattern='*')

'data' is list of LIST responses.

## imaplib.IMAP4.login(self, user, password)

Identify client using plaintext password. (typ, [data]) = <instance>.login(user, password)

NB: 'password' will be quoted.

## imaplib.IMAP4.login_cram_md5(self, user, password)

Force use of CRAM-MD5 authentication. (typ, [data]) = <instance>.login_cram_md5(user, password)

## imaplib.IMAP4.logout(self)

Shutdown connection to server. (typ, [data]) = <instance>.logout()

Returns server 'BYE' response.

## imaplib.IMAP4.lsub(self, directory='', pattern='*')

List 'subscribed' mailbox names in directory matching pattern. (typ, [data, ...]) = <instance>.lsub(directory='', pattern='*')

'data' are tuples of message part envelope and data.

## imaplib.IMAP4.myrights(self, mailbox)

Show my ACLs for a mailbox (i.e. the rights that I have on mailbox). (typ, [data]) = <instance>.myrights(mailbox)

## imaplib.IMAP4.namespace(self)

Returns IMAP namespaces ala rfc2342 (typ, [data, ...]) = <instance>.namespace()

## imaplib.IMAP4.noop(self)

Send NOOP command. (typ, [data]) = <instance>.noop()

## imaplib.IMAP4.open(self, host='', port=143, timeout=None)

Setup connection to remote server on "host:port" (default: localhost:standard IMAP4 port). This connection will be used by the routines: read, readline, send, shutdown.

## imaplib.IMAP4.partial(self, message_num, message_part, start, length)

Fetch truncated part of a message. (typ, [data, ...]) = <instance>.partial(message_num, message_part, start, length)

'data' is tuple of message part envelope and data.

## imaplib.IMAP4.proxyauth(self, user)

Assume authentication as "user". Allows an authorised administrator to proxy into any user's
mailbox.

(typ, [data]) = <instance>.proxyauth(user)

## imaplib.IMAP4.read(self, size)

Read 'size' bytes from remote.

## imaplib.IMAP4.readline(self)

Read line from remote.

## imaplib.IMAP4.recent(self)

Return most recent 'RECENT' responses if any exist, else prompt server for an update using the 'NOOP' command. (typ, [data]) = <instance>.recent()

'data' is None if no new messages,
else list of RECENT responses, most recent last.

## imaplib.IMAP4.rename(self, oldmailbox, newmailbox)

Rename old mailbox name to new. (typ, [data]) = <instance>.rename(oldmailbox, newmailbox)

## imaplib.IMAP4.response(self, code)

Return data for response 'code' if received, or None. Old value for response 'code' is cleared.

(code, [data]) = <instance>.response(code)

## imaplib.IMAP4.search(self, charset, *criteria)

Search mailbox for matching messages. (typ, [data]) = <instance>.search(charset, criterion, ...)

'data' is space separated list of matching message numbers.
If UTF8 is enabled, charset MUST be None.

## imaplib.IMAP4.select(self, mailbox='INBOX', readonly=False)

Select a mailbox. Flush all untagged responses.

(typ, [data]) = <instance>.select(mailbox='INBOX', readonly=False)

'data' is count of messages in mailbox ('EXISTS' response).

Mandated responses are ('FLAGS', 'EXISTS', 'RECENT', 'UIDVALIDITY'), so
other responses should be obtained via <instance>.response('FLAGS') etc.

## imaplib.IMAP4.send(self, data)

Send data to remote.

## imaplib.IMAP4.setacl(self, mailbox, who, what)

Set a mailbox acl. (typ, [data]) = <instance>.setacl(mailbox, who, what)

## imaplib.IMAP4.setannotation(self, mailbox, *args)

(typ, [data]) = <instance>.setannotation(mailbox[, entry, attribute]+) Set ANNOTATIONs.

## imaplib.IMAP4.setquota(self, root, limits)

Set the quota root's resource limits. (typ, [data]) = <instance>.setquota(root, limits)

## imaplib.IMAP4.shutdown(self)

Close I/O established in "open".

## imaplib.IMAP4.socket(self)

Return socket instance used to connect to IMAP4 server. socket = <instance>.socket()

## imaplib.IMAP4.sort(self, sort_criteria, charset, *search_criteria)

IMAP4rev1 extension SORT command. (typ, [data]) = <instance>.sort(sort_criteria, charset, search_criteria, ...)

## imaplib.IMAP4.status(self, mailbox, names)

Request named status conditions for mailbox. (typ, [data]) = <instance>.status(mailbox, names)

## imaplib.IMAP4.store(self, message_set, command, flags)

Alters flag dispositions for messages in mailbox. (typ, [data]) = <instance>.store(message_set, command, flags)

## imaplib.IMAP4.subscribe(self, mailbox)

Subscribe to new mailbox. (typ, [data]) = <instance>.subscribe(mailbox)

## imaplib.IMAP4.thread(self, threading_algorithm, charset, *search_criteria)

IMAPrev1 extension THREAD command. (type, [data]) = <instance>.thread(threading_algorithm, charset, search_criteria, ...)

## imaplib.IMAP4.uid(self, command, *args)

Execute "command arg ..." with messages identified by UID, rather than message number. (typ, [data]) = <instance>.uid(command, arg1, arg2, ...)

Returns response appropriate to 'command'.

## imaplib.IMAP4.unselect(self)

Free server's resources associated with the selected mailbox and returns the server to the authenticated state. This command performs the same actions as CLOSE, except that no messages are permanently removed from the currently selected mailbox.

(typ, [data]) = <instance>.unselect()

## imaplib.IMAP4.unsubscribe(self, mailbox)

Unsubscribe from old mailbox. (typ, [data]) = <instance>.unsubscribe(mailbox)

## imaplib.IMAP4.xatom(self, name, *args)

Allow simple extension commands notified by server in CAPABILITY response. Assumes command is legal in current state.

(typ, [data]) = <instance>.xatom(name, arg, ...)

Returns response appropriate to extension command `name'.

## imaplib.IMAP4_SSL(host='', port=993, *, ssl_context=None, timeout=None)

Instantiate with: IMAP4_SSL([host[, port[, ssl_context[, timeout=None]]]])

host - host's name (default: localhost);
        port - port number (default: standard IMAP4 SSL port);
        ssl_context - a SSLContext object that contains your certificate chain
                      and private key (default: None)
        timeout - socket timeout (default: None) If timeout is not given or is None,
                  the global default socket timeout is used

for more documentation see the docstring of the parent class IMAP4.

## imaplib.IMAP4_SSL.open(self, host='', port=993, timeout=None)

Setup connection to remote server on "host:port". (default: localhost:standard IMAP4 SSL port). This connection will be used by the routines: read, readline, send, shutdown.

## imaplib.IMAP4_stream(command)

IMAP4 client class over a stream Instantiate with: IMAP4_stream(command)

"command" - a string that can be passed to subprocess.Popen()

for more documentation see the docstring of the parent class IMAP4.

## imaplib.IMAP4_stream.open(self, host=None, port=None, timeout=None)

Setup a stream connection. This connection will be used by the routines: read, readline, send, shutdown.

## imaplib.IMAP4_stream.read(self, size)

Read 'size' bytes from remote.

## imaplib.IMAP4_stream.readline(self)

Read line from remote.

## imaplib.IMAP4_stream.send(self, data)

Send data to remote.

## imaplib.IMAP4_stream.shutdown(self)

Close I/O established in "open".

## imaplib.Int2AP(num)

Convert integer to A-P string representation.

## imaplib.Internaldate2tuple(resp)

Parse an IMAP4 INTERNALDATE string. Return corresponding local time.  The return value is a
time.struct_time tuple or None if the string has wrong format.

## imaplib.ParseFlags(resp)

Convert IMAP4 flags response to python tuple.

## imaplib.Time2Internaldate(date_time)

Return string in form: '"DD-Mmm-YYYY HH:MM:SS +HHMM"'.  The
date_time argument can be a number (int or float) representing
seconds since epoch (as returned by time.time()), a 9-tuple
representing local time, an instance of time.struct_time (as
returned by time.localtime()), an aware datetime instance or a
double-quoted string.  In the last case, it is assumed to already
be in the correct format.
