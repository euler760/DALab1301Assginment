def convert_temperature(value,unit):
    """    
    Convert temperature between Celsius and Fahrenheit.

    Parameters:
    - value: a number representing the temperature to convert
    - unit: a string that can be either:
        - 'C' if the input temperature is in Celsius
        - 'F' if the input temperature is in Fahrenheit

    Returns:
    - A string: the converted temperature rounded to 2 decimal places

    Examples:
    convert_temperature(0, 'C') should return "32.00"
    convert_temperature(32, 'F') should return "0.00"
    """
    if unit=="C":
        x=(9/5 * value) + 32
        y=str(x)
        z=y.partition('.')
        a=z[2][:2]
        b=""
        c=""
        TFah=""
        if len(a)==1:
            b=a+"0"
            TFah=z[0]+"."+b
            return TFah
        else:
            d=int(a[1])
            if 8>d>5:
                c=a[0]+str(d+1)
                TFah=z[0]+"."+c
                return TFah
            else:
                TFah=z[0]+"."+a
                return TFah
    elif unit=="F":
        x=5/9 * (value-32)
        y=str(x)
        z=y.partition('.')
        a=z[2][:2]
        b=""
        c=""
        TCel=""
        if len(a)==1:
            b=a+"0"
            TCel=z[0]+"."+b
            return TCel
        else:
            d=int(a[1])
            if 8>d>5:
                c=a[0]+str(d+1)
                TCel=z[0]+"."+c
                return TCel
            else:
                TCel=z[0]+"."+a
                return TCel
def estimate_protein_mass(num_amino_acids):
    """
    Estimate the mass of a protein based on the number of amino acids.
    
    Parameters:
    - num_amino_acids: an integer, the number of amino acids in the protein
    
    Returns:
    - An integer: estimated protein mass in daltons (Da)
    
    Assume the average mass of one amino acid residue is 110 Da.
    Example: estimate_protein_mass(50) should return 5500
    """
    promas=(num_amino_acids)*110
    return promas

