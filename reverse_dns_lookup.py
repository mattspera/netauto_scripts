from argparse import ArgumentParser

from dns.resolver import Resolver
from dns.reversename import from_address
from dns.exception import DNSException

def lookup_hostname(ip, server):
    try:
        resolver = Resolver(configure=False)
        resolver.nameservers.append(server)
        try:
            rev_name = from_address(ip)
            query_res = resolver.query(rev_name, 'PTR')[0]
            return query_res
        except DNSException as e: # handle nxdomain error
            print(ip + ' -> ' + e.msg)
    except DNSException as e:
        print(e.msg)

def main():
    parser = ArgumentParser()
    parser.add_argument('--file', help='text file containing list of IPs', required=True)
    parser.add_argument('--server', help='dns server to query', required=True)
    args = parser.parse_args()

    with open(args.file, 'r') as file_obj:
        ip_list = file_obj.read().splitlines()

    for ip in ip_list:
        hostname = lookup_hostname(ip, args.server)
        if hostname: print(ip + ' -> ' + str(hostname))

if __name__ == "__main__":
    main()
