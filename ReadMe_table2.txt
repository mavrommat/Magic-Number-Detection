J/ApJS/243/3       Chandra observations of SINGS galaxies       (Lehmer+, 2019)
================================================================================
X-ray binary luminosity function scaling relations for local galaxies based on
subgalactic modeling.
    Lehmer B.D., Eufrasio R.T., Tzanavaris P., Basu-Zych A., Fragos T.,
    Prestwich A., Yukita M., Zezas A., Hornschemeier A.E., Ptak A.
   <Astrophys. J. Suppl. Ser., 243, 3-3 (2019)>
   =2019ApJS..243....3L    (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Galaxies, nearby; Binaries, X-ray; X-ray sources
Keywords: galaxies: evolution; stars: formation; X-rays: binaries;
          X-rays: galaxies

Abstract:
    We present new Chandra constraints on the X-ray luminosity functions
    (XLFs) of X-ray binary (XRB) populations, as well as their scaling
    relations, for a sample of 38 nearby galaxies (D=3.4-29Mpc). Our
    galaxy sample is drawn primarily from the Spitzer Infrared Nearby
    Galaxies Survey (SINGS) and contains a wealth of Chandra (5.8Ms total)
    and multiwavelength data, allowing for star formation rates (SFRs) and
    stellar masses (M_*_) to be measured on subgalactic scales. We divided
    the 2478 X-ray-detected sources into 21 subsamples in bins of specific
    SFR (sSFR=SFR/M_*_) and constructed XLFs. To model the XLF dependence
    on sSFR, we fit a global XLF model, containing contributions from
    high-mass XRBs (HMXBs), low-mass XRBs (LMXBs), and background sources
    from the cosmic X-ray background that respectively scale with SFR,
    M_*_, and sky area. We find an HMXB XLF that is more complex in shape
    than previously reported and an LMXB XLF that likely varies with sSFR,
    potentially due to an age dependence. When applying our global model
    to XLF data for each individual galaxy, we discover a few galaxy XLFs
    that significantly deviate from our model beyond statistical scatter.
    Most notably, relatively low-metallicity galaxies have an excess of
    HMXBs above ~10^38^erg/s, and elliptical galaxies that have relatively
    rich populations of globular clusters (GCs) show excesses of LMXBs
    compared to the global model. Additional modeling of how the XRB XLF
    depends on stellar age, metallicity, and GC specific frequency is
    required to sufficiently characterize the XLFs of galaxies.

Description:
    In this paper, we have utilized 5.8Ms of Chandra ACIS data, combined
    with UV-to-IR observations, for 38 nearby (D<~30Mpc) Spitzer Infrared
    Nearby Galaxies Survey (SINGS; Kennicutt+ 2003PASP..115..928K)
    galaxies to revisit scaling relations of the HMXB and LMXB X-ray
    luminosity functions (XLFs) with SFR and M_*_, respectively.

--------------------------------------------------------------------------------

See also:
 B/chandra : The Chandra Archive Log (CXC, 1999-2014)
 J/ApJ/586/794  : Multiwavelength luminosities of galaxies (Bell, 2003)
 J/ApJ/602/231  : Chandra X-ray point sources in nearby gal. (Colbert+, 2004)
 J/ApJ/617/240  : Oxygen abundances in the GOODS-North field (Kobulnicky+, 2004)
 J/ApJ/681/197  : ACS Virgo Cluster Survey. XV (Peng+, 2008)
 J/ApJ/695/580  : Oxygen abundance in M83 (Bresolin+, 2009)
 J/ApJS/190/233 : Spectroscopy and abundances of SINGS gal. (Moustakas+, 2010)
 J/MNRAS/419/2095 : HMXBs in nearby galaxies (Mineo+, 2012)
 J/ApJ/764/41   : X-ray binary evolution across cosmic time (Fragos+, 2013)
 J/ApJ/772/82   : A catalog of globular cluster systems (Harris+, 2013)
 J/ApJ/774/136  : SINGS gal. X-ray data compared to models (Tzanavaris+, 2013)
 J/AJ/146/86    : Cosmicflows-2 catalog (CF2) (Tully+, 2013)
 J/ApJ/776/L31  : Energy feedback from XRB from z=0 to z=19.92 (Fragos+, 2013)
 J/MNRAS/440/2265 : Spectroscopy of NGC3310 HII reg. (Miralles-Caballero+, 2014)
 J/ApJS/212/21  : A deep Chandra ACIS survey of M83 (Long+, 2014)
 J/ApJ/817/95   : X-ray observations of HCG galaxies (Tzanavaris+, 2016)
 J/ApJ/825/7    : Evolution of ~6Ms CDF-S galaxies (Lehmer+, 2016)
 J/MNRAS/466/1019 : Bright HMXBs in THINGS galaxies (Sazonov+, 2017)
 J/ApJ/865/43   : X-ray analysis of Chandra-COSMOS gal. (Fornasini+, 2018)


Byte-by-byte Description of file: table2.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label    Explanations
--------------------------------------------------------------------------------
   1-  7  A7    ---       Gal      Name of the host galaxy
   9- 11  A3    ---       ---      [NGC]
  12- 15  I4    ---       NGC      NGC number of the host galaxy as in Table 7;
                                    column added by CDS
  17- 21  I5    ---       ObsID    [354/21676]? Chandra Observation ID;
                                    null for merged IDs
      23  A1    ---     f_ObsID    [de] Flag on ObsID (1)
  25- 35  F11.7 deg       RAdeg    Right Ascension, Aim Point (J2000)
  37- 47  F11.7 deg       DEdeg    Declination, Aim Point (J2000)
  49- 67  A19   "datime"  ObsDate  UT Observation Date time
  69- 71  I3    ks        Exp      [2/892] Total exposure time (2)
      73  I1    ---       Nfl      [1/2]? Number of flaring intervals, rejected
  76- 78  F3.1  ks        Tfl      [0.5/2]? Combined flare duration, rejected
  80- 84  F5.2  arcsec    dRA      [-0.7/0.8]? Offset in Right Ascension
  86- 90  F5.2  arcsec    dDE      [-1.3/0.6]? Offset in Declination
  92- 92  A1    ---       Mode     [FV] Observation Mode (F=faint mode;
                                    or V=very faint mode)
--------------------------------------------------------------------------------
Note (1): Flag on Observations, including merged datasets as follows:
    d = Indicates Obs. ID by which all other observations are reprojected to
        for alignment purposes. This Obs. ID was chosen for reprojection as
        it had the longest initial exposure time, before flaring intervals
        were removed;
    e = Merged observations (ObsID is null) where the RAdeg,DEdeg of the aim
        point represents exposure-time weighted value.
Note (2): All observations were continuous. These times have been corrected
    for removed data that were affected by high background; see Section 3.2.
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

================================================================================
(End)                  Prepared by [AAS], Emmanuelle Perret [CDS]    06-Dec-2019