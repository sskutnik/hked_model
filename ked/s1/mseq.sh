#!/bin/bash
# MCNP sequential executor
# M. Cook (20150114)

# Tell the user what you're doing
echo "MCNP Sequential Executor"
echo "Which version of MCNP do you wish to execute (mcnp5 or mcnp6)?"

# Read in which MCNP to execute
read COMM

# Ask user how many cores to run on (if mcnp6)
if [ "$COMM" = "mcnp6" ]; then
	echo "Execute on how many cores?"
	read CORE
fi

# Execute MCNP for each input in directory
for f in *.inp; do
	echo "Executing MCNP for input $f..."
	# Execute MCNP...
	if [ "$COMM" = "mcnp5" ]; then
		# For single core on mcnp5
		$COMM i=$f name=journal_results/$f.
		else
		#echo $COMM i=$f o=$f.o TASKS $CORE
		$COMM i=$f wwinp=hked_v12_ked_s1.e name=results/new_xray/nobias/$f. TASKS $CORE
	fi
done

# Now rename the output files to *.o format
for f in *.inp.o; do
	# For each file with *.i.o extension 
	# rename to *.o
	mv "$f" "`basename $f .inp.o`.o"
done

# Remove runtapes
rm runt*

echo "Complete... Go Vols!"