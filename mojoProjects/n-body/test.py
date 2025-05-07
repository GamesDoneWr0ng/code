import astropy.constants as c
import astropy.units as u

# moon mass in solar masses
print(c.M_moon.to(u.M_sun))