import bluetooth
print("Searching for device...")
nearby_devices = bluetooth.discover_devices(lookup_names = True)
print("found %d devices" % len(nearby_devices))
for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
