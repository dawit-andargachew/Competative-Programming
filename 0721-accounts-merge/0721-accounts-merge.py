class DisJointSet:
    def __init__(self):
        self.representative = {}

    def union(self, personName, email):
        personrep = self.find(personName)
        emailrep = self.find(email)
        
        self.representative[emailrep] = personrep        

    def find(self, item):
        if item not in self.representative:
            self.representative[item] = item
            return item

        val = item
        while item != self.representative[item]:
            item = self.representative[item]
        
        # path compression
        while val != self.representative[val]:
            parent = self.representative[val]
            self.representative[val] = item
            val = parent

        return item


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # Here is Union Fold Problem, and wants to merge Groups which have a common email

        # We need to find a unique representative for each group. We can use `name + str(index)`
        # `name + str(indxe)` is UniqueAccount where index is the index of the array
        # So even if there are multiple similar names we can identify them uniquely
        
        # Then make union of UniqueAccount and the list of emails given in the array. 
        # During union only UniqueAccount are used as a representative.
                
        # What if there are common email? It is handled in the union methods and take this as example
        # [ 
        #   ["John","jsmith@mail.com","john@mail.com"], => UniqueAccount = john0
        #   ["John","jsmith@mail.com","jo0@mail.com"] => UniqueAccount = john1
        # ] 
        
        # In the above case have a common email  and we need to merge them.
        # Here is the union method and handle this in the following way
        
        # when we call union( john1, jsmith@gmail.com)
        #       personrep = self.find(personName) -> personrep = john1
        #       emailrep = self.find(email) -> emailrep = john0
        
        #       self.representative[emailrep] = personrep ->  representative[john0] = john1,  so the two become merged
        # 
        
        obj, NAMES = DisJointSet(), {}

        # iterate over the array and union personname with eamil
        for i in range( len(accounts) ):
            acc = accounts[i]
            
            account, UniqueAccount = acc[0], acc[0] + str(i)
            NAMES[ UniqueAccount ] = account # store unique names with their original name

            for j in range(1, len(acc)):
                obj.union( UniqueAccount, acc[j])

        # collect name and email on the same group
        # like this {name: [email-1, email-2], ... } 
        collect = defaultdict(list)
        for e in obj.representative:
            # names shouldn't be included in email list
            if e not in NAMES:
                collect[ obj.find(e)].append(e)

        # put them on a list to be returned 
        answer = []
        for k in collect:
            curr = sorted( collect[k] )
            answer.append([ NAMES[k],*curr ])

        return answer