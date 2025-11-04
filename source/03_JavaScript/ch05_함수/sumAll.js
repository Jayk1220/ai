function sumAll(){
    let result=0;
    if(arguments.length==0){
        result = -999;
        return result;

    }else if(arguments.length==1){
        result=arguments[0];
        return result;

    } else {
        for (let data of arguments) {
            result += data;
        }
        return result;
    }
}