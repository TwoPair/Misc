import tarfile

for i in range(1000,1,-1):
    tar = tarfile.open(f'{i}.tar')
    tarinfo = tar.getmember(tar.getnames()[0])
    tar.extract(tarinfo)