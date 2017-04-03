import socket


def connectable(address, port, timeout=None):
    """Test TCP connectivity on an addr:port.

     Arguments:
        address (str): An IP address or FQDN of a host
        port (int): TCP destination port to use

    Returns:
        (bool): True if alive, False if not
    """
    s = None
    try:
        s = socket.create_connection((address, port), timeout=timeout)
        return True
    except socket.error:
        return False
    finally:
        if s is not None:
            s.close()
