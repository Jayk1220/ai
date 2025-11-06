//dateGetNumberOfDays.js
//now.getNumberofDays(openday) =>55
Date.prototype.getNumberofDays = function(that){
    let intervalMilisec = Math.abs(this.getTime() - that.getTime()); //절대값
    let day = Math.floor(intervalMilisec/(1000*60*60*24));//내림
    return day; 
};
let now = new Date();
let limitday = new Date(2026,1,12,18,0,0);// 26.2.12
console.log(now.getNumberofDays(limitday),'일 남음');
console.log(limitday.getNumberofDays(now), '일 남음');
console.log(now.getNumberofDays(now));