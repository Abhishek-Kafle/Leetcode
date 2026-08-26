class Solution(object):
    def topKFrequent(self, nums, k):
        num_of_ele = {}          #initial thought: append every number and then ad up their freuencies in the hash map
        return_list = []
        for i in nums:          #for loop: iterate through list and add their sum         
            if i in num_of_ele:
                num_of_ele[i] += 1
            else:
                num_of_ele[i] = 1
        #after this loop num_of_ele = {i in nums:freq_of(i)}

        #now we need these items sorted based on their frequency in descending order
        sorted_dict = sorted(num_of_ele.items(),key=lambda item: item[1], reverse = True)
        #this returns a list of items key value pairs in tuples ex:[(key,value)] 
        
        #iterate upto k and and append the key upto the kth term
        for i in range(k):
            return_list.append(sorted_dict[i][0])
        return(return_list)