# ipaddress

## ipaddress.AddressValueError(...)

A Value Error related to the address.

## ipaddress.IPv4Address(address)

Represent and manipulate single IPv4 Addresses.

## ipaddress.IPv4Network(address, strict=True)

This class represents and manipulates 32-bit IPv4 network + addresses.. Attributes: [examples for IPv4Network('192.0.2.0/27')]
    .network_address: IPv4Address('192.0.2.0')
    .hostmask: IPv4Address('0.0.0.31')
    .broadcast_address: IPv4Address('192.0.2.32')
    .netmask: IPv4Address('255.255.255.224')
    .prefixlen: 27

## ipaddress.IPv6Address(address)

Represent and manipulate single IPv6 Addresses.

## ipaddress.IPv6Network(address, strict=True)

This class represents and manipulates 128-bit IPv6 networks. Attributes: [examples for IPv6('2001:db8::1000/124')]
    .network_address: IPv6Address('2001:db8::1000')
    .hostmask: IPv6Address('::f')
    .broadcast_address: IPv6Address('2001:db8::100f')
    .netmask: IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0')
    .prefixlen: 124

## ipaddress.IPv6Network.hosts(self)

Generate Iterator over usable hosts in a network. This is like __iter__ except it doesn't return the
Subnet-Router anycast address.

## ipaddress.NetmaskValueError(...)

A Value Error related to the netmask.

## ipaddress.collapse_addresses(addresses)

Example:
    collapse_addresses([IPv4Network('192.0.2.0/25'),
                        IPv4Network('192.0.2.128/25')]) ->
                       [IPv4Network('192.0.2.0/24')]

Args:
    addresses: An iterable of IPv4Network or IPv6Network objects.

Returns:
    An iterator of the collapsed IPv(4|6)Network objects.

Raises:
    TypeError: If passed a list of mixed version objects.

## ipaddress.get_mixed_type_key(obj)

Address and Network objects are not sortable by default; they're
fundamentally different so the expression

IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

doesn't make any sense.  There are some times however, where you may wish
to have ipaddress sort these for you anyway. If you need to do this, you
can use this function as the key= argument to sorted().

Args:
  obj: either a Network or Address object.
Returns:
  appropriate key.

## ipaddress.ip_address(address)

Take an IP string/int and return an object of the correct type. Args:
    address: A string or integer, the IP address.  Either IPv4 or
      IPv6 addresses may be supplied; integers less than 2**32 will
      be considered to be IPv4 by default.

Returns:
    An IPv4Address or IPv6Address object.

Raises:
    ValueError: if the *address* passed isn't either a v4 or a v6
      address

## ipaddress.ip_interface(address)

Take an IP string/int and return an object of the correct type. Args:
    address: A string or integer, the IP address.  Either IPv4 or
      IPv6 addresses may be supplied; integers less than 2**32 will
      be considered to be IPv4 by default.

Returns:
    An IPv4Interface or IPv6Interface object.

Raises:
    ValueError: if the string passed isn't either a v4 or a v6
      address.

Notes:
    The IPv?Interface classes describe an Address on a particular
    Network, so they're basically a combination of both the Address
    and Network classes.

## ipaddress.ip_network(address, strict=True)

Take an IP string/int and return an object of the correct type. Args:
    address: A string or integer, the IP network.  Either IPv4 or
      IPv6 networks may be supplied; integers less than 2**32 will
      be considered to be IPv4 by default.

Returns:
    An IPv4Network or IPv6Network object.

Raises:
    ValueError: if the string passed isn't either a v4 or a v6
      address. Or if the network has host bits set.

## ipaddress.summarize_address_range(first, last)

Example:
    >>> list(summarize_address_range(IPv4Address('192.0.2.0'),
    ...                              IPv4Address('192.0.2.130')))
    ...                                #doctest: +NORMALIZE_WHITESPACE
    [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'),
     IPv4Network('192.0.2.130/32')]

Args:
    first: the first IPv4Address or IPv6Address in the range.
    last: the last IPv4Address or IPv6Address in the range.

Returns:
    An iterator of the summarized IPv(4|6) network objects.

Raise:
    TypeError:
        If the first and last objects are not IP addresses.
        If the first and last objects are not the same version.
    ValueError:
        If the last object is not greater than the first.
        If the version of the first address is not 4 or 6.

## ipaddress.v4_int_to_packed(address)

Args:
    address: An integer representation of an IPv4 IP address.

Returns:
    The integer address packed as 4 bytes in network (big-endian) order.

Raises:
    ValueError: If the integer is negative or too large to be an
      IPv4 IP address.

## ipaddress.v6_int_to_packed(address)

Represent an address as 16 packed bytes in network (big-endian) order. Args:
    address: An integer representation of an IPv6 IP address.

Returns:
    The integer address packed as 16 bytes in network (big-endian) order.
