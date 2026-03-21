function getDividers(nbr){
    const list=[]
    for (i=1; i<=nbr; i++){
        if(nbr%i===0){
            list.push(i)
        }
    }
    return list
   
}
// ......................test

// console.log( getDividers(25));
 
