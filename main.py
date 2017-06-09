from mount import *



def get_partition(device):
    """ Restituisce tutte le partizioni per il dispositivo """
    partitionsFile = open("/proc/partitions")
    lines = partitionsFile.readlines()[2:]
    partitionsFile.close()
    partitions = ["/dev/" + line.split()[-1] for line in lines]
    return_partitions = []
    for p in partitions:
        if device in p and p != device:
            return_partitions.append(p)
    return return_partitions[0]

def mount(device, name=None):

    if not name:
        name = get_device_name(device)
    mount_partition(get_partition(device), name)





devices = list_media_devices()
if devices:
    device = devices[0]
    path = get_media_path(device)
    mount(device)

    if is_mounted(device):
        print device, "\nsalva sulla chiavetta"
        with open(path + "/hello-world.txt", "w") as f:
            f.write("Hello World")
        unmount(device)


    
else:
    print("salva in locale")
    path = "/home/stage/cartellafatta/"
    os.system("mkdir -p " + path)
    with open(path + "hello-world.txt", "w") as f:
        f.write("Hello World")
