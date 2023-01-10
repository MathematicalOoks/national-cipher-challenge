# Upper case alphabet used to form the possible encryption keys
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Number of columns and rows used in this variation of the cadenus cipher
columns, rows = 5, 26
plain_text_row = [[0]*columns]*rows

# Arrays of expected cribs, current keys and keys added after testing
cribs = ["BETRAYAL", "ABRAHAM", "WOODHULL", "TALLMADGE", "WASHINGTON", "PSEUDONYM"]
known_keys = ["AOHDG", "BPIEH"]
keys = []

# function to start the recursive function that will generate all keys of length k
def generate_all_k_length(chars, k):
    n = len(alphabet)
    print_all_k_length_keys(chars, "", n, k)

# recursive function that generates all keys of length k and appends each
# key to the keys array
def print_all_k_length_keys(chars, prefix, n, k):
    if k == 0:
        keys.append(prefix)
        return

    for i in range(n):
        new_prefix = prefix + chars[i]
        print_all_k_length_keys(chars, new_prefix, n, k - 1)

generate_all_k_length(alphabet, columns)

# in the transposition cipher, no duplicates in keys are allowed
# therefore, this function removes all keys from the keys generated which contain duplicates
def remove_duplicates():
    unique_keys = []
    unique = False
    for i in keys:
        chars = set()
        unique = True
        for j in i:
            if j in chars:
                unique = False
                break
            chars.add(j)
        if unique:
            unique_keys.append(i)
    return unique_keys

final_keys = remove_duplicates()
print(final_keys, len(final_keys))

cipher_text = "IHRHG FTVEE EENNP OAIAO LARAE IEETI NNBKL SPREE ETNRM RAHSE NEUNI IUMND DTANW REAMO AYDMC DJNER ETSNA DAANF BYOAY MIDOI LJKRB GWHIU ANFTG BRESV MTFTA OAEEO OSERY OEEAS ANDTE TVODI OERSM SNNLC SHEEN NURYA LIAWN WPUDS UANNN EECMR CENAN ROITP LETBR RUYGH STNEN LOLGI OUEEG IASTF OLEEY RSMKI ITTIT DHCFS INSOU CEIIS EANOT EREME SINGI IANEA CVWEN MEIDR AEOTR DSRON RCOTT TTATG CUOLB EMEST DRFAI RIEAA NMTDU ROIEL DDLEE NFCUP AEWHT TLHNG CNRSN ATDRA NTELI ICNFD EEORE IVVEE SONIE HFSNH NATLR EAWUO OSTAT RISOS AOTSD SSASR ISIIE AROND ESTRU OWEAE SNLHT MENEI GKDDS TBELD UIPTN WAELM SDERT IOYEM GHWLO DPUUL VSTTD EMLGP CEODH PITRE AHFRH SYABT UNDOE COEEP RSSTD WIENM NMOID FRMEI NHYEC SSUDN MUNDS OSTAU CMDEN RADVT TAROT SNLAI SNISK UENCA EPELG ATSDE EAIRD SHBIT OEGPB ODEEF DISRO DNIST TSUEU CTSAC GWDRO ENOON IRWDE NNTOD ICINO MNLLO SSEOT FREOL MACSO OPSDO HDFIR GKTNE CIROE ROOHW BCCPN OARDI TNBKC AENOB IEUDT YEYOO FIGAM UDHGR CBONE ORHHI REHEE ROINS DRNUT ETIAA IXUAS OIEIE IDTRT ENNZM CTOLE CSCID NENCN PVOTT DOEGE OOOHD DRNFW UHENN AIURT SEDDD SSIYS RHHEL NEOSO USNEL VTMDG NWDTD AAMEL XANEF EIENR ECTOU NSKKO DTASH NGGEE IOTEE LEUEN RISOR OANGA LNTFC DRVUI NMDDA UHNLN MIVAD FNEBG OARRI TEEOA ERENN REIRE DERDI EDRUL DBITI SYATE NEOLF DSHER NRETB EIILO TOBDT OWRIR NSDAN HEEAU EETNS TNMRE MTSME OTLES TUHEI IIAIA TPGME HTEAA BMENT CNEAT EBNID ERGNT IDCRF NWCRH RNRDP REOOR RATOO USARC NBGTH HMLTE TPIAE EICFE FNLDT OPNNA INIHT AATTN TIDIO EETNR EEMRH EHABH GTTSE NUOEI ESTDE IOSIN HCTST BNNDR CANEN HNAWT NIYTH AITAS PSSCO EAOHA THBDO TBRDT MECIN WEGEG HEREE RNBOL HEKAN SNDFA SRXIY EOAGL TNESE MIAII YNGAX URETL ATEUG ENTPH NCCLS EHTID RLIAE PIBEA IYOOC VNIWR TLYEO AFITB HWOOL TATMP OFSGF LWIOD NFVTA TEDAD REUET HCOEW AMWNE NGNRE WPIAA TDEPO SIETE WMAHE SRRAE HIAST FHATN NERDT CSEUM NSDNE TOTTN EWRIT MLDEH GDMEH EABHS WSSOA SRTDT HDYDE GEOHO EFNIG IAHEI YMEAT UOEST ERXUA CEDVH TTAHN NOFSR TLNBU IERTI AEEDM WTPCR REDEE LHETH IEEEU UEISL IRITM CHYEH LVBTO TVAAF OBDAO PMWLN ODTLT SNHWO ATIBE EDXOT TTEIR THSPM OONGN EPHBO SOUOL FNHAG DTESI GLTNE TTEAT TRDMO LYVSM ESEAG ENSNE EOFNT OWTFP RSRWN RIRFA EGHEF LISOU IOTRA YTNHI HSPEE SFLIE DIGRS EEAIY ARESA HNNPI GESTT AXOSE IIYGA ENGPE TDNGE FEHOT EARPC WENNO NTBRD ERVLO EOTNO IGMRN EEOHR ESSOS DUDRL OFATL EEECI HNTET BDHUC RHBAO EASIT WTNSS NMHOO LLAON IGOHC ETSOS ECDRI ONIHX AEMSA ROSRU NRCAO HHOIV AIAAT NISVT HSNOH OSWUE TYISE REYOH NTEER LRNIM SLEHG TNTEE OROST OCENE NAFEL EBHDT OWHEI DOSER TTSAO XTUIE RSTFS TINPW IDIEE ELWCW AIFHC COAHL OHCVP NERXO HHACE EIEEE CEAOA NWTMM TCODN HDEED BFENA SCEAO SBTMK LNSGO HCNBP UDRKY OEYSE DETTS RENFH HEHET SOSUW UADEE STAOO EYTBA HLXWS YNIML EFATE TIAOS RPAIE ATNNI SROHS HMNBN AGROE BTOSE NEHHE SELDO MBOSS FTUED UEHAE STUOA XGTSD ITSET PTDBW DFRTA IYRTR EETIE RESND HOALS TOCIE TRNHT EDCPM EOEST HOOAE EARDA ERUYN SNHHE SREEF OOLAO TTNTT SIOWR ILOSE TNEIA ERTPN FHYOP EBRNR ANOIR NAMOD HUTMT ESNST HUBKP OMNEI CITSC REVAE FIKQB HCEIC CENHT ASTER SUAOS OOIAG FFNST POEEE IIEPE NOSRM HTTOE MRAAD ATUNI SEOUS MMALN KBSBT EFCEU FNRDU NYASO TESCE RGOBO TYGND HUNHE AITEU EEART NIOUY PEORW UNTNE IEAOC GRTCR RAMNN TSCIU QSHTI IAGTN HREEI ESKAU DAAXT SHUTE HAHER ESOEI ECOVT BOSGD IJTNN NTOUM SEALU IAFAO DFNAE INDAF TYTAT ENKGW RNOAE TRYES OSTND ATWNR SNRUN ESEOE ISNEE OITMR MNWTT OIAOT TRNNW ATNWT YWSYT IINOR DAAOO HAEHE SINWJ GTRHS NVNRT TEEON GOCEH KEEFR RISKH ESEOG KHIRS IFPAG DNIFO ADOEA REWKG HTITO WREEA ERCOR UWFUT OHEUE CFTNC RENOT OEOIT GACET RAOYO ICEIU TNEES ITDIO DHEOE NLSHO EISUS BDTNA RUOTE NERSD EARST DTADE EPEWT IUDAN ITPRI PHNIO ENOET EPTRV GAGRM RNUHU IRRVS EISGC LICMA USSTI OOMAN TEAEO YSDFR REEDN TDSRE OANSA YFGFR IMCTO LOAFM YITEM RIUTL SPTBE GFNNP NTSAU AOKGT YAVEI OMNYT RNOEM HIGSS KANPH FCRNR TATOO EATPE DOUHT NOEWT BELDS EDIDD EBOCB EEPTI OVEAE ATSRS EEEID LPIWR SPUHB ADVEH TNNFL ROENT OAIHU SEHNW EFFGD LTTOS EETEU DDHEV REEUN FUETA AWHAE OVTMC ARRHI TSWLH ONHEU"
cipher_text = ''.join(cipher_text.split())
block_size, index = columns * rows, 0
blocks = [[]]*(int(len(cipher_text)/block_size))
block, row = "", ""
# the first loop splits the text into block of size block_size
# then, the second loop splits each block into rows to form a grid structure
for i in range(len(cipher_text)):
    block += cipher_text[i]
    if (i + 1) % block_size == 0:
        print(block)
        blocks[index] = []
        for j in range(block_size):
            row += block[j]
            if (j + 1) % columns == 0:
                blocks[index].append(row)
                row = ""
        index += 1
        block = ""
print(blocks)

key_column_1 = {}
key_column_2 = {}
key_column_3 = {'A': 0}
counter = 0

# generates standard cadenus cipher key columns of length 26
for i in range(65, 91):
    key_column_1[chr(i)] = counter
    counter += 1
counter = 0
for i in range(90, 64, -1):
    key_column_2[chr(i)] = counter
    counter += 1
counter = 1
for i in range(90, 65, -1):
    key_column_3[chr(i)] = counter
    counter += 1

print(key_column_1)
print(key_column_2)
print(key_column_3)

# this function shifts each column upwards in each block of the ciphertext corresponding to the step given
# by the character at position "column" in the key. This step is decided by the key column used
def shift_columns(text, column, step):
    shifted_column = [0]*rows
    for i in range(len(text)):
        shifted_column[(rows - step + i) % rows] = text[i][column]
    return shifted_column

# this function will brute force the decryption of the cadenus cipher using the keys generated
# and the suspect key columns (to minimise output the plaintext is only printed if enough cribs are found
# in it
def decrypt_cadenus(text, sorted_key, unsorted_key, alphabet_key):
    final_decryption = ""
    column_map = {}
    cribs_found = 0
    for i in range(columns):
        new_column = shift_columns(text, i, alphabet_key[sorted_key[i]])
        column_map[sorted_key[i]] = new_column

    for i in range(rows):
        for j in unsorted_key:
            final_decryption += column_map[j][i]

    for i in cribs:
        if final_decryption.find(i) != -1:
            cribs_found += 1

    if cribs_found > 0:
        print(final_decryption)

    return cribs_found

# iterates through all keys of length 5 which were generated and are given as input
# to the decrypt function with the suspect key columns, which will output the decrypted text
# if enough cribs are found
for key in final_keys:
    plain_text_row = [[0]*columns]*rows
    if decrypt_cadenus(blocks[0], ''.join(sorted(key)), key, key_column_3) > 0:
        print(key)
