/**
 * @param {number} num
 * @return {number}
 */
 var addDigits = function(num) {
    let str = num.toString();
    let new_str = "";
    let new_num = 0;
    if(str.length === 1)
    {
        return parseInt(str);
    }
    else 
    {
        do 
        {
            for(let i = 0; i < str.length; i++)
            {
                new_num += parseInt(str[i]);
            }
            new_str = new_num.toString();
            str = new_str;
            new_num = 0;
            // console.log(new_num);
            // console.log(new_str);
            // console.log(str);
        }
        while(str.length != 1);
    }
    return parseInt(str);
};