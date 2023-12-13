def create_phone_number(ls):
    n = ''.join(map(str, ls))
    nu = f"({n[0:3]}) {n[3:6]}-{n[6: ]}"
    return(nu)