def sum_wm_bins(da, wm_type):
    """Sum the bins within a specified water mass class
    slice values are from water-masses-defined.ipynb in ECCO dir"""
    
    
    if wm_type == 'cdw':
        return da.sel(sigma2_bin=slice(1037.00, 1037.22690)).sum('sigma2_bin')
    elif wm_type == 'wsdw':
        return da.sel(sigma2_bin=slice(1037.13206, 1037.23912)).sum('sigma2_bin')
    elif wm_type == 'wsbw':
        return da.sel(sigma2_bin=slice(1037.20743, 1037.30879)).sum('sigma2_bin')
    elif wm_type == 'isw':
        return da.sel(sigma2_bin=slice(1037.31602, 1037.39800)).sum('sigma2_bin') #HSSW lives w/in range    
    else:
        print('WM TypeError: unspecified water mass type provided')