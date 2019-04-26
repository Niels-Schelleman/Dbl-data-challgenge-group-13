class RawDataUserFilter:

    def __init__(self, textfileloc, numfile):
        self.text = textfileloc
        self.num = numfile

    def textmaker(self):
        # opens and readies a text file containing all filenames
        filenames = open(self.text, 'r')
        filestring = filenames.read()
        listOfFilenames = filestring.split('\n')
        if self.num == 'all':
            listOfFilenames = listOfFilenames
        elif type(self.num) == int:
            listOfFilenames = listOfFilenames[0:self.num]
        else:
            print("error a non command value was inserted for numfile")
            listOfFilenames = {}
        return listOfFilenames

    def getKlmBawStd(self):
        # makes two empty list to dump all the dataframes into one for KLM one for british airways
        listOfFilenames = RawDataUserFilter(self.text, self.num).textmaker()
        frameklm = []
        framebrit = []

        # creates a for-loop which sifts through all the files
        for item in listOfFilenames:
            # reminder to see where the system is currently computing
            print("handling dataset:" + item)

            # takes the filename and inserts it into the Json to Dataframe object to turn it into a dataframe
            readable = jsonRead('json/' + item).JSONtoDf()

            # initialises a counter
            usernum = 0

            # checks for each user if the value is a dict, if not it gives a corresponding error message
            for i in list(readable['user']):
                if type(i) != dict:
                    if type(i) == float:
                        print("nan value changed to empty dict")
                    elif type(i) != float:
                        print('weird value changed to empty dict')
                    # changes non-dict values to be empty
                    readable['user'][usernum] = {}
                usernum += 1
            # try exept statement to catch any errors while not invalidating the processing of the rest of the data
            try:
                # takes the user dicts and turns them into rows of a dataframe
                subframe = pandas.DataFrame(list(readable['user']))

                # a dataframe containing all tweets whose user id is equal to the id of KLM for a certain json
                KLMlist = list(subframe[subframe['id'] == 56377143].index)
                # a dataframe containing all tweets whose user id is equal to the id for a certain json
                BritWaylist = list(subframe[subframe['id'] == 18332190].index)

                # appends all the dataframes per json to the corresponding empty list
                frameklm.append(readable[readable.index.isin(KLMlist)])
                framebrit.append(readable[readable.index.isin(BritWaylist)])
            except:
                # in case of an error, it prints this statement and continues on
                print('a critical error occured in dataframe:' + item)
            # returns the lists of datasets
        return (frameklm, framebrit)

    def getKlmBawBB(self):
        listOfFilenames = RawDataUserFilter(self.text, self.num).textmaker()
        frameklm = []
        framebrit = []
        for item in listOfFilenames:
            readable = jsonRead('json/' + item).JSONtoDf()
            usernum = 0
            for i in list(readable['user']):
                if type(i) != dict:
                    readable['user'][usernum] = {}
                usernum += 1
            try:
                subframe = pandas.DataFrame(list(readable['user']))
                KLMlist = list(subframe[subframe['id'] == 56377143].index)
                BritWaylist = list(subframe[subframe['id'] == 18332190].index)
                frameklm.append(readable[readable.index.isin(KLMlist)])
                framebrit.append(readable[readable.index.isin(BritWaylist)])
            except:
                print(item)
        return (frameklm, framebrit)

    def getReplyKlmBawStd(self):
        # gets a list of all files to be analyzed
        listOfFilenames = RawDataUserFilter(self.text, self.num).textmaker()
        # initialize list to put dataframes into
        RepToKlmList = []
        RepToBawList = []
        # gets a list of both all replies to klm and all replies to british airways in a file and adds them to a list
        for item in listOfFilenames:
            print('handling file:' + item)
            readable = jsonRead('json/' + item).JSONtoDf()
            RepToKlmList.append(readable[readable['in_reply_to_user_id'] == 56377143])
            RepToBawList.append(readable[readable['in_reply_to_user_id'] == 18332190])
        # returns filled lists
        return (RepToKlmList, RepToBawList)

    def getReplyKlmBawBB(self):
        listOfFilenames = RawDataUserFilter(self.text, self.num).textmaker()
        RepToKlmList = []
        RepToBawList = []
        for item in listOfFilenames:
            readable = jsonRead('json/' + item).JSONtoDf()
            RepToKlmList.append(readable[readable['in_reply_to_user_id'] == 56377143])
            RepToBawList.append(readable[readable['in_reply_to_user_id'] == 18332190])
        return (RepToKlmList, RepToBawList)