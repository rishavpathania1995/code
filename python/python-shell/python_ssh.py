import subprocess
import time
import datetime
import argparse
import os
import threading


def fetch_engine_file(engine_server,Engine_query1,Engine_query2):

    # generating file in engine
    print("\033[32mStarted engine thread at:{}\033[0m".format(datetime.datetime.now()))
    print("Creating nse-drop.1.txt in {}".format(engine_server))

    trader_file_gen = subprocess.Popen(["ssh", "-t", engine_server, Engine_query1], shell=False, stdin=subprocess.PIPE,
                                       stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(5)
    # copying file in local directory
    print("Copying nse-drop.1.txt file in local directory  /files_missingtrade")

    trader_file = subprocess.Popen(["scp", "-Cr", Engine_query2, "."], shell=False, stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(10)


def fetch_database_file(current_date,database_server,Database_query1,Database_query2):
    # generating  file in database
    print("\033[32mStarted database thread at:{}\033[0m".format(datetime.datetime.now()))
    print("Creating trades file in {} ".format(database_server))

    database_file_gen = subprocess.Popen(["ssh", "-t", database_server, Database_query1, current_date], shell=False,
                                         stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(5)
    print("Copying database file in local directory /files_missingtrade")

    # copying file in local directory
    database_file = subprocess.Popen(["scp", "-Cr", Database_query2, "."], shell=False, stdin=subprocess.PIPE,
                                     stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    time.sleep(20)


# main function starts here
if __name__ == "__main__":

    print("\033[32mApplication started at {}\033[0m".format(datetime.datetime.now()))
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="Enter engine server.")
    parser.add_argument("-d", help="Enter db server.")
    parser.add_argument("-efile",help="Enter trades file.")
    parser.add_argument("-dfile",help="Enter database file.")
    parser.add_argument("--h", help="./python.py -e mt43 -d mt42.")
    args = parser.parse_args()

    # checking arguments
    file_path_present = True

    if args.efile is None and args.dfile is None:
        file_path_present = False
        print("No file arguments were passed  i.e -efime -dfile ")

    if file_path_present is False:

        try:
            engine_server = args.e
            database_server = args.d
            print("Arguments added engine server: {} databaseserver:{}".format(engine_server, database_server))

        except:
            print("Error in adding Engine server and Database server")


    # getting current system date time
    current_date = datetime.datetime.today()
    current_date = current_date.strftime("%Y-%m-%d")
    print(current_date)

    # Defining variable
    #engine_server = "mt43"
    #database_server = "mt42"

    # setting trades file
    filename_database = "trade_" + current_date + ".csv"
    filename_trader = "nse-drop-copy.1.txt"


    if file_path_present is True:
        filename_database = args.dfile
        filename_trader = args.efile
        print("Reading Directly from files")


    else:

        Engine_query1 = "cd ~/wallsoft_x_hftcore&&./nse-drop-copy"
        Engine_query2 = engine_server + ":~/wallsoft_x_hftcore/nse-drop-copy.1.txt"
        Database_query1 = "rm -f /var/lib/mysql-files/trade_" + current_date + ".csv" + "&&cd ~/Store/scripts/wallsoft_x_live_db_scripts/&&./extract_trade_dated.sh "
        Database_query2 = database_server + ":~/Store/scripts/wallsoft_x_live_db_scripts/trade_" + current_date + ".csv"
        #print(Database_query1)
        print(os.getcwd())

        if(engine_server == 'mt46-a'):
            engine_server = 'mt46'
            Engine_query1 = "cd /home/wsuser/ws-engine&&./nse-drop-copy"
            Engine_query2 = engine_server + ":/home/wsuser/ws-engine/nse-drop-copy.1.txt"

        if(engine_server == 'mt51'):
            Engine_query1 = "cd /home/rishi/wallsoft_x_hftcore&&./nse-drop-copy"
            Engine_query2 = engine_server + ":/home/rishi/wallsoft_x_hftcore/nse-drop-copy.1.txt"





        if "files_missingtrade" not in os.listdir():
            print("Dir not present")
            os.mkdir("files_missingtrade")
            print("Dir created")
            os.chdir("files_missingtrade")

        else:
            print(os.listdir())
            print("Files Present in /files_missingtrade Deleting files ...")
            os.chdir("files_missingtrade")
            print(os.getcwd())
            del_dir = subprocess.Popen(["rm", "-rf", "nse-drop-copy.1.txt", filename_database], shell=False,
                                       stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            #print(del_dir.stdout.readlines())
            print("Files deleted")

        time.sleep(3)

        thread_engine = threading.Thread(target=fetch_engine_file, args =(engine_server, Engine_query1, Engine_query2,))
        # fetching engine file
        #fetch_engine_file(engine_server, Engine_query1, Engine_query2)

        thread_database = threading.Thread(target=fetch_database_file, args =(current_date, database_server, Database_query1, Database_query2))
        #fetching database file
        #fetch_database_file(current_date, database_server, Database_query1, Database_query2)

        print(Engine_query1)
        print(Engine_query2)
        print(Database_query2)
        print(Database_query1)
        print(Database_query2)
        thread_database.start()
        thread_engine.start()
        thread_engine.join()
        thread_database.join()


    # print(trader_file_gen.stdout.readline())
    # print(trader_file.stderr.readline())


    #################**********************************************##################################


    try:

        file_trader = open(filename_trader, "r")
        file_database = open(filename_database, "r")
        print("\033[32mreading file ..... \033[0m")
        print(" ")

    except:
        print("!!!!!!please enter file names correctly")


    lines_trader = file_trader.readlines()
    lines_database = file_database.readlines()


    file_database.close()  # closing files
    file_trader.close()

    result = []  # dumy list
    result2 = []  # dumy list
    final_trader_id = []

    for x in lines_trader:
        result.append(x.split(',')[7])

    for y in result:
        result2.append(int(y.split(':')[1]))

    for z in range(len(result2)):
        final_trader_id.append(int(result2[z]))   #getting final trader fillingno file

    result4 = []  # dumy list
    result5 = []  # dumy list
    final_database_id = []

    for e in lines_database:
        result4.append(e.split(",")[11])

    for f in range(len(result4)):
        result5.append((result4[f]).split('"'))

    for g in range(len(result4)):
        final_database_id.append(int(result5[g][1]))   # getting final database fillingno file

    # compare and find missing values
    trade_missing = []
    database_missing = []
    trade_missing_line = []       # lines present in trader file but missing in database
    database_missing_line = []    # line present in database file but missing in trader file


    #finding missing trade  and its line no
    for t in range (0,len(lines_trader)):
        if final_trader_id[t] not in final_database_id:
            tt=t+1                                     # removing zero index
            trade_missing_line.append(tt)
            trade_missing.append(final_trader_id[t])

    #finding missing database trade and its line no
    for t1 in range (0,len(lines_database)):
        if final_database_id[t1] not in final_trader_id:
            tt1=t1+1                                 # removing zero index
            database_missing_line.append(tt1)
            database_missing.append(final_database_id[t1])

    print("\033[32mBroker trades:{} :\n{}\033[0m".format(len(final_trader_id), sorted(final_trader_id)))
    print("   ")
    print("\033[32mDatabase trades:{} :\n\{}\033[0m".format(len(final_database_id), sorted(final_database_id)))
    print("   ")

    #print(len(trade_missing_line))
    #print(len(lines_trader))
    print("\033[31mLines No Broker file{}\033[0m".format(trade_missing_line))
    print("   ")

    print("Total Broker trades:{}".format(len(final_trader_id)))
    print("\033[31m!Trade in trader file but not in database  :{}\n\033[0m".format(trade_missing))

    #prints missing trade
    if len(trade_missing_line) > 0:
        for tm1 in trade_missing_line:
            print("\033[31mLine :{}->{}\n\033[0m".format(tm1 ,lines_trader[tm1-1]))

    print("\033[31mLines No Database file{}\033[0m".format(database_missing_line))
    print("Total Database trades:{}".format(len(final_database_id)))
    print("\033[31m!Trade in database file but not in trader file:{}\n\033[31m".format(database_missing))

    #print missing database trade
    if len(database_missing_line) > 0:
        for tm2 in database_missing_line:
            print("\033[31mLine : {}->{}\n\033[0m".format(tm2,lines_database[tm2-1]))

