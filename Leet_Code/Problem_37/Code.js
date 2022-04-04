/**
 * @param {string} word
 * @return {boolean}
 */
 var detectCapitalUse = function(word) {
    let countCap = 0;
    let countNotCap = 0;
    let checkFirstLetter = false;
    if(word.charCodeAt(0) >= 65 && word.charCodeAt(0) <= 91)
    {
        checkFirstLetter = true;
        for(let i = 1; i < word.length; i++)
        {   
            if(word.charCodeAt(i) >= 65 && word.charCodeAt(i) <= 91)
            {
                countCap++;
            }    
            else
            {
                countNotCap++;    
            }
        }   
    }
    else
    {
        for(let i = 1; i < word.length; i++)
        {   
            if(word.charCodeAt(i) >= 97 && word.charCodeAt(i) <= 122)
            {
                 countNotCap++;
            }    
            else
            {
                return false;     
            }
        }   
    }
    
    if(checkFirstLetter === true && countNotCap === word.length - 1)
    {
       return true;
    }
    else if(checkFirstLetter === true && countCap === word.length - 1)
    {
       return true;
    }
    else if(countNotCap === word.length - 1)
    {
        return true;
    }
    else 
    {
        return false;
    }
};