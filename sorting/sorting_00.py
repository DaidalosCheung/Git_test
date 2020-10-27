import random
import time

def randm( scale ):
    array0 = []
    for i in range(scale):
        array0.append(i)
    print( array0 )
    
    random.shuffle( array0 )

    return array0

#----------------------------- BUBBLE SORT ------------------------------

def bubble( unsorted = [], *args ): # What is *args means:

    for i in range( (len(unsorted)-1) ):
        num = 0
        for j in range( len(unsorted)-1 - i):
            pivot = 0.0
            if unsorted[j] > unsorted[j+1] :
                pivot = unsorted[j+1]
                unsorted[j+1] = unsorted[j]
                unsorted[j] = pivot
                num += 1
        if num == 0:
            break
                
    return unsorted
#------------------------------ MERGE SORT ------------------------------

def merge( unsorted = [], *args ):

    #Set Sorted as temperal list, save each rounds result
    for i in range( len( unsorted ) ):
        templist = [];
        # Divide the list into dynamic sub-list
        for j in range( 0, len( unsorted ) / 2, 2 ** i ):
            m = 2 * j; 
            n = 2 * j + 2 ** i;
            if ( n >= len(unsorted) ):
                break;

            # Do the comparation, and assign the number to the new list
            for k in range( 2 * j, 2*( 2 * j + 2 ** i )-1 ):
                print( '\ni: ' + str(i) + '   j: ' + str(j) )
                print('m = %d, n= %d' %( m, n));
                if unsorted[m] > unsorted[n]:
                    templist.append( unsorted[n] );
                    print( templist );
                    n += 1;
                    print('Marker go to n: ' + str(n) + '---' + str(unsorted[n]) );
                    # If n list used out, put all remains elements from m list to the end
                    if n >= 2 * (j + 1):
                        templist += unsorted[ m : 2*j + 2**i ]
                        print('By the end of the round ' + str( templist ) );
                        break;

                else:
                    templist.append( unsorted[m] )
                    print( templist );
                    m += 1;
                    print('Marker go to m = ' + str(m) + '---' + str(unsorted[m]) );
                    # If m list used out, put all remains elements from n list to the end
                    if m >= 2 * j + 2**i: #if used out all list_n, but it does not work
                        templist += unsorted[ n : 2*( j + 1 ) ];
                        print( 'By the end of the round ' + str(templist) );
                        break1;


        if ( len( templist ) < len( unsorted ) ):
            templist += unsorted[ m :  ]
            print ( templist );

                            
        if 2**i > len( unsorted ) / 2:
            break;

        unsorted = templist
                    
            # If the sub-array larger than unsored array, stop iteration
            
    return unsorted;

################################ MAIN FUNCTION ################################

scale = int( input("Enter a scale: "  ))
arrayUnsorted = randm( scale )
print(arrayUnsorted)
start_time = time.time()

sortedArray = merge( arrayUnsorted )
print( sortedArray )
print("--------- %s seconds ---------" % (time.time() - start_time))

print("This is the 1st version for git")
