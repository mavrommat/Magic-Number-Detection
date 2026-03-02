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

Byte-by-byte Description of file: table7.dat
--------------------------------------------------------------------------------
  Bytes Format Units       Label  Explanations
--------------------------------------------------------------------------------
  1-  3 A3     ---         ---    [NGC]
  4-  7 I4     ---         NGC    NGC number of the host galaxy
  9- 11 I3     ---         ID     Point-source identification number
                                   within the galaxy
 13- 22 F10.6  deg         RAdeg  Right Ascension, point source (J2000)
 24- 33 F10.6  deg         DEdeg  Declination, point source (J2000)
 35- 38 F4.1   arcmin      theta  [0/12.4] Offset (1)
 40- 47 F8.1   ct          NFB    [0.7/114995] Net (background subtracted)
                                   0.5-7keV counts
 49- 53 F5.1   ct        e_NFB    [1/359] 1{sigma} uncertainty in NFB
 55- 60 F6.3   10+22cm-2   NH     [0.008/15.5] Best-fit column density (2)
 62- 67 F6.3   10+22cm-2 e_NH     [0.001/14]?=-1 1{sigma} uncertainty in NH (2)
 69- 72 F4.2   ---         Gamma  [0.09/3.3] Best-fit photon index, {Gamma} (2)
 74- 78 F5.2   ---       e_Gamma  [0.01/3]?=-1 1{sigma} uncertainty in Gamma (2)
 80- 84 F5.1   [mW/m2]     logFFB [-16.6/-11.4] log, 0.5-8keV source flux
 86- 89 F4.1   [10-7W]     logLFB [34.8/41] log, 0.5-8keV source luminosity
 91- 91 I1     ---         Loc    [1/5] Location Flag (3)
--------------------------------------------------------------------------------
Note (1): Offset of the point source with respect to the average aim point
    of the Chandra observations.
Note (2): Best-fit column density NH and photon index {Gamma}, respectively,
    along with their respective 1{sigma} errors, based on spectral fits to an
    absorbed power-law model (TBABS * POW in xspec). For sources with small
    numbers of counts (<20 net counts), we adopted Galactic absorption
    appropriate for each galaxy and a photon index of {Gamma}=1.7.
Note (3): Flag indicating the location of the source within the galaxy.
    Flag as follows:
    1 = the source is within the Ks-band footprint adopted in Table 1, and
        outside a central region of avoidance, if applicable. All XLF
        calculations are based on Flag=1 sources;
    2 = source is within the Ks-band footprint, but has a luminosity of
        L<10^+35^erg/s, and was thus excluded from our XLF analysis;
    3 = indicates that the source is outside the 20mag/arcsec^2^ Ks-band
        ellipse of the galaxy, but within the "total" Ks-band ellipse.
    4 = the source is located in the central region of avoidance due to
        either the presence of an AGN or very high levels of source
        confusion.
    5 = indicates that the source is outside the "total" Ks-band ellipse.
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

================================================================================
(End)                  Prepared by [AAS], Emmanuelle Perret [CDS]    06-Dec-2019