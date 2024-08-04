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

                        branchid = int(line[0])
                            
                        if line[6] in data.keys():

                            if branchid in data[line[6]].keys():
                                data[line[6]][branchid] += 1

                            else:
                                data[line[6]][branchid] = 1

                        else:
                            data[line[6]] = {}


                if "Dendrite Branch" in line:
                    flag = True


            outfile.write(str(file) + "\n")

            for cellid in data:
                sorted_branchid = sorted(data[cellid].keys(), key=lambda x:x)
                outfile.write(" " + str(cellid) + "\n")

                for branch in sorted_branchid:
                    newline = str(branch) + "   " + str(data[cellid][branch])
                    outfile.write("  " + newline + "\n")

            outfile.write("\n")
