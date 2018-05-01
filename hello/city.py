def get_city_name(country,city,population=''):
    if population != None:
        printname = country+","+city+"-"+population
    else:
        printname = country+","+city
    return printname.title()
