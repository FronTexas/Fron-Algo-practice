function withinRange(c){
    var _c = parseInt(c);
    return 1<=_c && _c<=26;
    
}
function mapDecoding(message) {
    if (message.length == 0 ) return 1
    dp = new Array(3);
    
    for(var i = 0; i < message.length;i++){
        dp[i] = 0
        if(i == 0){
            if(message[i] != 0){
                dp[i] = 1; 
            }
        }else{
            comb = message[i-1] + message[i];
            if(message[i] == 0){
                if(withinRange(comb)){
                    if(i > 1) {dp[i] = dp[i-2];}
                    else {dp[i] = 1}
                }
            }
            else {
                dp[i] = dp[i-1];
                if(message[i-1] != 0 && withinRange(comb)){
                    if (i > 1){
                        dp[i] += dp[i-2];
                    }else{
                        dp[i] += 1
                    }
                }
            }
        }
        dp[i] %= ((1000000000) + 7)
    }
    return dp[message.length-1]
}

// console.log(mapDecoding("301"));
// console.log(mapDecoding("1001"));
// console.log(mapDecoding("101221"));
// console.log(mapDecoding("10122110"));
// console.log(mapDecoding("1111"));
// console.log(mapDecoding("11115112112"));
// console.log(mapDecoding("2871221111122261"));
// console.log(mapDecoding("1012"));
console.log(mapDecoding("1221112111122221211221221212212212111221222212122221222112122212121212221212122221211112212212211211"));
