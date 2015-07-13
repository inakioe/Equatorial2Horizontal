##-------------------------------------------------------------------------
## Horizontal Coordinates
##-------------------------------------------------------------------------
# Author: Inaki Ordonez-Etxeberria
#
# This function transform the Equatorial coordinates of an object to a Horizontal Coordinates. If the parameters lat, lon and date are empty, the function assumes the position of the Isaac Newton Telescope in La Palma, at the moment of execution of the function. 

def eq2hor(AR, DEC, lat = '28.775867', lon =  '-17.89733', date = 'now'):
# Definition of the observatory place
    observatory = ephem.Observer()
    observatory.lon = str(lon)
    observatory.lat = str(lat)
    if date  ==  'now':
        observatory.date = ephem.now()
    else:
        observatory.date = ephem.Date(date)
    
    # Definition of the target
    AR =  radians(float(AR)*15) 
    DEC = radians(float(DEC))
    target = ephem.Equatorial(AR, DEC, epoch = ephem.J2000)
    
    # Computing the target from and observation point and moment.
    body = ephem.FixedBody()
    body._ra = target.ra
    body._dec = target.dec
    body._epoch = target.epoch
    body.compute(observatory)
    
    return( degrees(body.az),  degrees(body.alt))
