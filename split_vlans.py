import argparse

def split_trunk_vlans(vlans_string):

    vlans_list = []
    vlans_split = vlans_string.split(',')

    for i in vlans_split:
        if '-' in i:
            vlan_range_upper_lower = i.split('-')
            vlans_list.extend(vlan_range_upper_lower)
            vlan_range = range(int(vlan_range_upper_lower[0]), int(vlan_range_upper_lower[1]))

            for v in vlan_range:
                if str(v) not in vlans_list:
                    vlans_list.append(str(v))
        else:
            vlans_list.append(i)

    vlans_list.sort(key=float)

    return vlans_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vlans', help='trunk vlans to split into list', required=True)
    args = parser.parse_args()

    print(split_trunk_vlans(args.vlans))

if __name__ == "__main__":
    main()