/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
 var uncommonFromSentences = function(s1, s2) {
    const res = (s1, s2) => s1.concat(' ',s2)
    .split(' ')
    .filter((e, index, arr) => arr.indexOf(e) === arr.lastIndexOf(e))
    return res(s1, s2)

};