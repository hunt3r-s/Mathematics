# Returns counts of significant digits for input
def numberOfSignificantDigits(n):
    
    # Convert n to float
    n = repr(float(n))
    
    # Split n at decimal point
    nSplit = n.split('.')
    whole = nSplit[0].lstrip('0')

    # Ensure n has only 1 decimal point
    if len(nSplit) == 2:
        decimal = nSplit[1].rstrip('0')
        return len(whole) + len(decimal)

    return len(whole)
