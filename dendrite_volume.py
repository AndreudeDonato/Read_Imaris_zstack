import sys
import os


# Get file names from command line
if len(sys.argv) > 1:
    input = sys.argv[1:]

# Else gets all file names with extension .csv
else:
    input = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            input.append(os.path.join(file))

delimiters = [";"] # All others delimiters that are not , get replaced

output = "output"
with open(output, "w") as outfile:

    for file in input:
        data = {}

        with open(file, "r") as fobj:
            flag = False

            for line in fobj:
                line = line.replace("\n", "")

                if flag is True:
                    for delimiter in delimiters:
                        line = line.replace(delimiter, ",")
                        line = line.split(",")

                        try:
                            dvolume = float(line[0])
                        except:
                            dvolume = 0
                            
                        if line[6] in data.keys():
                            data[line[6]] += dvolume
                        else:
                            data[line[6]] = dvolume


                if "Dendrite Volume" in line:
                    flag = True

        outfile.write(str(file) + "\n")
        for i in data:
            newline = str(i) + "    " + str(data[i])
            outfile.write(newline + "\n")
