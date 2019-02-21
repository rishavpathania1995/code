# !/usr/bin/python
#https://www.tutorialspoint.com/python/os_walk.htm
import json
import os
import re
import sys
local_path = os.getcwd()

path = input("Please enter Path : ")

if path is "":
    path = "/mnt/wsraid_nfs"

os.chdir(path)

d = {}
list1 = []
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      #print(os.path.join(root, name))
      list1.append(os.path.join(root, name))

print(list1)



#pattern = r"^./(NSE_FO_TBT_DATA)/(stream)/(\d{4}_\d{2}_\d{2})/(contract.gz)$"
#pattern2 = r"^./(NSE_FO)/(stream)/(\d{4}_\d{2}_\d{2})/(Nse_FO_TbtStream\d)_\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.dat.bz2$"

pattern_fo_info = r"^./(NSE_FO)/(\d{4}_\d{2}_\d{2})/fo_contract_stream_info.csv.bz2$"
pattern_fo_stream = r"^./(NSE_FO)/(\d{4}_\d{2}_\d{2})/(Nse_FO_TbtStream\d)_\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.dat.bz2$"
pattern_fo_contract = r"^./(NSE_FO)/(\d{4}_\d{2}_\d{2})/(contract.gz.bz2)$"

pattern_cd_contract = r"^./(NSE_CD)/(\d{4}_\d{2}_\d{2})/cd_contract.gz.bz2$"
pattern_cd_stream = r"^./(NSE_CD)/(\d{4}_\d{2}_\d{2})/(Nse_CDS_TbtStream\d)_\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.dat.bz2$"
pattern_cd_info = r"^./(NSE_CD)/(\d{4}_\d{2}_\d{2})/cd_contract_stream_info.csv.bz2$"

pattern_cm_contract = r"^./(NSE_CM)/(\d{4}_\d{2}_\d{2})/security.gz.bz2$"
pattern_cm_stream = r"^./(NSE_CM)/(\d{4}_\d{2}_\d{2})/(Nse_CM_TbtStream\d)_\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.dat.bz2$"
pattern_cm_info = r"^./(NSE_CM)/(\d{4}_\d{2}_\d{2})/cm_contract_stream_info.csv.bz2$"

d["WarehousePathPrefix"] = os.getcwd()
d["NSE_EQUITY_DERIVATIVE"] = {}
d["NSE_EQUITY"] = {}
d["NSE_CURRENCY_DERIVATIVE"] = {}


for sequence in list1:

    #############  FO section ############

    if re.match(pattern_fo_stream, sequence):
        ob = re.match(pattern_fo_stream, sequence)
        #print(ob.group(1), ob.group(2))
        date = ob.group(2).replace("_", '')
        #print(date)

        d["NSE_EQUITY_DERIVATIVE"][date] = d.get("NSE_EQUITY_DERIVATIVE").get(date, {})    # checking if already exists or not
        #print((ob.group(2)))

        if ob.group(3) == 'Nse_FO_TbtStream1':

            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath1"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream2':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath2"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream3':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath3"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream4':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath4"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream5':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath5"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream6':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath6"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream7':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath7"] = sequence[2:]

        if ob.group(3) == 'Nse_FO_TbtStream8':
            d["NSE_EQUITY_DERIVATIVE"][date]["StreamFilePath8"] = sequence[2:]

    if re.match(pattern_fo_contract, sequence):
        ob = re.match(pattern_fo_contract, sequence)
        date = ob.group(2).replace("_", '')
        #print(ob.group(1),ob.group(2))
        d["NSE_EQUITY_DERIVATIVE"][date] = d.get("NSE_EQUITY_DERIVATIVE").get(date, {})
        d["NSE_EQUITY_DERIVATIVE"][date]["ContractFilePath"] = sequence[2:]


    if re.match(pattern_fo_info, sequence):
        ob = re.match(pattern_fo_info, sequence)
        date = ob.group(2).replace("_", '')
        #print(ob.group(1),ob.group(2))
        d["NSE_EQUITY_DERIVATIVE"][date] = d.get("NSE_EQUITY_DERIVATIVE").get(date, {})
        d["NSE_EQUITY_DERIVATIVE"][date]["StreamInfoFilePath"] = sequence[2:]

    ############## END FO SECTION ##########

    ############ CM SECTION #############

    if re.match(pattern_cm_stream, sequence):
        ob = re.match(pattern_cm_stream ,sequence)
        date = ob.group(2).replace("_", '')
        d["NSE_EQUITY"][date] = d.get("NSE_EQUITY").get(date, {})

        if ob.group(3) == "Nse_CM_TbtStream1":
            d["NSE_EQUITY"][date]["StreamFilePath1"] = sequence[2:]

        if ob.group(3) == "Nse_CM_TbtStream2":
            d["NSE_EQUITY"][date]["StreamFilePath2"] = sequence[2:]

        if ob.group(3) == "Nse_CM_TbtStream3":
            d["NSE_EQUITY"][date]["StreamFilePath3"] = sequence[2:]

        if ob.group(3) == "Nse_CM_TbtStream4":
            d["NSE_EQUITY"][date]["StreamFilePath4"] = sequence[2:]

    if re.match(pattern_cm_contract, sequence):
        ob = re.match(pattern_cm_contract,sequence)
        date = ob.group(2).replace("_", '')
        d["NSE_EQUITY"][date] = d.get("NSE_EQUITY").get(date, {})
        d["NSE_EQUITY"][date]["ContractFilePath"] = sequence[2:]

    if re.match(pattern_cm_info, sequence):
        ob = re.match(pattern_cm_info,sequence)
        date = ob.group(2).replace("_", '')
        d["NSE_EQUITY"][date] = d.get("NSE_EQUITY").get(date ,{})
        d["NSE_EQUITY"][date]["StreamInfoFilePath"] = sequence[2:]



    ########### END CM SECTION ##############

    ############  START CD SECTION ###########


    if re.match(pattern_cd_stream, sequence):
        ob = re.match(pattern_cd_stream, sequence)
        date = ob.group(2).replace("_", '')
        d["NSE_CURRENCY_DERIVATIVE"][date] = d.get("NSE_CURRENCY_DERIVATIVE").get(date,{})

        if ob.group(3) == "Nse_CDS_TbtStream1":
            d["NSE_CURRENCY_DERIVATIVE"][date]["StreamFilePath1"] = sequence[2:]

    if re.match(pattern_cd_contract, sequence):
        ob = re.match(pattern_cd_contract, sequence)
        date = ob.group(2).replace("_",'')
        d["NSE_CURRENCY_DERIVATIVE"][date] = d.get("NSE_CURRENCY_DERIVATIVE").get(date, {})
        d["NSE_CURRENCY_DERIVATIVE"][date]["ContractFilePath"] = sequence[2:]

    if re.match(pattern_cd_info, sequence):
        ob = re.match(pattern_cd_info, sequence)
        date = ob.group(2).replace("_",'')
        d["NSE_CURRENCY_DERIVATIVE"][date] = d.get("NSE_CURRENCY_DERIVATIVE").get(date, {})
        d["NSE_CURRENCY_DERIVATIVE"][date]["StreamInfoFilePath"] = sequence[2:]


print(json.dumps(d, indent=2, sort_keys=True))

os.chdir(local_path)
print(os.getcwd())

with open("file.json", 'w') as file:
    json.dump(d, file)



*/