

with open('local_fix.txt') as f1, open('global_fixed.txt') as f2,open ('fasta.txt') as f3, open('outfile11.txt', 'w') as outfile:
    masterlist = [row for row in f1]
    secondlist = [row for row in f2]
    thirdlist = [row for row in f3]

    for srow in masterlist:
        # Dosyalarda karşılaştırılacak bölüm:
        search = srow.split()

        for trow in secondlist:
            # Dosyalarda karşılaştırılacak bölüm
            target = trow.split()
            # Debug:
            # print(search[0], target[0])

                
            for strow in thirdlist:
                # Dosyalarda karşılaştırılacak bölüm
                target2 = strow.split()
                # Debug:
                # print(search[0], target[0])
                
                if search[0] == target[0] and search[0]== target2[0]:
                    print(srow.rstrip(),trow.rstrip(),strow, end=' ', file=outfile)
#                if search[0] == target2[0]:
#                    print(strow, end='', file=outfile)  