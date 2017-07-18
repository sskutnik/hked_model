# HPAT: HKED Python Analysis Tool
# Matthew T. Cook
# 12 March 2014
# Department of Nuclear Engineering
# University of Tennessee, Knoxville

# import modules
import os as os
import numpy as np
import matplotlib.pyplot as plt
import warnings
#import math as math
#from matplotlib.backends.backend_pdf import PdfPages as pp
#from matplotlib.ticker import MultipleLocator

################################################################################
# Warning control
# Set script to ignore runtime warnings from modelResid divide by zero
warnings.simplefilter("ignore")

################################################################################
# Clear the screen
os.system('clear')

# Identify script
print("-----------------------------")
print("| HKED Python Analysis Tool |")
print("-----------------------------")

# Hardcode file name in for now
#fileName = raw_input("Enter file to analyze: ")
fileName = "hked_v11_xrf_s1_nr0.o"
specFile = "exdata/045gL_ked_u.txt"
# Hardcode sample type
sType = "U" # Options: "U" or "U-Pu"

# Hardcode figure file names
figName = "045gL_ked_U_full.pdf"
figNameROI = "045gL_ked_U_detail.pdf"
figName2 = "045gL_ked_U_full.png"
figNameROI2 = "045gL_ked_U_detail.png"

## Ask the user what to do
#plotResults = raw_input("Plot the results? (y/n): ")
#
## Ask user if a measured spectrum is to be analyzed
#importSpectrum = raw_input("Analyze a measured spectrum? (y/n): ")

################################################################################
# Open and create files needed by this script
# Open the input file for reading
f = open(fileName, "r")

# rename the input file and open it as a post processed output
base = os.path.splitext(fileName)[0]
outFile = base + ".opp"
sourceFile = base + ".src"

# create and open the output files for writing
o = open(outFile, "w")
s = open(sourceFile, "wb")

################################################################################
# Determine the run type and search terms

# Tell the user what's going on
print "Processing MCNP output:", fileName
# Search the file for XRF-RUN or KED-RUN tags
with f as search:
    for line in search:
        # Remove '\n' at end of line
        line = line.rstrip()
        if "xrf-s1" in line:
            aType = "XRF-S1"
            print "Run Type:", aType   
            break        
        elif "xrf-s2" in line:
            aType = "XRF-S2"
            print "Run Type:", aType           
            break
        elif "ked-s1" in line:
            aType = "KED-S1"
            print "Run Type:", aType           
            break
        elif "ked-s2" in line:
            aType = "KED-S2"
            print "Run Type:", aType           
            break

if aType == "XRF-S2" or aType == "KED-S2":
    # Ask the user what to do
    plotResults = "y" #raw_input("Plot the results? (y/n): ")
    #plotResults = "n"

    # Ask user if a measured spectrum is to be analyzed
    importSpectrum = "y" #raw_input("Analyze a measured spectrum? (y/n): ")
if aType == "XRF-S1" or aType == "KED-S1":
    importSpectrum = "n"
    plotResults = "n"


# Tell the user where the extracted spectrum is
print "MCNP tally extracted to:",outFile

# Set the tally surface/volume search string
if aType == "XRF-S1":
    searchPhrase = " surface  608.2"
    print "Searched MCNP output for:", searchPhrase
elif aType == "XRF-S2":
    searchPhrase = " cell  75"
    print "Searched MCNP output for:", searchPhrase
elif aType == "KED-S1":
    searchPhrase = " surface  311.2"
    print "Searched MCNP output for:", searchPhrase
elif aType == "KED-S2":
    searchPhrase = " cell  44"
    print "Searched MCNP output for:", searchPhrase             
               
################################################################################
# Create an output file and extract spectrum from MCNP output

if aType == "XRF-S1" or aType == "KED-S1":
    # Identify Stage 1 analysis
    print "Extracting Stage 1 F2 tally..."
    # Search for the specified string in the input file
    with open(fileName) as search:
        for line in search:
            # Remove '\n' at end of line
            line = line.rstrip()
            if searchPhrase in line:
                #for x in range (0,2053):
                #for x in range (0,602):
                #for x in range (0,2051):
                for x in range (0,8194):
                        line = search.next()
                   	# Remove the spaces between tally values 
                   	# and replace with commas
                   	line = line.replace('    ','')
                   	line = line.replace('   ',',')
                   	line = line.replace(' ',',')
                   	line = line.replace(',,energy,','energy')
                   	line = line.replace(',,total,,','total,')
                   	# Write the data to analysis file in CSV format
                   	o.write(line)
    # Close and reopen output file to flush the buffer
    o.close()
    o = open(outFile,"r")

################################################################################
# Create source file from Stage 1 tally for Stage 2 source

# write the Stage 2 SDEF options to the new source file
#if aType == "XRF-S1":
#    s2sdef = "SDEF VEC=-0.692 -0.721 0 DIR=1 POS=-9.57 -9.97 0 ERG=D1 PAR=2 ARA=0.001"
#elif aType =="KED-S1":
#    s2sdef = "SDEF VEC=1 0 0 DIR=1 POS=19.8545  0  0 ERG=D1 PAR=2 ARA=0.001"

# write the Stage 2 SDEF options to the new source file with a Cd-109 check source
if aType == "XRF-S1":
    s2sdef = "SDEF VEC=-0.692 -0.721 0  DIR=1 POS=D1  ERG=FPOS=D2 PAR=2 ARA=0.001 \n"
    s2sdef = s2sdef + "SI1 L  -9.57 -9.97 0      -9.57 -9.97 0 \n"
    s2sdef = s2sdef + "SP1     1                1E-3 \n"
    s2sdef = s2sdef + "DS2 S   4                3 \n"
    s2sdef = s2sdef + "SI3 L   0.02199 0.022163 0.024912 0.02943 0.025455 0.0880336 \n"
    s2sdef = s2sdef + "SP3 D   0.298   0.561    0.048    0.092   0.0231   0.0370"
elif aType =="KED-S1":
    s2sdef = "SDEF VEC=1 0 0 DIR=1 POS=D1  ERG=FPOS=D2 PAR=2 ARA=0.001 \n"
    s2sdef = s2sdef + "SI1 L  19.8545 0 0      19.8545 1 0 \n"
    s2sdef = s2sdef + "SP1     1                1E-3 \n"
    s2sdef = s2sdef + "DS2 S   4                3 \n"
    s2sdef = s2sdef + "SI3 L   0.02199 0.022163 0.024912 0.02943 0.025455 0.0880336 \n"
    s2sdef = s2sdef + "SP3 D   0.298   0.561    0.048    0.092   0.0231   0.0370"

if aType == "XRF-S1" or aType == "KED-S1":
    print "Writing Stage 2 source file..."
    # write source file header
    sheader = "c Source file processed from output: "
    s.write(sheader + fileName + "\n")
    s.write(s2sdef + "\n")
    
    # import the source data from the preprocessed output file
    sourcein = np.genfromtxt(outFile, delimiter=",", skip_header=1, skip_footer=1, 
            usecols=(0,1))
    mcnpEnergy = np.genfromtxt(outFile, delimiter=",", skip_header=1, skip_footer=1, 
            usecols=(0))
    mcnpTally = np.genfromtxt(outFile, delimiter=",", skip_header=1, skip_footer=1, 
            usecols=(1))
    mcnpError= np.genfromtxt(outFile, delimiter=",", skip_header=1, skip_footer=1, 
            usecols=(2))
    
    # sum the source and copy the energies
    sumsource = sum(sourcein[:,1])
    sourceenergy = sourcein[:,0]
    
    # normalize the Stage 1 tally
    for x in range(0,len(sourcein)):
        sourcenorm = sourcein[:,1]/sumsource
    
    # write source energies
    for x in range(0,len(sourcein)):
        if x == 0:
            #soutline1 = "SI1 L  "
            # Use SI1 L for source with Cd-109
            soutline1 = "SI4 L  "
            soutline2 = str(sourceenergy[x])
            s.write(soutline1)
            s.write(soutline2 + "\n")
        else:
            soutline = ("       " + str(sourceenergy[x]))
            s.write(soutline + "\n")
    
    # write the source intensities
    for x in range(0,len(sourcein)):
        if x == 0:
            #soutline1 = "SP1 D  "
            # Use SP4 D for source with Cd-109
            soutline1 = "SP4 D  "
            soutline2 = str(sourcenorm[x])
            s.write(soutline1)
            s.write(soutline2 + "\n")
        else:
            soutline = ("       " + str(sourcenorm[x]))
            s.write(soutline + "\n")
            
    # tell user where the source file was written
    print "Stage 1 tally written to Stage 2 source file:", sourceFile
    
    errorin = np.genfromtxt(outFile, delimiter=",", skip_header=1, skip_footer=1, 
            usecols=(0,2))

################################################################################
# Import data from Stage 2 runs

if aType == "XRF-S2" or aType == "KED-S2":
    print "Extracting Stage 2 F8 tally..."
    with open(fileName) as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            if searchPhrase in line:
                for x in range (0,2052):
               	    line = search.next()
                    # remove the spaces between tally values 
                    # and replace with commas
                    line = line.replace('    ','')
                    line = line.replace('   ',',')
                    line = line.replace(' ',',')
               	    line = line.replace(',,energy,','energy')
                    line = line.replace(',,total,,','total,')
                    # write the data to analysis file in CSV format
               	    o.write(line)

# Close and reopen the file to flush the buffer
    o.close()
    o = open(outFile,"r")
################################################################################
# Normalize data from Stage 2 runs

if aType == "XRF-S2" or aType == "KED-S2":
    # import the source data from the preprocessed output file
    spectrumIn = np.genfromtxt(outFile, delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(0,1))
    #print spectrumIn
    #print "spectrumIn=",len(spectrumIn)
    
    s2Bins = np.genfromtxt(outFile, delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(0))
    s2Tally = np.genfromtxt(outFile, delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(1))
    s2Error = np.genfromtxt(outFile, delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(2))
    
    # Set correction factor
    corrFact = 1.0
    #corrFact = 0.99342
        
    # Convert Stage 2 bin energies to keV
    for i in range(0,len(s2Bins)):
        s2Bins[i] = s2Bins[i]*1000
        # Apply correction factor (see "Spectral Correction Factor.xlsx")
        s2Bins[i] = s2Bins[i]*corrFact
    
    # Initialize normalized tally matrix
    s2NormTal = np.zeros((len(s2Tally),1))
    #print s2NormTal
    
    # Normalize the Stage 2 tally
    for i in range(0,len(s2Tally)):
        s2NormTal[i] = s2Tally[i]/sum(s2Tally)
    

################################################################################
# Import data from measurement files

if importSpectrum == "y":
    # Get the file name from the user and open it
    #specFile = raw_input("Specify measured data file to import: ")
    #specFile = "u300_sal_x_201307220900_3_cnf.txt"
    m = open(specFile,"r")
    # Import the data into a spectrum variable
    measChannel = np.genfromtxt(specFile, delimiter=",",skip_header=1,
        usecols=(0))
    measSpectrum = np.genfromtxt(specFile, delimiter=",",skip_header=1,
        usecols=(1))
    infoLen = len(measSpectrum)
    #print infoLen
    spectInfo = np.genfromtxt(specFile, delimiter=",",skip_footer=infoLen)
    # Print the energy calibration
    print "Energy calibration: E(ch#)=",spectInfo[3],"+",spectInfo[4],"* ch#"

    # Initialize the energy calibrated array
    measEnergy = np.zeros((len(measChannel),1))
    # Apply energy calibration to measured spectra
    for i in range(0,len(measChannel)):
        measEnergy[i] = spectInfo[3]+spectInfo[4]*measChannel[i]
    
    # Initialize the normalized spectrum array
    measNormSpec = np.zeros((len(measSpectrum),1))
    
    # Normalize measured spectra for comparison
    for i in range(0,len(measSpectrum)):
        measNormSpec[i] = measSpectrum[i]/sum(measSpectrum)
        if measNormSpec[i] == 0:
            measNormSpec[i] == 1E-50
        
# Print message if not importing data
elif importSpectrum == "n":
    print "INFO: Measured data not imported"
    
################################################################################
# Run comparison algorithms 

if importSpectrum == "y":
    
    # Break out if arrays are not the same length
    if len(s2NormTal) != len(measNormSpec):
        print "Stage 2 tally & measured spectra not same length!"

    # Initialize residual array
    modelResid = np.zeros((len(s2NormTal),1))
    
    # Ask user if the spectrum is to be corrected
    corrCtl = "y" #raw_input("Correct spectal shift? (y,n): ")
    
    if corrCtl == "y":
        # Calcuate the channel offset using the imported energy calibration
        # Average simulated deviation from measured data
        avgOffset = 0.7071167 #keV
        #avgOffset = 0
        # Calculate channel offset
        chOffset = avgOffset / spectInfo[4]
        # Round and convert chOffset to integer
        chOffset = int(round(chOffset))
        print "INFO: MCNP spectrum corrected by",chOffset,"channels"
        
        # Initialize corrected array
        corrSpec = np.zeros((len(s2NormTal),1))
        corrError = np.zeros((len(s2NormTal),1))
        corrBins = np.zeros((len(s2NormTal),1))
        # Shift MCNP spectrum by calculated channel offset to nearest integer
        for i in range(chOffset,len(s2NormTal)):
            if i < len(s2NormTal):
                corrSpec[i-chOffset] = s2NormTal[i]
                corrError[i-chOffset] = s2Error[i]
                corrBins[i] = s2Bins[i]-avgOffset
            elif i == len(s2NormTal):
                print "INFO: Corrected spectrum generated"
    elif corrCtl == "n":
        print "INFO: Spectrum not corrected"
        
    if corrCtl == "y":
        # Calculate the relative difference in corrected spectra
        for i in range(chOffset,len(s2NormTal)):
            #modelResid[i] = (s2NormTal[i]-measNormSpec[i])/measNormSpec[i]
            if measNormSpec[i] == 0:
                modelResid[i] = 1E-50
            else:
                #modelResid[i] = math.sqrt(corrSpec[i]**2+measNormSpec[i]**2)
                #modelResid[i] = abs(1-(corrSpec[i]/measNormSpec[i]))]
                #modelResid[i] = abs((s2NormTal[i]-measNormSpec[i]))/measNormSpec[i]
                modelResid[i] = abs(1-(corrSpec[i]/measNormSpec[i]))
                
                


    #elif corrCtl == "n":
        ## Calculate the relative difference in spectra
        #for i in range(0,len(s2NormTal)):
        #    if measNormSpec[i] == 0:
        #        modelResid[i] = 1E-50
        #    else:
        #        modelResid[i] = (s2NormTal[i]-measNormSpec[i]) #/measNormSpec[i]
        
    # Convert from lists to arrays
    #s2Bins = np.asarray(s2Bins)
    #corrSpec = np.asarray(corrSpec)
    #corrError = np.asarray(corrError)
    
    # Convert from lists to vectors
    s2Bins = np.hstack(s2Bins)
    corrSpec = np.hstack(corrSpec)
    corrError = np.hstack(corrError)

    ## Sum the Ka and Kb peak ROIs for tally results
    #ka1sum = 0
    #ka2sum = 0
    #kbsum = 0
    #ka1start = 1336 
    #ka1end = 1364
    #ka2start = 1284
    #ka2end = 1309
    #kbstart = 1500
    #kbend = 1598
    ## Ka1
    #for i in range(ka1start,ka1end):
    #    ka1sum = corrSpec[i] + ka1sum
    ## Ka2
    #for i in range(ka2start,ka2end):
    #    ka2sum = corrSpec[i] + ka2sum        
    ## Kb
    #for i in range(kbstart,kbend):
    #    kbsum = corrSpec[i] + kbsum  
    ## Sum the Ka and Kb peak ROIs for tally results
    #ka1sumD = 0
    #ka2sumD = 0
    #kbsumD = 0
    #ka1startD = 1336 
    #ka1endD = 1364
    #ka2startD = 1284
    #ka2endD = 1309
    #kbstartD = 1500
    #kbendD = 1598
    ## Ka1
    #for i in range(ka1startD,ka1endD):
    #    ka1sumD = measNormSpec[i] + ka1sumD
    ## Ka2
    #for i in range(ka2startD,ka2endD):
    #    ka2sumD = measNormSpec[i] + ka2sumD        
    ## Kb
    #for i in range(kbstart,kbend):
    #    kbsumD = measNormSpec[i] + kbsumD
    #
    #print "Tally Ka1 Sum:",ka1sum
    #print "Tally Ka2 Sum:",ka2sum
    #print "Tally Kb Sum:",kbsum
    #print "Data Ka1 Sum:",ka1sumD
    #print "Data Ka2 Sum:",ka2sumD
    #print "Data Kb Sum:",kbsumD
        
# Print message if not plotting results
elif importSpectrum == "n":
    print "INFO: Spectral comparison not run"

################################################################################
# Plot the results

# If plotResults is "y" then call matplotlib
if plotResults == "y":
    
    # close any previous figures
    plt.close("all")
    
    # Prompt for plot title
    plotTitle = "" #raw_input("Enter string for plot title: ")
    
    # Set the figure dimensions
    plt.figure(figsize=(8,4))

    # Plot the tally results
    plt.subplot(2,1,1)
    plt.ylabel("Relative Intensity")
    plt.xlim((0,155))
    plt.ylim((1E-6,1E-1))
    plt.semilogy(s2Bins,corrSpec,color="red",label="MCNP")
    #plt.errorbar(s2Bins,corrSpec,yerr=corrError*corrSpec,color="red",
        #label="MCNP",errorevery=10)
    # Set the title
    plt.title(plotTitle) 

    # Plot the measured spectrum
    plt.subplot(2,1,1)
    plt.semilogy(measEnergy,measNormSpec,color="blue",label="Experimental")
    plt.xlim((0,155))
    plt.ylabel("Relative Intensity", fontsize=10)
    # Set the legend location
    plt.legend(loc=1,prop={'size':6})
    plt.tick_params(labelsize=12)
    plt.tick_params(which='both', width=1, labelsize=10)
    plt.tick_params(which='major', length=8)
    plt.grid(b=True,which="major")
    if aType == "XRF-S2":
        if sType == "U":
            # U case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,117,facecolor='0.5',alpha=0.25)
        elif sType == "U-Pu":
            # U-Pu case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
            plt.axvspan(93,99.09,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,116,facecolor='0.5',alpha=0.25)
            plt.axvspan(99.1,100,facecolor='g',alpha=0.25)
            plt.axvspan(103,104.5,facecolor='g',alpha=0.25)
            plt.axvspan(116.5,118,facecolor='g',alpha=0.25)
            plt.axvspan(119.5,121.5,facecolor='g',alpha=0.25)
    elif aType == "KED-S2":
        plt.axvspan(114,117,facecolor='0.5',alpha=0.25)
        
        
    # Plot the residuals
    plt.subplot(2,1,2)
    #plt.semilogy(s2Bins,modelResid, marker='.', linestyle='none')
    plt.scatter(corrBins,modelResid, marker='.',s=5)
    plt.xlabel("Energy (keV)", fontsize=10)
    plt.xlim((0,155))
    plt.ylim((10E-4,10E3))
    plt.yscale("log")
    plt.ylabel("Absolute Error", fontsize=10)
    plt.tick_params(labelsize=12)
    plt.tick_params(which='both', width=1,labelsize=10)
    plt.tick_params(which='major', length=8)
    plt.grid(b=True,which="major")
    if aType == "XRF-S2":
        if sType == "U":
            # U case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,117,facecolor='0.5',alpha=0.25)
        elif sType == "U-Pu":
            # U-Pu case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
            plt.axvspan(93,99.09,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,116,facecolor='0.5',alpha=0.25)
            plt.axvspan(99.1,100,facecolor='g',alpha=0.25)
            plt.axvspan(103,104.5,facecolor='g',alpha=0.25)
            plt.axvspan(116.5,118,facecolor='g',alpha=0.25)
            plt.axvspan(119.5,121.5,facecolor='g',alpha=0.25)
    elif aType == "KED-S2":
        plt.axvspan(114,117,facecolor='0.5',alpha=0.25)
        
    # Ask user to save the file
    saveFile = "y" #raw_input("Do you want to save full figure as a PDF? (y/n): ")
    if saveFile == "y":
        #figName = raw_input("Enter file name: ")
        plt.savefig(figName, dpi=1000, format='pdf', orientation='landscape', 
            bbox_inches='tight')
        plt.savefig(figName2, dpi=1000, format='png', orientation='landscape', 
            bbox_inches='tight')
    elif saveFile =="n":
        print "INFO: Figure not saved"

#######
# Plot detailed in version
# Set the figure dimensions
    plt.figure(figsize=(8,4))

    # Plot the tally results
    plt.subplot(2,1,1)
    plt.ylabel("Relative Intensity")
    #plt.xlim((90,120))
    plt.xlim((92,122))
    plt.ylim((1E-6,1E-1))
    plt.semilogy(s2Bins,corrSpec,color="red",label="MCNP")
    #plt.errorbar(s2Bins,corrSpec,yerr=corrError*corrSpec,color="red",
    #    label="MCNP",errorevery=10)
    ## Set the title
    plt.title(plotTitle) 

    # Plot the measured spectrum
    plt.subplot(2,1,1)
    plt.semilogy(measEnergy,measNormSpec,color="blue",label="Experimental")
    #plt.xlim((90,120))
    plt.xlim((92,122))
    plt.ylabel("Relative Intensity", fontsize=10)
    # Set the legend location
    plt.legend(loc=1,prop={'size':6})
    plt.tick_params(labelsize=12)
    plt.tick_params(which='both', width=1, labelsize=10)
    plt.tick_params(which='major', length=8)
    plt.grid(b=True,which="major")
    if aType == "XRF-S2":
        if sType == "U":
            # U case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,117,facecolor='0.5',alpha=0.25)
        elif sType == "U-Pu":
            # U-Pu case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
            plt.axvspan(93,99.09,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,116,facecolor='0.5',alpha=0.25)
            plt.axvspan(99.1,100,facecolor='g',alpha=0.25)
            plt.axvspan(103,104.5,facecolor='g',alpha=0.25)
            plt.axvspan(116.5,118,facecolor='g',alpha=0.25)
            plt.axvspan(119.5,121.5,facecolor='g',alpha=0.25)
    elif aType == "KED-S2":
        plt.axvspan(114,117,facecolor='0.5',alpha=0.25)
        
    # Plot the residuals
    plt.subplot(2,1,2)
    #plt.semilogy(s2Bins,modelResid, marker='.', linestyle='none')
    plt.scatter(corrBins,modelResid,marker='.',s=5)
    plt.xlabel("Energy (keV)", fontsize=10)
    plt.xlim((92,122))
    plt.ylim((10E-4,10E3))
    plt.yscale("log")
    plt.ylabel("Absolute Error", fontsize=10)
    plt.tick_params(labelsize=12)
    plt.tick_params(which='both', width=1,labelsize=10)
    plt.tick_params(which='major', length=8)
    plt.grid(b=True,which="major")
    if aType == "XRF-S2":
        if sType == "U":
            # U case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,117,facecolor='0.5',alpha=0.25)
        elif sType == "U-Pu":
            # U-Pu case
            plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
            plt.axvspan(93,99.09,facecolor='0.5',alpha=0.25)
            plt.axvspan(108,116,facecolor='0.5',alpha=0.25)
            plt.axvspan(99.1,100,facecolor='g',alpha=0.25)
            plt.axvspan(103,104.5,facecolor='g',alpha=0.25)
            plt.axvspan(116.5,118,facecolor='g',alpha=0.25)
            plt.axvspan(119.5,121.5,facecolor='g',alpha=0.25)
    elif aType == "KED-S2":
        plt.axvspan(114,117,facecolor='0.5',alpha=0.25)

    # Ask user to save the file
    saveFile = "y" #raw_input("Do you want to save zoomed figure as a PDF? (y/n): ")
    if saveFile == "y":
        #figNameROI = raw_input("Enter file name: ")
        plt.savefig(figNameROI, dpi=1000, format='pdf', orientation='landscape', 
            bbox_inches='tight')
        plt.savefig(figNameROI2, dpi=1000, format='png', orientation='landscape', 
            bbox_inches='tight')
    elif saveFile =="n":
        print "INFO: Figure not saved"
#######

    # show the plots
    plt.show()
# Print message if not plotting results
elif plotResults == "n":
    print "INFO: Results not plotted"
    

################################################################################
# close all open files
f.close()
o.close()
s.close()