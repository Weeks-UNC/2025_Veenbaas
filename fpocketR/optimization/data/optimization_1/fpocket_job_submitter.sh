#!/bin/bash

### List (space seperated) values to run for each parameter. ###
### Number of values per parameter much be equal. ###
declare -a para_m=(2.6 3.0 3.4 3.8 4.2)
declare -a para_M=(5.4 5.8 6.2 6.6 7.0)
declare -a para_i=(10 15 20 25 30)
declare -a para_D=(1.6 2.0 2.4 2.8 3.2)

### Number of values to try per parameter. ###
x=5
# Counter.
y=0

for ((a = 0; a < $x; a++)); do
	m=${para_m[$a]}

for ((b = 0; b < $x; b++)); do
	M=${para_M[$b]}

for ((c = 0; c < $x; c++)); do	
	i=${para_i[$c]}

for ((e = 0; e < $x; e++)); do
	D=${para_D[$e]}

((y++))

echo "Parameters: -m $m -M $M -i $i -D $D"

while read line; do fpocket -f $line -m $m -M $M -i $i -D $D; done < fpocketFiles_PDB.txt

mkdir fpocketOutput.Riboswitches-m_$m-M_$M-i_$i-D_$D
mv *_Clean_out fpocketOutput.Riboswitches-m_$m-M_$M-i_$i-D_$D
rm -r *_Clean_out

done
done
done
done

echo "Finished! Number of parameter iterations: $y"