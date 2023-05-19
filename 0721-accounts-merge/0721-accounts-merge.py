class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # Here is Union Fold Problem, and wants to merge Groups which have a common email

        # person name can be used as a representative for a given group but it is not unique. 
        #   So to make each name:
        #                   1, store in separte dictionary
        #                   2, add each row index in to the name so that each can be unique 
        #                       like {John0: john, John1: john} even if John is the same are unique and represent a given group


        represent, NAMES = {}, {}
        def union(person, email):
            person_rep = find(person)
            email_rep = find(email)
            represent[email_rep] = person_rep
        
        def find(name):
            if name not in represent:
                represent[name] = name
                return name
            
            while name != represent[name]:
                name = represent[name]
            return name

        # iterate over the array and union personname with eamil
        for i in range( len(accounts) ):
            acc = accounts[i]
            NAMES[acc[0]+str(i)] = acc[0]

            for j in range(1, len(acc)):
                union(acc[0]+str(i) , acc[j])

        # collect name and email on the same group
        # like this {name: emails} => 
        collect = defaultdict(list)
        for e in represent:
            # names shouldn't be included in email list
            if e not in NAMES:
                collect[ find(e)].append(e)
        
        # put them on a list to be returned 
        answer = []
        for k in collect:
            curr = sorted( collect[k] )
            answer.append([ NAMES[k],*curr])

        return answer