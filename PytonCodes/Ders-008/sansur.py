def Sansur(cumleList,yasakliKelime,yeniKelime):
    for i in range(len(cumleList)):
        cumleList[i]=cumleList[i].replace(yasakliKelime,yeniKelime)
    return cumleList