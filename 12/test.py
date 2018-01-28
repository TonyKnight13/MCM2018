import netCDF4 as nc  

nc_obj=nc.Dataset("C:\\Users\\Administrator\\Desktop\\air.mon.anom.nc") 
print(nc_obj)  

print(nc_obj.variables.keys())
l = list(nc_obj.variables.keys())  
for i in range(len(l)):
    #查看nc文件中的變量
    print(nc_obj.variables[l[i]])  
    #查看U這個變量的屬性 
    print(nc_obj.variables[l[i]].ncattrs()) 
    #讀取數據值
    print(nc_obj.variables[l[i]][:])
    print('***************************')