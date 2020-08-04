import socket


def services_by_range(lower_port=0, upper_port=1023):
    if not isinstance(lower_port, int) or not isinstance(upper_port, int):
        print("Invalid port range.")
        return
    if lower_port > upper_port or lower_port < 0 or upper_port > 65535:
        print("Invalid port range.")
        return

    count = 0
    for i in range(lower_port, upper_port + 1):
        try:
            service = socket.getservbyport(i, 'tcp')
            count += 1
            print(f"TCP/{i} : {service}")
        except socket.error:
            pass

        try:
            service = socket.getservbyport(i, 'udp')
            count += 1
            print(f"UDP/{i} : {service}")
        except socket.error:
            pass

    if count == 0:
        print(
            f"No known services in the port range {lower_port} to {upper_port}.")
    else:
        print(
            f"Found {count} known services in the port range {lower_port} to {upper_port}.")
