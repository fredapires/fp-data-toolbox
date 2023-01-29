### Transformation functions below
###=============================================


### DONE function that loops over a list ;noted_on:2022-10-10
    #   includes progress bar 
    #   outputs list that then needs to be joined back into original df
def loop_over_list(index_list):
    output_list = [] # setup output list
    i = 0 # setup variable for looping progress bar
    for id in index_list:
        
        ### logic for determining new values goes here
        
        output_list.append() # append output list with new value
        
        ### loop orchestration below
        i = i + 1       ### iterate on integer
        progress_stat = str(round((i / index),2)) + ' / 1.0' # calc for progress
        print(progress_stat, end='\r') # print progress
    return output_list


