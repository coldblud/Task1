from suryatask1.engine import DeviceFaker







def main():
    device_count = int(input("Enter the number of devices to generate data of:"))
    filename = input ("Enter filename to be saved:")

    devices = DeviceFaker.fake_devices(device_count)

    DeviceFaker.write_json_to_file(devices, filename)


if __name__=="__main__":
    main()
