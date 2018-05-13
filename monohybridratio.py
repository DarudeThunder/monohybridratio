print("======-----======-----======-----======-----======-----======")
print("Hello! Welcome to Andrew Chen's Program for Offspring Phenotype and Genotype Ratios!")
print("Please note that this program only works with monohybrids.")
print("Please use the letter 'A' to represent alleles. Eg: 'Aa' for heterozygous")
print("======-----======-----======-----======-----======-----======")
parent1 = input("What is the first parent's genotype? ")
if parent1 == "AA":
    print("The first parent is homozygous dominant.")
    allele1 = "A"
    allele2 = "A"
elif parent1 == "Aa":
    print("The first parent is heterozygous.")
    allele1 = "A"
    allele2 = "a"
elif parent1 == "aA":
    print("The first parent is heterozygous.")
    allele1 = "A"
    allele2 = "a"
elif parent1 == "aa":
    print("The first parent is homozygous recessive.")
    allele1 = "a"
    allele2 = "a"
else:
    print("I don't recognize that.")
parent2 = input("What is the second parent's genotype? ")
if parent2 == "AA":
    print("The second parent is homozygous dominant.")
    allele3 = "A"
    allele4 = "A"
elif parent2 == "Aa":
    print("The second parent is heterozygous.")
    allele3 = "A"
    allele4 = "a"
elif parent2 == "aA":
    print("The second parent is heterozygous.")
    allele3 = "A"
    allele4 = "a"
elif parent2 == "aa":
    print("The second parent is homozygous recessive.")
    allele3 = "a"
    allele4 = "a"
else:
    print("I don't recognize that.")
gen1 = allele1 + allele3
gen2 = allele2 + allele3
gen3 = allele1 + allele4
gen4 = allele2 + allele4
print("The possible genotypes are:")
print(gen1)
print(gen2)
print(gen3)
print(gen4)
dratio = 0
rratio = 0
hratio = 0
hdratio = 0
hrratio = 0
if gen1 == "AA":
    dratio = dratio + 1
    hdratio = hdratio + 1
elif gen1 == "Aa":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen1 == "aA":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen1 == "aa":
    rratio = rratio + 1
    hrratio = hrratio + 1
if gen2 == "AA":
    dratio = dratio + 1
    hdratio = hdratio + 1
elif gen2 == "Aa":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen2 == "aA":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen2 == "aa":
    rratio = rratio + 1
    hrratio = hrratio + 1
if gen3 == "AA":
    dratio = dratio + 1
    hdratio = hdratio + 1
elif gen3 == "Aa":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen3 == "aA":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen3 == "aa":
    rratio = rratio + 1
    hrratio = hrratio + 1
if gen4 == "AA":
    dratio = dratio + 1
    hdratio = hdratio + 1
elif gen4 == "Aa":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen4 == "aA":
    dratio = dratio + 1
    hratio = hratio + 1
elif gen4 == "aa":
    rratio = rratio + 1
    hrratio = hrratio + 1
print("The dominant:recessive phenotype ratio is:")
print(dratio)
print("to")
print(rratio)
print("The AA:Aa:aa genotype ratio is:")
print(hdratio)
print("to")
print(hratio)
print("to")
print(hrratio)