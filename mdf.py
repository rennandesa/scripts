#!/usr/bin/env python

import shutil


def get_fs() -> list:
    fs = []
    with open("/proc/filesystems") as f:
        lines = f.readlines()
        for line in lines:
            if "nodev" not in line:
                fs.append(line.strip())
        return fs


def get_mounts(fs: list) -> list:
    mounts = []
    with open("/proc/mounts") as f:
        lines = f.readlines()
        for line in lines:
            if line.split()[2] in fs:
                mounts.append((line.split()[1], line.split()[2]))
        return mounts


def convert_bytes(bytes: int) -> str:
    to_return = bytes/1024/1024
    if to_return > 1000:
        return f"{to_return/1024:.2f} GB".replace(".", ",")
    else:
        return f"{to_return:.2f} MB".replace(".", ",")


if __name__ == "__main__":
    filesystems = get_fs()
    mount_points = get_mounts(filesystems)
    total = 0
    total_use = 0
    total_free = 0


    for mount in mount_points:
        du = shutil.disk_usage(mount[0])
        total += du[0]
        total_use += du[1]
        total_free += du[2]
        print(f"{mount[0]:10} \ttype {mount[1]:5} \ttotal: {convert_bytes(du[0]):>10} \tused: {convert_bytes(du[1]):>10} \tfree: {convert_bytes(du[2]):>10}")

    print(" " * 30 + f"\ttotal: {convert_bytes(total):>10}" + " " * 13 + f"{convert_bytes(total_use):>10}" + " " * 14 + f"{convert_bytes(total_free):>10}")
