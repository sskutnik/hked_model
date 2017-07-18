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
print "-----------------------------"
print "| HKED Python Analysis Tool |"
print "-----------------------------"

# Hardcode file name in for now
#lib84 = raw_input("Enter file to analyze: ")
lib84 = "hked_v10_xrf_s2_300gL_Th.o"
lib12 = "hked_v11_xrf_s2_300gL_U.o"
specFile = "u300_sal_x_201307220900_3_cnf.txt"

################################################################################
# Open and create files needed by this script
# Open the input file for reading
f = open(lib84, "r")
g = open(lib12, "r")


o = open("lib84.opp","w")
p = open("lib12.opp","w")

################################################################################
# Determine the run type and search terms

# Tell the user what's going on
print "Processing MCNP output:", lib84
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
#print "MCNP tally extracted to:",outFile

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
    searchPhrase = "cell ..."
    print "Searched MCNP output for:", searchPhrase             
               
################################################################################

################################################################################
# Import data from lib84 Stage 2 runs

if aType == "XRF-S2" or aType == "KED-S2":
    print "Extracting Stage 2 F8 tally..."
    with open(lib84) as search:
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
    o = open("lib84.opp","r")
################################################################################
# Normalize data from Stage 2 runs

if aType == "XRF-S2" or aType == "KED-S2":
    # import the source data from the preprocessed output file
    spectrumInA = np.genfromtxt("lib84.opp", delimiter=",", skip_header=3, 
        skip_footer=1, usecols=(0,1))
    #print spectrumIn
    #print "spectrumIn=",len(spectrumIn)
    
    s2BinsA = np.genfromtxt("lib84.opp", delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(0))
    s2TallyA = np.genfromtxt("lib84.opp", delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(1))
    s2ErrorA = np.genfromtxt("lib84.opp", delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(2))
    
    # Set correction factor
    corrFact = 1.0
    #corrFact = 0.99342
        
    # Convert Stage 2 bin energies to keV
    for i in range(0,len(s2BinsA)):
        s2BinsA[i] = s2BinsA[i]*1000
        # Apply correction factor (see "Spectral Correction Factor.xlsx")
        s2BinsA[i] = s2BinsA[i]*corrFact
    
    # Initialize normalized tally matrix
    s2NormTalA = np.zeros((len(s2TallyA),1))
    #print s2NormTal
    
    # Normalize the Stage 2 tally
    for i in range(0,len(s2TallyA)):
        s2NormTalA[i] = s2TallyA[i]/sum(s2TallyA)
    

################################################################################

################################################################################
# Import data from mcplib12 Stage 2 runs

if aType == "XRF-S2" or aType == "KED-S2":
    print "Extracting Stage 2 F8 tally..."
    with open(lib12) as search:
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
               	    p.write(line)

# Close and reopen the file to flush the buffer
    p.close()
    p = open("lib12.opp","r")
################################################################################
# Normalize data from Stage 2 runs

if aType == "XRF-S2" or aType == "KED-S2":
    # import the source data from the preprocessed output file
    spectrumInB = np.genfromtxt("lib12.opp", delimiter=",", skip_header=3, 
        skip_footer=1, usecols=(0,1))
    #print spectrumIn
    #print "spectrumIn=",len(spectrumIn)
    
    s2BinsB = np.genfromtxt("lib12.opp", delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(0))
    s2TallyB = np.genfromtxt("lib12.opp", delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(1))
    s2ErrorB = np.genfromtxt("lib12.opp", delimiter=",", skip_header=3, skip_footer=1, 
            usecols=(2))
    
    # Set correction factor
    corrFact = 1.0
    #corrFact = 0.99342
        
    # Convert Stage 2 bin energies to keV
    for i in range(0,len(s2BinsB)):
        s2BinsB[i] = s2BinsB[i]*1000
        # Apply correction factor (see "Spectral Correction Factor.xlsx")
        s2BinsB[i] = s2BinsB[i]*corrFact
    
    # Initialize normalized tally matrix
    s2NormTalB = np.zeros((len(s2TallyB),1))
    #print s2NormTal
    
    # Normalize the Stage 2 tally
    for i in range(0,len(s2TallyB)):
        s2NormTalB[i] = s2TallyB[i]/sum(s2TallyB)
    

################################################################################


# Import data from measurement files

if importSpectrum == "y":
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
    if len(s2NormTalA) != len(measNormSpec):
        print "Stage 2 tally & measured spectra not same length!"

    # Initialize residual array
    modelResidA = np.zeros((len(s2NormTalA),1))
    
    # Ask user if the spectrum is to be corrected
    corrCtl = raw_input("Correct spectal shift? (y,n): ")
    
    if corrCtl == "y":
        # Calcuate the channel offset using the imported energy calibration
        # Average simulated deviation from measured data
        avgOffset = 0.7071167
        #avgOffset = 0
        # Calculate channel offset
        chOffset = avgOffset / spectInfo[4]
        # Round and convert chOffset to integer
        chOffset = int(round(chOffset))
        print "INFO: MCNP spectrum corrected by",chOffset,"channels"
        
        # Initialize corrected array
        corrSpecA = np.zeros((len(s2NormTalA),1))
        corrErrorA = np.zeros((len(s2NormTalA),1))
        # Shift MCNP spectrum by calculated channel offset to nearest integer
        for i in range(chOffset,len(s2NormTalA)):
            if i < len(s2NormTalA):
                corrSpecA[i-chOffset] = s2NormTalA[i]
                corrErrorA[i-chOffset] = s2ErrorA[i]
            elif i == len(s2NormTalA):
                print "INFO: Corrected spectrum generated"
    elif corrCtl == "n":
        print "INFO: Spectrum not corrected"
        
    if corrCtl == "y":
        # Calculate the relative difference in corrected spectra
        for i in range(0,len(s2NormTalA)):
            #modelResid[i] = (s2NormTal[i]-measNormSpec[i])/measNormSpec[i]
            if measNormSpec[i] == 0:
                modelResidA[i] = 1E-50
            else:
                modelResidA[i] = (corrSpecA[i]-measNormSpec[i])/measNormSpec[i]
    elif corrCtl == "n":
        # Calculate the relative difference in spectra
        for i in range(0,len(s2NormTalA)):
            if measNormSpec[i] == 0:
                modelResidA[i] = 1E-50
            else:
                modelResidA[i] = (s2NormTalA[i]-measNormSpec[i])/measNormSpec[i]
        
    # Convert from lists to arrays
    #s2Bins = np.asarray(s2Bins)
    #corrSpec = np.asarray(corrSpec)
    #corrError = np.asarray(corrError)
    
    # Convert from lists to vectors
    s2BinsA = np.hstack(s2BinsA)
    corrSpecA = np.hstack(corrSpecA)
    corrErrorA = np.hstack(corrErrorA)

# Print message if not plotting results
elif importSpectrum == "n":
    print "INFO: Spectral comparison not run"

################################################################################


################################################################################
# Run comparison algorithms 

if importSpectrum == "y":
    
    # Break out if arrays are not the same length
    if len(s2NormTalB) != len(measNormSpec):
        print "Stage 2 tally & measured spectra not same length!"

    # Initialize residual array
    modelResidB = np.zeros((len(s2NormTalB),1))
    
    # Ask user if the spectrum is to be corrected
    corrCtl = raw_input("Correct spectal shift? (y,n): ")
    
    if corrCtl == "y":
        # Calcuate the channel offset using the imported energy calibration
        # Average simulated deviation from measured data
        avgOffset = 0.7071167
        #avgOffset = 0
        # Calculate channel offset
        chOffset = avgOffset / spectInfo[4]
        # Round and convert chOffset to integer
        chOffset = int(round(chOffset))
        print "INFO: MCNP spectrum corrected by",chOffset,"channels"
        
        # Initialize corrected array
        corrSpecB = np.zeros((len(s2NormTalB),1))
        corrErrorB = np.zeros((len(s2NormTalB),1))
        # Shift MCNP spectrum by calculated channel offset to nearest integer
        for i in range(chOffset,len(s2NormTalB)):
            if i < len(s2NormTalB):
                corrSpecB[i-chOffset] = s2NormTalB[i]
                corrErrorB[i-chOffset] = s2ErrorB[i]
            elif i == len(s2NormTalB):
                print "INFO: Corrected spectrum generated"
    elif corrCtl == "n":
        print "INFO: Spectrum not corrected"
        
    if corrCtl == "y":
        # Calculate the relative difference in corrected spectra
        for i in range(0,len(s2NormTalB)):
            #modelResid[i] = (s2NormTal[i]-measNormSpec[i])/measNormSpec[i]
            if measNormSpec[i] == 0:
                modelResidB[i] = 1E-50
            else:
                modelResidB[i] = abs((corrSpecB[i]-measNormSpec[i]))/measNormSpec[i]
    elif corrCtl == "n":
        # Calculate the relative difference in spectra
        for i in range(0,len(s2NormTalB)):
            if measNormSpec[i] == 0:
                modelResidB[i] = 1E-50
            else:
                modelResidB[i] = abs(s2NormTalB[i]-measNormSpec[i])/measNormSpec[i]
        
    # Convert from lists to arrays
    #s2Bins = np.asarray(s2Bins)
    #corrSpec = np.asarray(corrSpec)
    #corrError = np.asarray(corrError)
    
    # Convert from lists to vectors
    s2BinsB = np.hstack(s2BinsB)
    corrSpecB = np.hstack(corrSpecB)
    corrErrorB = np.hstack(corrErrorB)

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
    plotTitle = raw_input("Enter string for plot title: ")
    #plotTitle = 'K X-ray Spectrum of 300 g/L Uranium in HNO3'
    
    # Set the figure dimensions
    plt.figure(figsize=(8,4))

    # Plot the tally results
    plt.subplot(1,1,1)
    plt.ylabel("Relative Intensity")
    #plt.xlabel("Energy (keV)")
    plt.xlim((0,140))
    plt.ylim((1E-7,1E-1))
    plt.yscale("log")
    #plt.semilogy(s2Bins,corrSpec,color="red",label="MCNP")
    plt.errorbar(s2BinsA,corrSpecA,color="red",
        label="Thorium",errorevery=10)
    plt.errorbar(s2BinsB,corrSpecB,color="blue",
        label="Uranium",errorevery=10)
    # Set the title
    plt.title(plotTitle) 

    ## Plot the measured spectrum
    #plt.subplot(1,1,1)
    #plt.semilogy(measEnergy,measNormSpec,color="blue",label="Experimental")
    #plt.xlim((0,155))
    #plt.ylabel("Relative Intensity", fontsize=10)
    plt.xlabel("Energy (keV)", fontsize=10)
    ## Set the legend location
    plt.legend(loc=1,prop={'size':8})
    plt.grid(b=True,which="major")
    #plt.tick_params(labelsize=12)
    #plt.tick_params(which='both', width=1, labelsize=10)
    #plt.tick_params(which='major', length=8)
    ##plt.tick_params(which='minor', length=6)
    #plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
    #plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
        
    ## Plot the residuals
    #plt.subplot(2,1,2)
    ##plt.semilogy(s2Bins,modelResid, marker='.', linestyle='none')
    #plt.scatter(s2BinsA,modelResidA, marker='.',s=3,color="red")
    #plt.xlabel("Energy (keV)", fontsize=10)
    #plt.xlim((0,155))
    #plt.ylim((-10,10))
    ##plt.ylim((-10,2300))
    #plt.ylabel("Error", fontsize=10)
    #plt.tick_params(labelsize=12)
    #plt.tick_params(which='both', width=1,labelsize=10)
    #plt.tick_params(which='major', length=8)
    ##plt.tick_params(which='minor', length=6)
    #plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
    #plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
    #
    ## Plot the residuals
    #plt.subplot(2,1,2)
    ##plt.semilogy(s2Bins,modelResid, marker='.', linestyle='none')
    #plt.scatter(s2BinsB,modelResidB, marker='.',s=3,color="green")
    #plt.legend(loc=1,prop={'size':6})
    #plt.xlabel("Energy (keV)", fontsize=10)
    #plt.xlim((0,155))
    #plt.ylim((10E-4,10E2))
    #plt.yscale("log")
    #plt.ylabel("Error", fontsize=10)
    #plt.tick_params(labelsize=12)
    #plt.tick_params(which='both', width=1,labelsize=10)
    #plt.tick_params(which='major', length=8)
    ##plt.tick_params(which='minor', length=6)


    # Ask user to save the file
    saveFile = raw_input("Do you want to save full figure as a PDF? (y/n): ")
    if saveFile == "y":
        figName = raw_input("Enter file name: ")
        plt.savefig(figName, dpi=1000, format='pdf', orientation='landscape', 
            bbox_inches='tight')
    elif saveFile =="n":
        print "INFO: Figure not saved"

######
    # Set the figure dimensions
    plt.figure(figsize=(8,4))

    # Plot the tally results
    plt.subplot(1,1,1)
    plt.ylabel("Relative Intensity")
    #plt.xlabel("Energy (keV)")
    plt.xlim((86,120))
    plt.ylim((1E-7,1E-1))
    plt.yscale("log")
    #plt.semilogy(s2Bins,corrSpec,color="red",label="MCNP")
    plt.errorbar(s2BinsA,corrSpecA,color="red",
        label="Thorium",errorevery=10)
    plt.errorbar(s2BinsB,corrSpecB,color="blue",
        label="Uranium",errorevery=10)
    # Set the title
    plt.title(plotTitle) 

    ## Plot the measured spectrum
    #plt.subplot(1,1,1)
    #plt.semilogy(measEnergy,measNormSpec,color="blue",label="Experimental")
    #plt.xlim((90,120))
    #plt.ylabel("Relative Intensity", fontsize=10)
    plt.xlabel("Energy (keV)", fontsize=10)
    ## Set the legend location
    plt.legend(loc=1,prop={'size':8})
    #plt.tick_params(labelsize=12)
    #plt.tick_params(which='both', width=1, labelsize=10)
    #plt.tick_params(which='major', length=8)
    ##plt.tick_params(which='minor', length=6)
    plt.grid(b=True,which="major")
    #plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
    #plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
        
    ## Plot the residuals
    #plt.subplot(2,1,2)
    ##plt.semilogy(s2Bins,modelResid, marker='.', linestyle='none')
    #plt.scatter(s2BinsA,modelResidA, marker='.',s=3,color="red")
    #plt.xlabel("Energy (keV)", fontsize=10)
    #plt.xlim((90,120))
    #plt.ylim((10E-4,10E2))
    #plt.yscale("log")
    #plt.ylabel("Abs. Error", fontsize=10)
    #plt.tick_params(labelsize=12)
    #plt.tick_params(which='both', width=1,labelsize=10)
    #plt.tick_params(which='major', length=8)
    ##plt.tick_params(which='minor', length=6)
    #plt.axvspan(93,100,facecolor='0.5',alpha=0.25)
    #plt.axvspan(108,118,facecolor='0.5',alpha=0.25)
    #
    ## Plot the residuals
    #plt.subplot(2,1,2)
    ##plt.semilogy(s2Bins,modelResid, marker='.', linestyle='none')
    #plt.scatter(s2BinsB,modelResidB, marker='.',s=3,color="green")
    #plt.legend(loc=1,prop={'size':6})
    #plt.xlabel("Energy (keV)", fontsize=10)
    #plt.xlim((90,120))
    #plt.ylim((10E-4,10E2))
    #plt.yscale("log")
    #plt.ylabel("Abs. Error", fontsize=10)
    #plt.grid(b=True,which="major")
    #plt.tick_params(labelsize=12)
    #plt.tick_params(which='both', width=1,labelsize=10)
    #plt.tick_params(which='major', length=8)
    ##plt.tick_params(which='minor', length=6)


    # Ask user to save the file
    saveFile = raw_input("Do you want to save zoomed figure as a PDF? (y/n): ")
    if saveFile == "y":
        figName = raw_input("Enter file name: ")
        plt.savefig(figName, dpi=1000, format='pdf', orientation='landscape', 
            bbox_inches='tight')
    elif saveFile =="n":
        print "INFO: Figure not saved"
#####



    # show the plots
    plt.show()
# Print message if not plotting results
elif plotResults == "n":
    print "INFO: Results not plotted"
    

################################################################################
# close all open files
f.close()
g.close()
o.close()
p.close()