let isPalindrome = function(x) {
    
    if(x < 0){
        return false;
    } else if(x === 0) {
        return true;
    }else if(x % 10 === 0){
        return false;
    } else {
        multiplier = 10
        x_arr = []
        while(multiplier <= x*10){
            x_arr.unshift((x % multiplier) / (multiplier / 10))
            x = x - (x % multiplier)
            multiplier *= 10
        }
        for(i=x_arr.length-1; i >= x_arr.length/2 ; i--){
            numAtSpot = x_arr[x_arr.length-(1+i)]
            reversedNumAtSpot = x_arr[i]
            if(numAtSpot !== reversedNumAtSpot){
                 return false;
            }
        }
        return true;
    }
}